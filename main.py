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


while True:
    try:
        treasure_row = int(input(f"Enter the row: (0 to {rows -1}) for treasure: "))
        treasure_col = int(input(f"Enter the col: (0 to {cols -1}) for treasure: "))

        if 0 <= treasure_row < rows and 0 <= treasure_col < cols:
            print("Greate, You win!!")
            break
        else:
            print("Wrong Hit, Try again!")

    except ValueError:
        print("Enter valid numbers.")
