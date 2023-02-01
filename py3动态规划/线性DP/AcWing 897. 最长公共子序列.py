from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
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
# @Time    : 2023/02/01 11:53

"""
    集合：所有在A[1…i]中出现过且在B[1…j]中也出现过的子序列
    属性：Max
"""

if __name__ == '__main__':
    N = 1010
    f = [[0] * N for _ in range(N)]

    n, m = map(int, input().split())
    a = " " + input()
    b = " " + input()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
            if a[i] == b[j]:
                f[i][j] = f[i - 1][j - 1] + 1

    print(f[n][m])
