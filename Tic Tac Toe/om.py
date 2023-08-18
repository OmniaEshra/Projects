import numpy as np


def create_board():
    return np.array([['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']])


def print_board(board):
    print(board)


def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move. Try again.")
        return False
    elif board[row][col] != '-':
        print("Position already occupied. Try again.")
        return False
    return True





def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] != '-') or (board[0][2] == board[1][1] == board[2][0] != '-'):
        return board[1][1]

    # No winner
    return None


def play_game():
    current_player = 'X'
    game_board = create_board()

    while True:
        print_board(game_board)

        try:
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))
            
            if is_valid_move(game_board, row, col):
                make_move(game_board, row, col, current_player)
                winner = check_winner(game_board)
                if winner:
                    print_board(game_board)
                    print(f"Player {winner} wins!")
                    break
                # Switch players only if the move was valid
                current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Please enter a number.")
        except IndexError:
            print("Please enter an index between 0 and 2")

play_game()
