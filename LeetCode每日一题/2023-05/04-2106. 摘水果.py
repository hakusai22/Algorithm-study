'''
Author: hakusai
Date: 2023-05-04 18:58:30
LastEditTime: 2023-05-04 19:00:51
'''
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = i = s = 0
        for j, (pj, fj) in enumerate(fruits):
            s += fj
            while i <= j and pj - fruits[i][0] + min(abs(startPos - fruits[i][0]), abs(startPos - fruits[j][0])) > k:
                s -= fruits[i][1]
                i += 1
            ans = max(ans, s)
        return ans
