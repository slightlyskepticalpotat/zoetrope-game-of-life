#include <bits/stdc++.h>

using namespace std;

int rows, cols, n, x, y, near;

int main()
{
    printf("Rows, cols, gens: ");
    scanf("%d %d %d", &rows, &cols, &n);
    vector<vector<int>> old {rows, vector<int>(cols, 0)}, cur, next;
    cur = next = old;
    printf("Starting cells: ");
    while (scanf("%d %d", &x, &y) != EOF) {
        cur[x][y] = 1;
        printf("Starting cells: ");
    }

    for (int i = 0; i < n + 1; i++) {
        cur, next = next, old;
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
                        if (0 <= r + dx && r + dx <= rows - 1 && 0 <= c + dy && c + dy <= cols - 1) {
                            near += (cur[r + dx][c + dy]) && ((dx, dy) != (0, 0));
                        }
                    }
                }
                if (!cur[r][c]) {
                    next[r][c] = (near == 3);
                } else {
                    next[r][c] = (near == 2) || (near == 3);
                }
            }
        }
    }
    return 0;
}