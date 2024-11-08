import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 700
screen_height = 700

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load images
wizard_image = pygame.image.load("resized_wizard.gif")
treasure_image = pygame.image.load("resized_treasure.gif")
wall_image = pygame.image.load("resized_wall.gif")
enemy_r_image = pygame.image.load("resized_enemy_r.gif")
enemy_l_image = pygame.image.load("resized_enemy_l.gif")

# Resize images to match the 24x24 size
wizard_image = pygame.transform.scale(wizard_image, (24, 24))
treasure_image = pygame.transform.scale(treasure_image, (24, 24))
wall_image = pygame.transform.scale(wall_image, (24, 24))
enemy_r_image = pygame.transform.scale(enemy_r_image, (24, 24))
enemy_l_image = pygame.transform.scale(enemy_l_image, (24, 24))

# Setup maze
levels = [
    "",
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XP XXXXXXXE         XXXXX",
        "X  XXXXXXX  XXXXXX  XXXXX",
        "X       XX  XXXXXX  XXXXX",
        "X       XX  XXX       EXX",
        "XXXXXX  XX  XXX        XX",
        "XXXXXX  XX  XXXXXX  XXXXX",
        "XXXXXX  XX    XXXX  XXXXX",
        "X  XXX        XXXXT XXXXX",
        "X  XXX  XXXXXXXXXXXXXXXXX",
        "X         XXXXXXXXXXXXXXX",
        "X                XXXXXXXX",
        "XXXXXXXXXXXX     XXXXX  X",
        "XXXXXXXXXXXXXXX  XXXXX  X",
        "XXX  XXXXXXXXXX         X",
        "XXXE                    X",
        "XXX         XXXXXXXXXXXXX",
        "XXXXXXXXXX  XXXXXXXXXXXXX",
        "XXXXXXXXXX              X",
        "XX   XXXXX              X",
        "XX   XXXXXXXXXXXXX  XXXXX",
        "XX    YXXXXXXXXXXX  XXXXX",
        "XX          XXXX        X",
        "XXXXE                   X",
        "XXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
]


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([24, 24], pygame.SRCALPHA)
        pygame.draw.circle(self.image, ORANGE, (12, 12), 10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = wizard_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.gold = 0
        self.lives = 5
        self.start_x = 100
        self.start_y = 100
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.power_up_active = False
        self.power_up_end_time = 0

    def update(self, keys, walls):
        # Update power-up status
        if self.power_up_active and time.time() > self.power_up_end_time:
            self.power_up_active = False
            self.invulnerable = False

        if self.invulnerable and not self.power_up_active:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False

        # Get the player's new position based on key presses
        original_position = self.rect.copy()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 24
        if keys[pygame.K_RIGHT]:
            self.rect.x += 24
        if keys[pygame.K_UP]:
            self.rect.y -= 24
        if keys[pygame.K_DOWN]:
            self.rect.y += 24

        # Check for collision with walls and revert position if needed
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect = original_position

    def activate_power_up(self):
        self.power_up_active = True
        self.invulnerable = True
        self.power_up_end_time = time.time() + 10  # 10 seconds duration

    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.power_up_active = False
        self.invulnerable = False

    def hit_by_enemy(self):
        if not self.invulnerable and not self.power_up_active:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_timer = 20
            return True
        return False


class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = treasure_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = enemy_l_image if direction == 'left' else enemy_r_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self, walls):
        original_position = self.rect.copy()

        if self.direction == 'up':
            self.rect.y -= 24
        elif self.direction == 'down':
            self.rect.y += 24
        elif self.direction == 'left':
            self.rect.x -= 24
            self.image = enemy_l_image
        elif self.direction == 'right':
            self.rect.x += 24
            self.image = enemy_r_image

        if pygame.sprite.spritecollide(self, walls, False):
            self.rect = original_position
            self.direction = random.choice(['up', 'down', 'left', 'right'])


def find_empty_spaces(level):
    empty_spaces = []
    for y, row in enumerate(level):
        for x, char in enumerate(row):
            if char == ' ':  # Only consider empty spaces
                empty_spaces.append((x * 24, y * 24))
    return empty_spaces


def spawn_power_up(walls, empty_spaces):
    if not empty_spaces:
        return None

    # Choose a random empty space
    x, y = random.choice(empty_spaces)
    return PowerUp(x, y)


def setup_maze(level):
    walls = pygame.sprite.Group()
    treasures = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    power_ups = pygame.sprite.Group()
    empty_spaces = []

    for y, row in enumerate(level):
        for x, char in enumerate(row):
            screen_x = x * 24
            screen_y = y * 24

            if char == 'X':
                wall = pygame.sprite.Sprite()
                wall.image = wall_image
                wall.rect = wall.image.get_rect()
                wall.rect.x = screen_x
                wall.rect.y = screen_y
                walls.add(wall)
            elif char == 'P':
                player.rect.x = screen_x
                player.rect.y = screen_y
                player.start_x = screen_x
                player.start_y = screen_y
            elif char == 'T':
                treasure = Treasure(screen_x, screen_y)
                treasures.add(treasure)
            elif char == 'E':
                enemy = Enemy(screen_x, screen_y, random.choice(['up', 'down', 'left', 'right']))
                enemies.add(enemy)
            elif char == ' ':
                empty_spaces.append((screen_x, screen_y))

    # Add initial power-up in a valid empty space
    if empty_spaces:
        power_ups.add(spawn_power_up(walls, empty_spaces))

    return walls, treasures, enemies, power_ups, empty_spaces


def reset_game():
    player.lives = 5
    player.reset_position()
    return setup_maze(levels[1])


# Initialize player and maze
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup maze level
walls, treasures, enemies, power_ups, empty_spaces = setup_maze(levels[1])
all_sprites.add(walls, treasures, enemies, power_ups)

# Font setup
font = pygame.font.Font(None, 74)
power_up_spawn_timer = time.time() + 15  # Spawn first power-up after 15 seconds

# Game states
PLAYING = 0
GAME_OVER = 1
VICTORY = 2
game_state = PLAYING

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (game_state == GAME_OVER or game_state == VICTORY):
                walls, treasures, enemies, power_ups, empty_spaces = reset_game()
                all_sprites = pygame.sprite.Group()
                all_sprites.add(player, walls, treasures, enemies, power_ups)
                game_state = PLAYING
            elif event.key == pygame.K_q and (game_state == GAME_OVER or game_state == VICTORY):
                running = False

    if game_state == PLAYING:
        # Handle player movement
        keys = pygame.key.get_pressed()
        player.update(keys, walls)

        # Check for power-up collection
        power_up_hits = pygame.sprite.spritecollide(player, power_ups, True)
        if power_up_hits:
            player.activate_power_up()

        # Spawn new power-up periodically
        if time.time() > power_up_spawn_timer and len(power_ups) < 1:
            new_power_up = spawn_power_up(walls, empty_spaces)
            if new_power_up:
                power_ups.add(new_power_up)
                all_sprites.add(new_power_up)
            power_up_spawn_timer = time.time() + 15

        # Check for victory
        if pygame.sprite.spritecollide(player, treasures, True):
            game_state = VICTORY

        # Check for collisions with enemies
        if pygame.sprite.spritecollide(player, enemies, False):
            if player.hit_by_enemy():
                print(f"Player hit! Lives remaining: {player.lives}")
                if player.lives <= 0:
                    game_state = GAME_OVER

        # Update all enemies
        for enemy in enemies:
            enemy.update(walls)

    # Clear the screen
    screen.fill(BLACK)  # Using black background

    # Draw all sprites
    all_sprites.draw(screen)

    # Display lives
    lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
    screen.blit(lives_text, (10, 10))

    # Display power-up status
    if player.power_up_active:
        time_left = int(player.power_up_end_time - time.time())
        power_up_text = font.render(f"Power-up: {time_left}s", True, ORANGE)
        screen.blit(power_up_text, (10, 60))

    # Handle game states
    if game_state == GAME_OVER:
        game_over_text = font.render("GAME OVER", True, RED)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        text_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2))
        restart_rect = restart_text.get_rect(center=(screen_width / 2, screen_height / 2 + 60))
        screen.blit(game_over_text, text_rect)
        screen.blit(restart_text, restart_rect)

    elif game_state == VICTORY:
        victory_text = font.render("PLAYER WINS!", True, GOLD)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        text_rect = victory_text.get_rect(center=(screen_width / 2, screen_height / 2))
        restart_rect = restart_text.get_rect(center=(screen_width / 2, screen_height / 2 + 60))
        screen.blit(victory_text, text_rect)
        screen.blit(restart_text, restart_rect)

    # Update the screen
    pygame.display.update()

    # Control the frame rate
    clock.tick(10)

    

# Quit pygame
pygame.quit()