import java.util.Scanner;
import java.util.Arrays;

fun main() {
    val scan = Scanner(System.`in`);
    print("Rows, cols, gens: ");
    val (rows, cols, n) = arrayOf(scan.nextInt(), scan.nextInt(), scan.nextInt());
    val old = Array(rows) {IntArray(cols)}
    var cur = old.copy();
    print("Starting cells: ");
    while (scan.hasNext()) {
        val (x, y) = arrayOf(scan.nextInt(), scan.nextInt());
        cur[x][y] = 1;
        print("Starting cells: ");
    }
    println();
    for (i in 0..n) {
        var next = old.copy(); // hack to copy 2d array
        println("Generation " + i);
        for (j in 0..rows-1) {
            for (k in 0..cols-1) {
                if (cur[j][k] == 1) {
                    print("*");
                } else {
                    print(" ");
                }
            }
            print("\n");
        }
        for (r in 0..rows-1) {
            for (c in 0..cols-1) {
                var near = 0;
                for (dx in -1..1) {
                    for (dy in -1..1) {
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
        cur = next.copy();
    }
}

fun Array<IntArray>.copy() = Array(size) {get(it).clone()}