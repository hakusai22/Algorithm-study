'''
Author: hakusai
Date: 2023-06-09 10:45:13
LastEditTime: 2023-06-09 10:51:38
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
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        return len({nums[i]+nums[-i-1] for i in range(len(nums)//2)})
