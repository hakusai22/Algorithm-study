'''
Author: hakusai
Date: 2023-04-12 19:36:36
LastEditTime: 2023-04-18 00:25:31
FilePath: /Algorithm-study/每日一题_Py3/2023-04/12_1147. 段式回文.py
'''
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
# @Time    : 2023/04/12 19:36

"""
你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
subtexti 是 非空 字符串
所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
返回k可能最大值。

"""

class Solution:
    def longestDecomposition(self, s: str) -> int:
        if s == "":
            return 0
        for i in range(1, len(s) // 2 + 1):
            if s[:i] == s[-i:]:
                return 2 + self.longestDecomposition(s[i:-i])
        return 1
