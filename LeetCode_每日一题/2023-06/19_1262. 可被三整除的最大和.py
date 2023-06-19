'''
Author: hakusai
Date: 2023-06-19 07:49:34
LastEditTime: 2023-06-19 08:07:14
Description: 
'''
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List, Optional


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for a in nums:
            for i in dp[:]:
                print(i)
                dp[(i+a) % 3] = max(dp[(i+a) % 3], i+a)
        return dp[0]
