# Tic Tac Toe Game
This repository contains a Python script that implements a game of Tic Tac Toe, using the command line interface. The game requires two players, who take turns placing their respective markers (either 'X' or 'O') on a 3x3 grid. The first player to align three of their markers horizontally, vertically, or diagonally wins the game.

# How to Play
1. Clone the repository to your local machine.
2. Install Python (version 3.6 or higher) and the IPython module (version 7.0 or higher) if they are not already installed
Open a terminal window and navigate to the directory containing the cloned repository.
3. Run the command python tic_tac_toe.py to start the game.
4. Follow the prompts to choose your marker ('X' or 'O'), decide who goes first, and play the game.
5. The game ends when one player wins or the board is full (a tie).
6. After the game ends, you will be prompted to play again or exit the game.

# Code Overview
The Python script tic_tac_toe.py contains the following functions:

display_board(board): Prints the current state of the game board to the command line interface.

player_input(): Asks the user to choose a marker ('X' or 'O') and returns a list containing the markers for each player.

place_marker(board, marker, position): Places the specified marker on the board at the specified position.

win_check(board, mark): Returns True if the specified player's markers are aligned to win the game.

choose_first(): Randomly selects which player goes first.

space_check(board, position): Returns True if the specified position on the board is empty.

full_board_check(board): Returns True if the board is full.

player_choice(board, player, marker): Asks the specified player to choose a position on the board and returns the chosen position.

replay(): Asks the user if they want to play again and returns True if they do.

The main program uses these functions to run the game, using a while loop to continue playing until the user chooses to exit.
