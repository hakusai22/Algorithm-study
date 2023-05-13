'''
Author: hakusai
Date: 2023-05-05 17:10:48
LastEditTime: 2023-05-11 22:34:23
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
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            print(bin(i)[2:])
            print(bin(i))
            if not bin(i)[2:] in s:
                return False
        return True


