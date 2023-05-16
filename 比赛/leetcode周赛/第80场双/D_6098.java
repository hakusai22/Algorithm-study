package 比赛.LeetCode周赛.第80场双;
class D_6098 {
  public long countSubarrays(int[] nums, long k) {
    int n = nums.length;
    int r = 0;
    long sum = 0L;
    long ans = 0;
    for (int i = 0; i < n; ++i) {
      while (r < n && sum * (r - i) < k) sum += nums[r++];
      if (sum * (r - i) < k) {
        ans += r - i;
      } else {
        ans += r - i - 1;
      }
      sum -= nums[i];
    }
    return ans;
  }
}