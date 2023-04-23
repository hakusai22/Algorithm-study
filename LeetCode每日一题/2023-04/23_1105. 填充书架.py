'''
Author: hakusai
Date: 2023-04-22 21:49:02
LastEditTime: 2023-04-23 21:57:14
'''

import random
import sys
import os
import math
import gc
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0]*(n+1)
        for i, (w, h) in enumerate(books, 1):
            f[i] = f[i-1]+h
            for j in range(i-1, 0, -1):
                w += books[j-1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j-1][1])
                f[i] = min(f[i], f[j-1]+h)
        return f[n]


if __name__ == "__main__":
    print(111)
