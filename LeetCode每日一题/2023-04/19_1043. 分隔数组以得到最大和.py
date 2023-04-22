'''
Author: hakusai
Date: 2023-04-19 22:12:59
LastEditTime: 2023-04-20 10:22:38
FilePath: /Algorithm-study/每日一题_Py3/2023-04/19_1043. 分隔数组以得到最大和.py
'''

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        f = [0] * (n+1)
        for i in range(1, n+1):
            mx = 0
            for j in range(i, max(0, i-k), -1):
                mx = max(mx, arr[j-1])
                f[i] = max(f[i], f[j-1]+mx*(i-j+1))
        return f[n]
