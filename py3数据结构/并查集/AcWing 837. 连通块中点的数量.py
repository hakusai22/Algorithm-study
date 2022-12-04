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

def IF():
    return float(input())

def MI():
    return map(int, input().split())

def MF():
    return map(float, input().split())

def LI():
    return list(input().split())

def LII():
    return list(map(int, input().split()))

def LFI():
    return list(map(float, input().split()))

def GMI():
    return map(lambda x: int(x) - 1, input().split())

def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/11/20 22:09

if __name__ == '__main__':
    N = 100010
    p = [0] * N
    size = [0] * N

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    n, m = map(int, input().split())

    for i in range(1, n + 1):
        p[i] = i
        size[i] = 1

    while m:
        m -= 1
        li = input().split()
        if li[0] == 'C':
            a, b = int(li[1]), int(li[2])
            if find(a) == find(b):
                continue
            size[find(b)] += size[find(a)]
            p[find(a)] = find(b)
        elif li[0] == 'Q1':
            a, b = int(li[1]), int(li[2])
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")
        else:
            a = int(li[1])
            print(size[find(a)])

# https://www.acwing.com/problem/content/839/