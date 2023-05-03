'''
Author: hakusai
Date: 2023-04-27 16:13:57
LastEditTime: 2023-04-27 16:32:44
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
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = defaultdict(int)
        ans = 0
        for s in words:
            x = 1
            for i in range(len(s)):
                t = s[:i]+s[i+1:]
                x = max(x, d[t]+1)
            d[s] = x
            ans = max(ans, x)
        return ans
