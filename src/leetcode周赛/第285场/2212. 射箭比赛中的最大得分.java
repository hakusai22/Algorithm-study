package leetcode周赛.第285场;

class Solution {
    private int max, result[];

    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        maximumBobPoints(1, 0, new int[12], numArrows, aliceArrows);
        return result;
    }

    private void maximumBobPoints(int i, int points, int[] curr, int numArrows, int[] aliceArrows) {
        if (numArrows >= 0) {
            if (i < 12) {
                maximumBobPoints(i + 1, points, curr, numArrows, aliceArrows);
                maximumBobPoints(i + 1, points + i, curr, numArrows - (curr[i] = aliceArrows[i] + 1), aliceArrows);
                curr[i] = 0;
            } else if (points >= max) {
                max = points;
                curr[0] = numArrows;
                result = curr.clone();
            }
        }
    }
}