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


def is_row_winner(board, row):
    if row == 1:
        return board[0] == board[1] and board[1] == board[2]
    elif row == 2:
        return board[3] == board[4] and board[4] == board[5]
    else:
        return board[6] == board[7] and board[7] == board[8]

def is_column_winner(board, column):
    if column == 1:
        return board[0] == board[3] and board[3] == board[6]
    elif column == 2:
        return board[1] == board[4] and board[4] == board[7]
    else:
        return board[2] == board[5] and board[5] == board[8]

def is_diag_winner(board, diag):
    if diag == "left":
        return board[0] == board[4] and board[4] == board[8]
    else:
        return board[2] == board[4] and board[4] == board[6]


# def top_row_is_winner(board):
#     return board[0] == board[1] and board[1] == board[2]

# def middle_row_is_winner(board):
#     return board[3] == board[4] and board[4] == board[5]

# def bottom_row_is_winner(board):
#     return board[6] == board[7] and board[7] == board[8]

# def left_column_is_winner(board):
#     return board[0] == board[3] and board[3] == board[6]

# def middle_column_is_winner(board):
#     return board[1] == board[4] and board[4] == board[7]

# def right_column_is_winner(board):
#     return board[2] == board[5] and board[5] == board[8]

# def left_diagonal_is_winner(board):
#     return board[0] == board[4] and board[4] == board[8]

# def right_diagonal_is_winner(board):
#     return board[2] == board[4] and board[4] == board[6]


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 1):
        game_over(board, board[0])
    elif is_row_winner(board, 2):
        game_over(board, board[3])
    elif is_row_winner(board, 3):
        game_over(board, board[6])
    elif is_column_winner(board, 1):
        game_over(board, board[0])
    elif is_column_winner(board, 2):
        game_over(board, board[1])
    elif is_column_winner(board, 3):
        game_over(board, board[2])
    elif is_diag_winner(board, "left"):
        game_over(board, board[0])
    elif is_diag_winner(board, "right"):
        game_over(board, board[0])


    # if top_row_is_winner(board):
    #     game_over(board, board[0])
    # elif middle_row_is_winner(board):
    #     game_over(board, board[3])
    # elif bottom_row_is_winner(board):
    #     game_over(board, board[6])
    # elif left_column_is_winner(board):
    #     game_over(board, board[0])
    # elif middle_column_is_winner(board):
    #     game_over(board, board[1])
    # elif right_column_is_winner(board):
    #     game_over(board, board[2])
    # elif left_diagonal_is_winner(board):
    #     game_over(board, board[0])
    # elif right_diagonal_is_winner(board):
    #     game_over(board, board[0])

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
