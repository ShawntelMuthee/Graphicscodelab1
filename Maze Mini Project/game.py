import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MOVE_DISTANCE = 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Load images
wizard_image = pygame.image.load("resized_wizard.gif")
treasure_image = pygame.image.load("resized_treasure.gif")
wall_image = pygame.image.load("resized_wall.gif")
enemy_r_image = pygame.image.load("resized_enemy_r.gif")
enemy_l_image = pygame.image.load("resized_enemy_l.gif")

# Resize images to 24x24
wizard_image = pygame.transform.scale(wizard_image, (24, 24))
treasure_image = pygame.transform.scale(treasure_image, (24, 24))
wall_image = pygame.transform.scale(wall_image, (24, 24))
enemy_r_image = pygame.transform.scale(enemy_r_image, (24, 24))
enemy_l_image = pygame.transform.scale(enemy_l_image, (24, 24))

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Maze layout levels
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

# Game states
PLAYING = 0
GAME_OVER = 1
VICTORY = 2


# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = wizard_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.gold = 0
        self.lives = 3
        self.invulnerable = False
        self.invulnerable_timer = 0

    def update(self, keys, walls):
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False

        original_position = self.rect.copy()

        # Move based on key input
        if keys[pygame.K_LEFT]:
            self.rect.x -= MOVE_DISTANCE
        elif keys[pygame.K_RIGHT]:
            self.rect.x += MOVE_DISTANCE
        elif keys[pygame.K_UP]:
            self.rect.y -= MOVE_DISTANCE
        elif keys[pygame.K_DOWN]:
            self.rect.y += MOVE_DISTANCE

        # Check wall collision and bounce back if collision occurs
        if pygame.sprite.spritecollideany(self, walls):
            self.rect = original_position

    def hit_by_enemy(self):
        if not self.invulnerable:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_timer = 20
            return True
        return False


class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = treasure_image
        self.rect = self.image.get_rect(topleft=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = enemy_l_image if direction == 'left' else enemy_r_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        self.change_direction_timer = 30

    def update(self, walls):
        if self.change_direction_timer <= 0:
            # Randomize direction
            self.direction = random.choice(['up', 'down', 'left', 'right'])
            self.change_direction_timer = 30

        original_position = self.rect.copy()

        # Movement based on direction
        if self.direction == 'up':
            self.rect.y -= MOVE_DISTANCE
        elif self.direction == 'down':
            self.rect.y += MOVE_DISTANCE
        elif self.direction == 'left':
            self.rect.x -= MOVE_DISTANCE
            self.image = enemy_l_image
        elif self.direction == 'right':
            self.rect.x += MOVE_DISTANCE
            self.image = enemy_r_image

        # Bounce back and randomize direction on wall collision
        if pygame.sprite.spritecollideany(self, walls):
            self.rect = original_position
            self.direction = random.choice(['up', 'down', 'left', 'right'])

        self.change_direction_timer -= 1


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = wall_image
        self.rect = self.image.get_rect(topleft=(x, y))


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, GOLD, (12, 12), 12)  # Draw a circle to create the sphere effect
        self.rect = self.image.get_rect(center=(x, y))  # Position it in the maze
        self.respawn_timer = 180 # Timer for respawn delay
        self.active = True  # Power-up is initially active

    def spawn(self, walls, maze):
        """Ensure the power-up doesn't spawn on walls and is within the valid maze area."""
        valid_positions = []
        for y, row in enumerate(maze):
            for x, char in enumerate(row):
                if char == ' ' and not self.collides_with_wall(x * MOVE_DISTANCE, y * MOVE_DISTANCE, walls):
                    valid_positions.append((x * MOVE_DISTANCE, y * MOVE_DISTANCE))

        if valid_positions:
            self.rect.x, self.rect.y = random.choice(valid_positions)

    def collides_with_wall(self, x, y, walls):
        """Check if a given (x, y) position collides with a wall."""
        temp_rect = pygame.Rect(x, y, MOVE_DISTANCE, MOVE_DISTANCE)
        return any(temp_rect.colliderect(wall.rect) for wall in walls)

    def update(self, walls, maze):
        """Update the respawn timer and deactivate when time is up."""
        if not self.active:
            self.respawn_timer -= 1
            if self.respawn_timer <= 0:
                self.active = True  # Reactivate the power-up after timer expires
                self.spawn(walls, maze)  # Spawn at a new valid position

    def trigger_respawn(self, walls, maze):
        """Trigger the respawn mechanism after a fixed period of time."""
        if self.active:
            self.active = False  # Deactivate the power-up
            self.respawn_timer = 300  # Set to 300 frames for 5 seconds (approximately)
            self.spawn(walls, maze)  # Spawn at a new location when triggered

# Setup functions and main game loop
def setup_maze(level, player):
    walls = pygame.sprite.Group()
    treasures = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    powerups = pygame.sprite.Group()  # To store power-ups

    for y, row in enumerate(level):
        for x, char in enumerate(row):
            screen_x = x * MOVE_DISTANCE
            screen_y = y * MOVE_DISTANCE
            if char == 'X':
                wall = Wall(screen_x, screen_y)
                walls.add(wall)
            elif char == 'P':
                player.rect.x = screen_x
                player.rect.y = screen_y
            elif char == 'T':
                treasure = Treasure(screen_x, screen_y)
                treasures.add(treasure)
            elif char == 'E':
                enemy = Enemy(screen_x, screen_y, random.choice(['up', 'down', 'left', 'right']))
                enemies.add(enemy)

    # Add power-ups to random locations
    for _ in range(3):  # You can adjust the number of power-ups
        power_up = PowerUp(random.randint(0, (SCREEN_WIDTH // MOVE_DISTANCE) - 1) * MOVE_DISTANCE,
                           random.randint(0, (SCREEN_HEIGHT // MOVE_DISTANCE) - 1) * MOVE_DISTANCE)
        power_up.spawn(walls, level)  # Pass the maze layout to the spawn method
        powerups.add(power_up)

    return walls, treasures, enemies, powerups



def display_score(player):
    score_text = font.render(f"Treasures: {player.gold}  Lives: {player.lives}", True, GOLD)
    screen.blit(score_text, (10, 10))


def display_game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))


def display_victory():
    victory_text = font.render("VICTORY! YOU WIN!", True, GOLD)
    screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 2))


def reset_game(player):
    player.lives = 3
    player.gold = 0
    return setup_maze(levels[1], player)


def main():
    player = Player()
    all_sprites = pygame.sprite.Group(player)

    walls, treasures, enemies, powerups = setup_maze(levels[1], player)
    all_sprites.add(walls, treasures, enemies, powerups)

    game_state = PLAYING
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_state in (GAME_OVER, VICTORY):
                    walls, treasures, enemies, powerups = reset_game(player)
                    all_sprites = pygame.sprite.Group(player, walls, treasures, enemies, powerups)
                    game_state = PLAYING
                elif event.key == pygame.K_q and game_state in (GAME_OVER, VICTORY):
                    running = False

        keys = pygame.key.get_pressed()

        if game_state == PLAYING:
            player.update(keys, walls)
            enemies.update(walls)

            # Check for collisions with treasures
            if pygame.sprite.spritecollide(player, treasures, True):
                player.gold += 1
                if not treasures:  # Check for victory if no treasures are left
                    game_state = VICTORY

            # Check for collisions with power-ups and increase lives
            if pygame.sprite.spritecollide(player, powerups, True):
                player.lives += 1  # Restore a life when collecting a power-up

            # Check for collisions with enemies
            if pygame.sprite.spritecollideany(player, enemies):
                if player.hit_by_enemy():
                    if player.lives <= 0:
                        game_state = GAME_OVER

        # Update power-ups and handle respawn logic
        for power_up in powerups:
            power_up.update(walls, levels[1])  # Pass walls and maze to update method

        # Trigger respawn for power-ups periodically
        for power_up in powerups:
            power_up.trigger_respawn(walls, levels[1])  # Pass walls and maze to respawn

        # Draw everything
        screen.fill(BLACK)
        all_sprites.draw(screen)
        display_score(player)

        # Display game state message if game is over or won
        if game_state == GAME_OVER:
            display_game_over()
            restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        elif game_state == VICTORY:
            display_victory()
            restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()
        clock.tick(10)  # Set to 10 FPS for demonstration

    pygame.quit()



if __name__ == "__main__":
    main()
