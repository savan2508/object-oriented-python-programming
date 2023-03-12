import random

from IPython.display import clear_output


def display_board(board):
    clear_output()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ['X', 'O']

    else:
        return ['O', 'X']


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # win check for the tic-tac-toe
    # Check if all the row share the same marker
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # Check for the horizontal rows
            (board[4] == board[5] == board[6] == mark) or  # Check for the horizontal rows
            (board[7] == board[8] == board[9] == mark) or  # Check for the horizontal rows
            (board[7] == board[4] == board[1] == mark) or  # Check for the vertical rows
            (board[8] == board[5] == board[2] == mark) or  # Check for the vertical rows
            (board[9] == board[6] == board[3] == mark) or  # Check for the vertical rows
            (board[7] == board[5] == board[3] == mark) or  # Check for the diagonal rows
            (board[1] == board[5] == board[9] == mark))  # Check for the diagonal rows


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player, marker):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{player} ({marker}) choose a position: (1-9) '))

    return position


def replay():

    choice = input("Play again? Enter Yes or No")

    return choice == 'Yes'


print('Welcome to the TIC TAC TOE')

while True:

    #  PLAY THE GAME

    # Set everything up
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()

    print(turn + 'will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            # Display the board
            display_board(the_board)

            # choose as position
            position = player_choice(the_board, 'Player 1', player1_marker)

            # Place the marker on the board
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print("The game is TIE!")
                    game_on = False

                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)

            position = player_choice(the_board, 'Player 2', player2_marker)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board()
                    print("The game is TIE!")
                    game_on = False

                else:
                    turn = 'Player 1'
            #
    if not replay():
        break
