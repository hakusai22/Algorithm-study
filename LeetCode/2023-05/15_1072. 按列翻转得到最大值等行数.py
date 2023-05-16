'''
Author: hakusai
Date: 2023-05-15 08:30:08
LastEditTime: 2023-05-15 08:38:12
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
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            if row[0]:
                for j in range(len(row)):
                    row[j] ^= 1
                cnt[tuple(row)] += 1
        return max(cnt.values())
