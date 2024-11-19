import random


rows = int(input("Rows: "))
cols = int(input("Cols: "))

board = []

for r in range(rows):
    row = []

    for c in range(cols):
        row.append("*")
    
    board.append(row)


treasure_row = random.randint(0, rows - 1)
treasure_col = random.randint(0, cols - 1)

board[treasure_row][treasure_col] = "T"

for row in board:
    print(" ".join(row))

