from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from string import ascii_lowercase
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/01 17:45

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        count = 0
        map = defaultdict()
        map[" "] = " "
        for s in key:
            if s not in map:
                map[s] = ascii_lowercase[count]
                count += 1
        res=""
        for i in range(len(message)):
            res+=map[message[i]]

        return res
