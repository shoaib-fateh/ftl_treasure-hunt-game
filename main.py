


row = 10
col = 10

board = []

for r in range(row):
    row = []

    for c in range(col):
        row.append("*")
    
    board.append(row)


for row in board:
    print(" ".join(row))

