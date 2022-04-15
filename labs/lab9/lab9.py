"""
Name: <Jalena Austin>
<TicTacToe>.py

Problem: <Use a collection of functions to create a user-friendly and interactive play of the original game of
    tic-tac-toe.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""


def build_board():
    board_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_nums


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    for j in range(0, 9, 3):
        if board[j] == board[j + 1] == board[j + 2]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    for i in board:
        if str(i).isnumeric():
            return False
    return True


def get_winner(board):
    if not game_over(board):
        return None

    for i in range(3):
        if 'x' == board[i] == board[i + 3] == board[i + 6]:
            return 'x'
        else:
            return 'o'
    for j in range(0, 9, 3):
        if 'x' == board[j] == board[j + 1] == board[j + 2]:
            return 'x'
        else:
            return 'o'
    if 'x' == (board[0] == board[8] == board[4]):
        return 'x'
    if 'x' == (board[2] == board[7] == board[2]):
        return 'x'
    if 'o' == (board[0] == board[8] == board[4]):
        return 'o'
    if 'o' == (board[2] == board[7] == board[2]):
        return 'o'


def play(board):
    print('Instructions: Welcome to Tic Tac Toe! Type in a number (1 through 9) to place your position on the board.')
    print('To start playing answer the question below to start your game. Good luck!')
    print_board(board)
    begin_game = input('Do you want to play (yes or no)? ')
    while begin_game[0] == 'y':
        spot_play = 0
        while spot_play <= 9 and not game_over(board):
            player = ''
            if (spot_play % 2) == 0:
                player += 'x'
            elif (spot_play % 2) == 1:
                player += 'o'
            player_switch = int(input("It is {}'s turn, choose a spot on the board 1 through 9. ".format(player)))
            while not is_legal(board, player_switch):
                player_switch = int(input("This position is already filled. Choose a new position (1 through 9): "))
            fill_spot(board, player_switch, player)
            print_board(board)
            spot_play += 1
            if game_over(board):
                if (winning_game(board) and get_winner(board)) == ('x' and 'o'):
                    print("{} won". format(player))
                else:
                    print("Tie")

        begin_game = input('Do you want to play again?').lower()
        board = build_board()


def main():
    pass


if __name__ == '__main__':
    main()
