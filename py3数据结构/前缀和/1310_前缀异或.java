class Solution {
    public int[] xorQueries(int[] arr, int[][] qs) {
        int n = arr.length, m = qs.length;
        int[] sum = new int[n + 1];
        for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] ^ arr[i - 1];
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int l = qs[i][0] + 1, r = qs[i][1] + 1;
            ans[i] = sum[r] ^ sum[l - 1];
        }
        return ans;
    }
}