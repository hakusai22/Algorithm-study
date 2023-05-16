'''
Author: hakusai
Date: 2023-05-14 01:16:48
LastEditTime: 2023-05-14 01:21:33
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
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        ans = [0]*n
        even, odd = 0, 1
        for x, cnt in sorted(((x, cnt) for x, cnt in Counter(barcodes).items()), key=lambda x: x[1], reverse=True):
            while cnt:
                cnt -= 1
                if even < n:
                    ans[even] = x
                    even += 2
                else:
                    ans[odd] = x
                    odd += 2
        return ans
