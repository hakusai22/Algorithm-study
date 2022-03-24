package leetcode每日一题._03_23;

class Solution {
    public int findKthNumber(int n, int k) {
        int cur = 1;
        k--;
        while(k > 0) {
            long cnts = dfs(cur, cur, n);
            if(cnts <= k) {
                k -= cnts;
                cur++;
            } else {
                k--;
                cur *= 10;
            }
        }
        return cur;
    }

    private long dfs(long l, long r, int n) {
        if(l > n)
            return 0;
        return Math.min(r, n) - l + 1 + dfs(l * 10, r * 10 + 9, n);
    }
}
