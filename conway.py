import copy, sys

rows, cols, n = map(int, input("Rows, cols, gens: ").split())
old = [[0 for i in range(cols)] for j in range(rows)]
cur = new = copy.deepcopy(old)
try:
    while raw := input("Starting cells: "): # 0 0 is top left
        x, y = map(int, raw.split())
        cur[x][y] = 1
except:
    print("")

for i in range(n + 1):
    cur, new = new, copy.deepcopy(old)
    sys.stdout.write("Generation " + str(i) + "\n" + ("\n".join("".join(["*" if i else " " for i in line]) for line in cur) + "\n"))
    for r in range(rows):
        for c in range(cols):
            near = 0 # alive nearby
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                        near += int(0 <= r + dx <= rows - 1 and 0 <= c + dy <= cols - 1 and cur[r + dx][c + dy] and (dx, dy) != (0, 0))
            if not cur[r][c]: # dead cell
                new[r][c] = int(near == 3)
            else: # live cell
                new[r][c] = int(near in (2, 3))