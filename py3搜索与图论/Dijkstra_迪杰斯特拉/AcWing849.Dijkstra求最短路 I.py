from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

MOD = int(1e9 + 7)
INF = int(1e20)
'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''

def I():
    return input()

def II():
    return int(input())

def FI():
    return float(input())

def MII():
    return map(int, input().split())

def MFI():
    return map(float, input().split())

def LI():
    return list(input().split())

def LMII():
    return list(map(int, input().split()))

def LMFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/11/28 22:32
if __name__ == '__main__':
    N = 510
    # 因为题目的边远大于点，因此是稠密图，稠密图用邻接矩阵去存。
    d = [[0x3f3f3f3f] * N for _ in range(N)]
    # dist为每个点到起点的距离
    dist = [0x3f3f3f3f] * N
    # st表示每个点的最短距离已经确定了
    st = [False] * N

    def dijkstra():
        dist[1] = 0
        # 迭代 n - 1 次，因为每迭代一次，一个点的最短距离就确定了，并把它加入到确定的集合当中。
        # 前 n - 1 个点已经确定，那么最后一个点自然也就是最短距离了，所以可以把 n 改成 n - 1
        for i in range(n - 1):
            # 随便定义一个点，主要是为了后面比较，然后找到最小距离的点
            t = -1
            # 循环每个点，找到最短距离的点，并把它赋值给 t
            for j in range(1, n + 1):
                if not st[j] and dist[j] < dist[t]:
                    t = j
            # 标记该点距离确定
            st[t] = True
            # 根据该点更新其他所有点的距离
            for j in range(1, n + 1):
                dist[j] = min(dist[j], dist[t] + d[t][j])

            # 如果取到了最后一个点，则最后一个点的最短距离被找到，结束循环。
            if t == n:
                break

        if dist[n] == 0x3f3f3f3f:
            return -1
        return dist[n]

    n, m = map(int, input().split())
    while m:
        a, b, c = map(int, input().split())
        d[a][b] = min(d[a][b], c)
        m -= 1
    print(dijkstra())
