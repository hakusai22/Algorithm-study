'''
Author: hakusai
Date: 2023-04-22 17:33:12
LastEditTime: 2023-04-22 17:35:58
'''
from cmath import inf
from typing import List


class Solution:
    def supplyWagon(self, a: List[int]) -> List[int]:
        n = len(a)
        for _ in range((n + 1) // 2):
            mx = inf
            k = -1
            for i in range(len(a) - 1):
                if a[i] + a[i + 1] < mx:
                    mx = a[i] + a[i + 1]
                    k = i
            a = a[:k] + [a[k] + a[k + 1]] + a[k + 2:]
        return a
