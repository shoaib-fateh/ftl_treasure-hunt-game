import random

rows = int(input("Enter the number of rows for the game board: "))
cols = int(input("Enter the number of columns for the game board: "))

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
        guess_row = int(input(f"Choose a row to hide the treasure (0 to {rows - 1}): "))
        guess_col = int(input(f"Choose a column to hide the treasure {cols - 1}): "))

        if guess_row == treasure_row and guess_col == treasure_col:
            print("Great, You win!!")
            break
        else:
            print("Wrong Hit, Try again!")
    except ValueError:
        print("Please enter valid numbers.")
