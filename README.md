**Maze Game**:
A 2D maze game developed using Python and Pygame. The game features a player, enemies, treasures, walls, and power-ups that respawn after a short period. The player must collect treasures while avoiding enemies and navigating through the maze.

**Features**:
Player Movement: Move the player with arrow keys.
Enemies: Randomly move enemies that can reduce the player's lives if touched.
Treasure: Collect treasures to increase score.
Power-ups: Collect power-ups to increase lives. Power-ups respawn after a short delay.
Game States: The game includes the following states:
Playing: The game is active.
Game Over: The player loses all lives.
Victory: The player collects all treasures.

**Game Controls**:
Arrow Keys: Move the player around the maze.
R: Restarts the game after a game over or victory.
Q: Quits the game.

**Requirements**:
Python 3.x
Pygame library
The game runs in a virtual python environment (v.env)

You can install Pygame using the following command:
pip install pygame

**Setup**:
Clone or download the repository.
Place the necessary image files.

**How to Play**:
Objective: Collect all treasures and avoid the enemies.
The player has 5 lives to start with. Every time the player is hit by an enemy, a life is deducted. The player can collect power-ups to increase their lives.
Victory: Collect all treasures to win the game.
Game Over: Lose all lives and the game ends.

**Code Structure**:
Main Functions
setup_maze(level, player): Sets up the maze, placing walls, treasures, enemies, and power-ups.
display_score(player): Displays the score, including the number of remaining lives.
display_game_over(): Displays the game over message.
display_victory(): Displays the victory message.
reset_game(player): Resets the game state, lives, and score.

**Game Classes**:
Player: Represents the player character. Handles movement and interaction with treasures, enemies, and power-ups.
Treasure: Represents a treasure that the player can collect to gain points.
Enemy: Represents an enemy that randomly moves and can reduce the player's lives upon collision.
Wall: Represents a wall that the player and enemies cannot pass through.
PowerUp: Represents a power-up item that the player can collect to gain extra lives. Power-ups respawn after a delay.

**Game Loop**:
The game runs in a loop where it continuously checks for player input, updates the game state, handles collisions, and updates the display.
