'''
Author: hakusai
Date: 2023-06-01 22:43:33
LastEditTime: 2023-06-01 22:55:23
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
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(x: int) -> bool:
            cnt, pre = 1, price[0]
            for cur in price:
                if cur >= x+pre:
                    pre = cur
                    cnt += 1
            return cnt >= k

        price.sort()
        l, r = 0, price[-1]-price[0]
        while l < r:
            mid = (l+r+1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid-1

        return l


if __name__ == "__main__":
    Solution.maximumTastiness(self=None, price=[13, 5, 1, 8, 21, 2], k=3)
