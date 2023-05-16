'''
Author: hakusai
Date: 2023-04-26 09:20:43
LastEditTime: 2023-04-26 09:32:00
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
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0

        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans
            maxSumA = 0
            for i in range(firstLen+secondLen, len(s)):
                maxSumA = max(maxSumA, s[i-secondLen]-s[i-secondLen-firstLen])
                ans = max(ans, maxSumA+s[i]-s[i-secondLen])
        f(firstLen, secondLen)  # 左a右b
        f(secondLen, firstLen)  # 左b右a
        return ans
