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
# @Time    : 2023/01/31 17:36

"""
    有 N 组物品和一个容量是 V 的背包。
    每组物品有若干个，同一组内的物品最多只能选一个。
    每件物品的体积是 vij，价值是 wij，其中 i 是组号，j是组内编号。
    求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。
    输出最大价值。
"""

N = 110
v = [[0] * N for _ in range(N)]
w = [[0] * N for _ in range(N)]
s = [[0] * N for _ in range(N)]
f = [0] * N

n, m = map(int, input().split())

for i in range(0, n):
    s[i] = int(input())
    for j in range(0, s[i]):
        v[i][j], w[i][j] = map(int, input().split())

for i in range(0, n):
    for j in range(m, -1, -1):
        for k in range(0, s[i]):
            if v[i][k] <= j:
                f[j] = max(f[j], f[j - v[i][k]] + w[i][k])

print(f[m])
