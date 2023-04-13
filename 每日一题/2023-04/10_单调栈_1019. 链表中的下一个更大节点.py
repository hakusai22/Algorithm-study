from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys

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
# @Time    : 2023/04/11 01:56

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur = [0, 0]
        d = 0
        n = len(instructions)
        for i in range(n * 4):
            match instructions[i % n]:
                case 'R':
                    d = (d + 1) % 4
                case 'L':
                    d = (d - 1) % 4
                case 'G':
                    match d:
                        case 0:
                            cur[1] += 1
                        case 1:
                            cur[0] += 1
                        case 2:
                            cur[1] -= 1
                        case 3:
                            cur[0] -= 1
            if cur == [0, 0] and i % n == n - 1:
                return True
        return False
