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
# @Time    : 2023/01/31 15:29

if __name__ == '__main__':
    N = 110
    v = [0] * N
    w = [0] * N
    s = [0] * N
    f = [[0] * N for _ in range(N)]
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        v[i], w[i], s[i] = map(int, input().split())

    for i in range(1, n + 1):
        for j in range(m + 1):
            k = 0
            f[i][j] = f[i - 1][j]
            while 1:
                if k <= s[i] and k * v[i] <= j:
                    f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i])
                    k += 1
                else:
                    break
    print(f[n][m])
