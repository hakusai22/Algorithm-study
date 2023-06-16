'''
Author: hakusai
Date: 2023-06-13 16:25:12
LastEditTime: 2023-06-13 16:31:50
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
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = b = 0
        for i in cnt.values():
            a = len(nums)-b-i
            ans += a*b*i
            b += i
        return ans


if __name__ == "__main__":
    Solution.unequalTriplets(self=None, nums=[4, 4, 2, 4, 3])
