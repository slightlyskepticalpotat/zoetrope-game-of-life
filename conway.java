import java.util.Scanner;
import java.util.Arrays;

public class conway {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Rows, cols, gens: ");
        int rows = scan.nextInt(), cols = scan.nextInt(), n = scan.nextInt(), near = 0;
        int[][] old = new int[rows][cols];
        int[][] cur = Arrays.stream(old).map(int[]::clone).toArray(int[][]::new), next = Arrays.stream(old).map(int[]::clone).toArray(int[][]::new);
        System.out.print("Starting cells: ");
        while (scan.hasNext()) {
            int x = scan.nextInt(), y = scan.nextInt();
            cur[x][y] = 1;
            System.out.print("Starting cells: ");
        }
        System.out.println();
        for (int i = 0; i < n + 1; i++) {
            next = Arrays.stream(old).map(int[]::clone).toArray(int[][]::new); // hack to copy 2d array
            System.out.println("Generation " + i);
            for (int j = 0; j < rows; j++) {
                for (int k = 0; k < cols; k++) {
                    if (cur[j][k] == 1) {
                        System.out.print("*");
                    } else {
                        System.out.print(" ");
                    }
                }
                System.out.print("\n");
            }
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    near = 0;
                    for (int dx = -1; dx < 2; dx++) {
                        for (int dy = -1; dy < 2; dy++) {
                            if (0 <= r + dx && r + dx <= rows - 1 && 0 <= c + dy && c + dy <= cols - 1 && cur[r + dx][c + dy] == 1 && Math.abs(dx) + Math.abs(dy) != 0) {
                                near++;
                            }
                        }
                    }
                    if (cur[r][c] == 0 && near == 3) {
                        next[r][c]++;
                    } else if (cur[r][c] == 1 && (near == 2 || near == 3)) {
                        next[r][c]++;
                    }
                }
            }
            cur = next;
        }
    }
}