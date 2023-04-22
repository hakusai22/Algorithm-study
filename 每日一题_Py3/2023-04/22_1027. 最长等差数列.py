'''
Author: hakusai
Date: 2023-04-22 16:44:21
LastEditTime: 2023-04-22 17:12:50
'''


from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[1] * 1001 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for k in range(i):
                j = nums[i]-nums[k]+500
                f[i][j] = max(f[i][j], f[k][j]+1)
                ans = max(ans, f[i][j])
        return ans
