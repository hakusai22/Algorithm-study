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
# @Time    : 2023/02/01 17:30

if __name__ == '__main__':
    N = 15
    M = 1010
    f = [[0] * N for _ in range(N)]
    a = [[0] * N for _ in range(M)]

    def distance(a, b):
        la = len(a) - 1
        lb = len(b) - 1

        for i in range(1, lb + 1):
            f[0][i] = i
        for i in range(1, la + 1):
            f[i][0] = i

        for i in range(1, la + 1):
            for j in range(1, lb + 1):
                f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
                if a[i] == b[j]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
        return f[la][lb]

    n, m = map(int, input().split())
    for i in range(n):
        a[i] = " " + input()

    while m:
        m -= 1
        li = input().split()
        b = " " + li[0]
        lmt = int(li[1])
        res = 0
        for i in range(n):
            if distance(a[i], b) <= lmt:
                res += 1
        print(res)
