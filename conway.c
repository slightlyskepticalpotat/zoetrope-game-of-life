#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int rows, cols, n, x, y, near;

int main()
{
    printf("Rows, cols, gens: ");
    scanf("%d %d %d", &rows, &cols, &n);
    int old[rows][cols], cur[rows][cols], next[rows][cols];
    memset(old, 0, rows * cols * sizeof(int));
    memcpy(cur, old, sizeof(cur));
    memcpy(next, old, sizeof(next));
    printf("Starting cells: ");
    while (scanf("%d %d", &x, &y) != EOF) {
        cur[x][y] = 1;
        printf("Starting cells: ");
    }
    printf("\n");
    for (int i = 0; i < n + 1; i++) {
        memcpy(next, old, sizeof(next));
        printf("Generation %d\n", i);
        for (int j = 0; j < rows; j++) {
            for (int k = 0; k < cols; k++) {
                if (cur[j][k]) {
                    printf("*");
                } else {
                    printf(" ");
                }
            }
            printf("\n");
        }
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                near = 0;
                for (int dx = -1; dx < 2; dx++) {
                    for (int dy = -1; dy < 2; dy++) {
                        if (0 <= r + dx && r + dx <= rows - 1 && 0 <= c + dy && c + dy <= cols - 1 && cur[r + dx][c + dy] && abs(dx) + abs(dy) != 0) {
                            near++;
                        }
                    }
                }
                next[r][c] += (cur[r][c] == 0 && near == 3);
                next[r][c] += (cur[r][c] == 1 && (near == 2 || near == 3));
            }
        }
        memcpy(cur, next, sizeof(cur));
    }
    return 0;
}