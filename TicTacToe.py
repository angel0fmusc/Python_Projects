from random import randint

def player_input():
    '''
        Request player to choose X or O.
        Allow input to be lowercase.
        :return: tuple of player marker positions
    '''
    marker = ''

    # Keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def display_board(board):
    print('\n'*2)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---'*3)
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---' * 3)
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def place_marker(board, marker, position):
    '''
        Place marker on board
            :param board: list
            :param marker: string
            :param position: index of board list
            :return: none
    '''
    board[position] = marker


def win_check(board, mark):
    '''
        Check if given mark has won the game
        :param board: list; indexes 0-10 only using 1-9
        :param mark: X or 0; string
        :return: boolean if mark won the board
    '''
    return(
        (board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right
        (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonal
        (board[7] == mark and board[5] == mark and board[3] == mark)    # diagonal
    )


def choose_first():
    '''
        Choose whether Player 1 or Player 2 will go first
        :return: string
    '''
    if randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    '''
        Check if position requested is available
        Return True if the index at the requested location is empty
        Otherwise, return False
            :param board: list of 10
            :param position: index to check in list
            :return: boolean
    '''
    return board[position] == ' '


def full_board_check(board):
    '''
        Check if the board is full.
        Return True if the board is full; otherwise, return False
            :param board: list of 10
            :return: boolean
    '''

    for i in range(1, 10):
        # If there is an empty space on the board, it is not full.
        # Return False
        if space_check(board, i):
            return False
    # Board is full
    return True


def player_choice(board):
    '''
        Ask for the player's next position (as a number 1-9) and use the space_check function to check if the position
        is free. If so, return the position for later use
            :param board: list
            :return: index of free position
    '''
    choice = 0

    # If the position is not in the list of choice, or the space is not free,
    # Choose a new position
    while choice not in range(1, 10) or not space_check(board, choice):
        choice = int(input(f"{turn}, choose a position 1 - 9: "))

    return choice


def replay():
    '''
        As the player if they want to play again.
        Return True if yes; otherwise, return False
        :return: Boolean
    '''
    choice = input("Do you want to play again? Enter 'Yes' or 'No': ")

    return choice == "Yes"


print('Welcome to Tic Tac Toe!')

while True:
    board = [' ']*10
    display_board(board)

    player1, player2 = player_input()

    turn = choose_first()
    print(f'{turn} will go first')

    play_game = input("Do you want to play a game? Enter Yes or No. ")

    if play_game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1's turn
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print('Congratulations, Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print(f"Congratulations, Player 2! You won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break