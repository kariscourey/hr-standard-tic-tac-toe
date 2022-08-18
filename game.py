def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()


def game_over(board, number):
        print_board(board)
        print("GAME OVER")
        print(number, "has won")
        exit()


def top_row_is_winner(board):
    return game_over(board, board[0])

def middle_row_is_winner(board):
    return game_over(board, board[3])

def bottom_row_is_winner(board):
    return game_over(board, board[6])

def left_column_is_winner(board):
    return game_over(board, board[0])

def middle_column_is_winner(board):
    return game_over(board, board[1])

def right_column_is_winner(board):
    return game_over(board, board[2])

def left_diagonal_is_winner(board):
    return game_over(board, board[0])

def right_diagonal_is_winner(board):
    return game_over(board, board[0])

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if top_row_is_winner(board):
        game_over(board, board[0])
    elif middle_row_is_winner(board):
        game_over(board, board[3])
    elif bottom_row_is_winner(board):
        game_over(board, board[6])
    elif left_column_is_winner(board):
        game_over(board, board[0])
    elif middle_column_is_winner(board):
        game_over(board, board[1])
    elif right_column_is_winner(board):
        game_over(board, board[2])
    elif left_diagonal_is_winner(board):
        game_over(board, board[0])
    elif right_diagonal_is_winner(board):
        game_over(board, board[0])

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
