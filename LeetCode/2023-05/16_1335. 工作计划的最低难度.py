'''
Author: hakusai
Date: 2023-05-16 08:59:13
LastEditTime: 2023-05-16 09:56:04
'''
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        lru_cache(maxsize=None)
        def dfs(i, j):
            if i == 0:
                return max(jobDifficulty[:j+1])
            res, mx = inf, 0
            for k in range(j, i-1, -1):
                mx = max(mx, jobDifficulty[k])
                res = min(res, dfs(i-1, k-1)+mx)
            return res
        return dfs(d-1, n-1)
