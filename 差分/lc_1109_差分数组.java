class Solution {
    public int[] corpFlightBookings(int[][] bs, int n) {
        int[] c = new int[n + 1];
        for (int[] bo : bs) {
            int l = bo[0] - 1, r = bo[1] - 1, v = bo[2];
            c[l] += v;
            c[r + 1] -= v;
        }
        int[] ans = new int[n];
        ans[0] = c[0];
        for (int i = 1; i < n; i++) {
            ans[i] = ans[i - 1] + c[i];
        }
        return ans;
    }
}

