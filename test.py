player = "o"
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def do_diag(player, board):
    for i in range(3):
        row = i
        col = i
        board[row][col] = player
        print(f"i = {i}; row = {row}; col = {col}")
        print_board(board)

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}\t", end="")
        print()

do_diag(player, board)
# print_board(board)

