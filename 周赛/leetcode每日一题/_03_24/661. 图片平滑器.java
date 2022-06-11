package leetcode每日一题._03_24;

class Solution {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length, n = img[0].length;
        int[][] presum = new int[m + 1][n + 1], ans = new int[m][n];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                presum[i + 1][j + 1] = presum[i][j + 1] + presum[i + 1][j] - presum[i][j] + img[i][j];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++) {
                int cnts = 0, downI = Math.max(0, i - 1), upI = Math.min(m, i + 2), downJ = Math.max(0, j - 1), upJ = Math.min(n, j + 2);
                for(int di = downI; di < upI; di++)
                    for(int dj = downJ; dj < upJ; dj++)
                        cnts++;
                ans[i][j] = (presum[upI][upJ] - presum[upI][downJ] - presum[downI][upJ] + presum[downI][downJ]) / cnts;
            }
        return ans;
    }
}



