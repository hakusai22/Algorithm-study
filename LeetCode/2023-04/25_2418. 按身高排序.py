'''
Author: hakusai
Date: 2023-04-25 14:33:59
LastEditTime: 2023-04-25 14:38:16
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
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indics = list(range(len(names)))
        indics.sort(key=lambda x: heights[x], reverse=True)
        res = []
        for i in indics:
            res.append(names[i])
        return res
