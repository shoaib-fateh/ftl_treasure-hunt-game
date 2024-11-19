import random
from colorama import Fore, Style, init

init()

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


print("\n" + Fore.GREEN + Style.BRIGHT + "Game Board:" + Style.RESET_ALL)


for row in board:
    print(" ".join(row))
print("\n" + "-" * 20 + "\n")


while True:
    try:

        guess_row = int(input(f"{Fore.YELLOW}Choose a row to hide the treasure (0 to {rows - 1}): {Style.RESET_ALL}"))
        guess_col = int(input(f"{Fore.YELLOW}Choose a column to hide the treasure (0 to {cols - 1}): {Style.RESET_ALL}"))

        if guess_row > rows or guess_col > cols: 
            print(Fore.RED + "Outsite of the board, Try again!")

        elif guess_row == treasure_row and guess_col == treasure_col:
            print(Fore.CYAN + "Great, You win!!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Wrong Hit, Try again!" + Style.RESET_ALL)


    except ValueError:
        print(Fore.MAGENTA + "Please enter valid numbers." + Style.RESET_ALL)
