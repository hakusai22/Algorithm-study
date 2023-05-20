/*
 * @Author: hakusai
 * @Date: 2023-05-14 12:34:09
 * @LastEditTime: 2023-05-14 12:34:19
 */

import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    int[][] dirs = new int[][] {
            { -1, 1 }, { 1, 1 }, { 0, 1 }
    };
    public int maxMoves(int[][] grid) {
        int h = grid.length, w = grid[0].length;
        boolean[][] used = new boolean[h][w];
        Deque<int[]> deq = new LinkedList<>();
        for (int i = 0; i < h; i++) {
            deq.offer(new int[] { i, 0 });
            used[i][0] = true;
        }
        int ans = 0;
        while (!deq.isEmpty()) {
            int[] cur = deq.poll();
            int y = cur[0], x = cur[1];
            ans = Math.max(ans, x);
            for (int i = 0; i < dirs.length; i++) {
                int ny = y + dirs[i][0];
                int nx = x + dirs[i][1];
                if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                    if (grid[ny][nx] <= grid[y][x])
                        continue;
                    if (!used[ny][nx]) {
                        used[ny][nx] = true;
                        deq.offer(new int[] { ny, nx });
                    }
                }
            }
        }
        return ans;
    }
}