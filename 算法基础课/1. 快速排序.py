from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache

'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
'''

'''
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/7 11:10


def qucick_sort(data, l, r):
    if l >= r:
        return
    i = l - 1
    j = r + 1
    x = data[l + r >> 1]
    while i < j:
        while 1:
            i += 1
            if data[i] >= x:
                break
        while 1:
            j -= 1
            if data[j] <= x:
                break
        if i < j:
            data[i], data[j] = data[j], data[i]
    qucick_sort(data, l, j)
    qucick_sort(data, j + 1, r)


if __name__ == '__main__':
    n = int(input())
    data = [int(x) for x in input().split()]
    qucick_sort(data, 0, n - 1)
    print(" ".join(map(str, data)))
