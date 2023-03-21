class Solution {

  public int longestSubsequence(String s, int k) {
    int n = s.length();
    int[] left = new int[n];
    int ans = 0;
    char[] cs = s.toCharArray();
    for (int i = 0, cnt = 0; i < n - 1; i++) {
      if (cs[i] == '0') cnt++;
      left[i + 1] = cnt;
    }
    int l = 0, r = 0, cur = 0;
    while (r < n) {
      cur = (cur << 1) + cs[r] - '0';
      if (cur <= k) {
        ans = Math.max(ans, r - l + 1 + left[l]);
      }
      while (cur > k) {
        if (cs[l] == '1') cur -= 1 << (r - l);
        l++;
      }
      r++;
      ans = Math.max(ans, r - l);
    }
    return ans;
  }
}