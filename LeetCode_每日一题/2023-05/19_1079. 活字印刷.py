'''
Author: hakusai
Date: 2023-05-19 00:48:13
LastEditTime: 2023-05-19 00:48:24
Description: 
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
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        n = len(tiles)
        s = set()

        def dfs(i, t):
            if i == n:
                return
            for k, v in cnt.items():
                if v > 0:
                    nt = t + k
                    s.add(nt)
                    cnt[k] -= 1
                    dfs(i+1, nt)
                    cnt[k] += 1
        dfs(0, "")
        return len(s)
