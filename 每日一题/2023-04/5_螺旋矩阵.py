from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys
from typing import List

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

def input():
    return sys.stdin.readline().rstrip()

def end(r=-1):
    print(r)
    exit()

# -*- coding: utf-8 -*-
# @Author  : wink
# @Time    : 2023/04/05 10:57

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # 顺时针
    # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 逆时针
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = 0
    m, n = len(matrix), len(matrix[0])
    x, y = -1, 0
    ans = list()
    for i in range(m * n):
        nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
        if not 0 <= nx < m or not 0 <= ny < n or matrix[nx][ny] == INF:
            dir_idx = (dir_idx + 1) % len(directions)
            nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
        ans.append(matrix[nx][ny])
        matrix[nx][ny] = INF
        x, y = nx, ny
    return ans

if __name__ == '__main__':
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
