# Don't Panic.

import sys

def peers(x, y):
    neighbours = 0
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1 and board[x + 1][y] == 1:
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1 and board[x - 1][y] == 1:
        neighbours += 1
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x][y + 1] == 1:
        neighbours += 1
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x][y - 1] == 1:
        neighbours += 1
    if 0 <= x + 1 <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x + 1][y + 1] == 1:
        neighbours += 1
    if 0 <= x + 1 <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x + 1][y - 1] == 1:
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x - 1][y + 1] == 1:
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x - 1][y - 1] == 1:
        neighbours += 1
    return neighbours

rows, columns = int(input("Rows: ")), int(input("Columns: "))
board = [[0] * columns for _ in range(rows)]
iterations = int(input("Iterations: "))
print("Enter each live cell at the beginning with the row and column number separated by a space (bottom left is 0, 0). Enter \"-1 -1\" to move on:")
while True:
    x, y = map(int, input().split())
    if x + y == -2:
        break
    board[rows - x - 1][y] = 1

for i in range(iterations):
    new = [[0] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            neighbours = peers(r, c)
            if board[r][c] == 0: # dead cell
                if neighbours == 3: # new cell
                    new[r][c] = 1 
            else: # live cell
                if neighbours == 2 or neighbours == 3: # surviving cell
                    new[r][c] = 1
    board = new
    sys.stdout.write(f"Iteration {i + 1}\n")
    sys.stdout.write("_" * (columns + 2) + "\n")
    sys.stdout.write("\n".join("|" + "".join(["*" if char else " " for char in line]) + "|" for line in board) + "\n")
    sys.stdout.write("‾" * (columns + 2) + "\n")
