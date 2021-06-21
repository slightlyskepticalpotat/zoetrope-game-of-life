import copy
import sys

rows = int(input("Rows: "))
columns = int(input("Columns: "))
iterations = int(input("Iterations: "))
empty_board = [[0 for i in range(columns)] for j in range(rows)]
board = copy.deepcopy(empty_board)
sys.stdout.write("Space-separated starting cells (bottom left is 0 0), \"-1 -1\" to continue: \n")
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    board[rows - x - 1][y] = 1

for i in range(iterations):
    new = copy.deepcopy(empty_board)
    for r in range(rows):
        for c in range(columns):
            neighbours = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= r + dx <= rows - 1 and 0 <= c + dy <= columns - 1 and board[r + dx][c + dy] and abs(dx) + abs(dy) > 0:
                        neighbours += 1
            if board[r][c] == 0: # dead cell
                if neighbours == 3:
                    new[r][c] = 1
            else: # live cell
                if neighbours == 2 or neighbours == 3:
                    new[r][c] = 1
    board = new
    sys.stdout.write(f"Iteration {i + 1}\n")
    sys.stdout.write("_" * (columns + 2) + "\n")
    sys.stdout.write("\n".join("|" + "".join(["*" if char else " " for char in line]) + "|" for line in board) + "\n")
    sys.stdout.write("_" * (columns + 2) + "\n")
