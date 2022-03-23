"""
Name: <Jalena Austin>
<TicTacToe>.py

Problem: <Use a collection of functions to create a user-friendly and interactive play of the original game of
    tictactoe.>

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
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[7] == board[3]:
        return True
    if board[1] == board[9] == board[3]:
        return True
    if board[2] == board[9] == board[3]:
        return True
    if board[0] == board[9] == board[4]:
        return True
    if board[2] == board[7] == board[2]:
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
    if game_over(board) == (board[0] == board[1] == board[2]):
        return 'x'
    if game_over(board) == (board[3] == board[4] == board[5]):
        return 'x'
    if game_over(board) == (board[6] == board[7] == board[8]):
        return 'x'
    if game_over(board) == (board[0] == board[7] == board[3]):
        return 'x'
    if game_over(board) == (board[1] == board[9] == board[3]):
        return 'x'
    if game_over(board) == (board[2] == board[9] == board[3]):
        return 'x'
    if game_over(board) == (board[0] == board[9] == board[4]):
        return 'x'
    if game_over(board) == (board[0] == board[9] == board[4]):
        return 'x'
    if game_over(board) == (board[2] == board[7] == board[2]):
        return 'x'
    if game_over(board) == (board[0] == board[1] == board[2]):
        return 'o'
    if game_over(board) == (board[3] == board[4] == board[5]):
        return 'o'
    if game_over(board) == (board[6] == board[7] == board[8]):
        return 'o'
    if game_over(board) == (board[0] == board[7] == board[3]):
        return 'o'
    if game_over(board) == (board[1] == board[9] == board[3]):
        return 'o'
    if game_over(board) == (board[2] == board[9] == board[3]):
        return 'o'
    if game_over(board) == (board[0] == board[9] == board[4]):
        return 'o'
    if game_over(board) == (board[0] == board[9] == board[4]):
        return 'o'
    if game_over(board) == (board[2] == board[7] == board[2]):
        return 'o'
    if not game_over(board):
        return None


def play(board):
    build_board()
    print_board(board)
    user_choice = eval(input('Instructions: Welcome to Tic Tac Toe! Type in a number (1 through 9) to place your position on the board. X will start first. '))

    while not game_over(board):
        player = 0
        for i in board:
            player += i
            if player % 2 == 0:
                print('x' + "'s turn.")
            else:
                print('o' + "'s turn.")
            position = int(user_choice) - 1
            board = position[0:8]
            is_legal(board, position)
            fill_spot(board, position, player)
            winning_game(board)

        if get_winner(board) == 'x' or get_winner(board) == 'o':
            print(get_winner(board) + 'won!')
        else:
            print('Tie')
        user_input = input('Do you want to play again?').lower()
        if user_input == 'y' or user_input == 'yes':
            return user_choice
        else:
            break


def main():
    pass


if __name__ == '__main__':
    main()
