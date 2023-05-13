'''
Author: hakusai
Date: 2023-05-13 10:37:57
LastEditTime: 2023-05-13 10:41:13
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
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        return max((x for x in s if -x in s), default=-1)
