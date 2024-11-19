


row = 10
col = 10

board = []

for r in range(row):
    row = []

    for c in range(col):
        row.append("*")
    
    board.append(row)


treasure_row = 5
treasure_col = 5

board[treasure_row][treasure_col] = "T"

for row in board:
    print(" ".join(row))

