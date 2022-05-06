import os
# tic tac toe

"""
tic-tac-toe board
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

Algorithm
    user_input = 1-9
    don't accept anything else
    check if user_input is already taken
    add to board
    check if user won = check rows, cols, diagonals
    toggle between players upon successful moves

"""

# creating an 2 dimentional array/list for board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = True  # True = Player 1; False = Player 2
turns = 0

# Other func
clearConsole = lambda: print("\n" * 100)

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}\t", end="")
        print()

def quit_game(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing...!")
        return True
    else:
        return False

def check_input(user_input):
    # Check if number
    if not is_num(user_input): return False
    user_input = int(user_input)
    # Check of 1-9
    if not bounds(user_input): return False

    return True

def is_num(user_input):
    if not user_input.isnumeric():
        print('This is not a valid number!')
        return False
    else:
        return True

def bounds(user_input):
    if user_input >= 1 and user_input <= 9:
        return True
    else:
        print('This number is out of bounds!')
        return False

def is_taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print('Position already taken!')
        return True
    else:
        return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)
    # print(f"row = {row}\ncol = {col}")
    return (row, col)

def add_to_board(coords, board, active_player):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_player

def current_player(player):
    if player:
        return "x"
    else:
        return "o"

def is_win(player, board):
    # Checking rows
    if check_row(player, board): return True
    if check_col(player, board): return True
    if check_diag(player, board): return True
    return False

def check_row(player, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != player:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(player, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != player:
                complete_col = False
                break
        if complete_col:
            return True
    return False

def check_diag(player, board):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player: return True
    else: return False

while turns < 9:
    active_player = current_player(player)
    print_board(board)
    user_input = input(f"Player {active_player.upper()} (1 thru 9 | \"q\" to quit) : ")
    if quit_game(user_input): break
    if not check_input(user_input):
        print('Please try again...')
        continue
    # Converting user_input to index position terminology
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if is_taken(coords, board):
        print('Please try again')
        continue
    add_to_board(coords, board, active_player)
    if is_win(active_player, board):
        print(f"{active_player.upper()} won!")
        break

    turns += 1
    if turns == 9: print("Tie!")

    player = not player
    clearConsole()

