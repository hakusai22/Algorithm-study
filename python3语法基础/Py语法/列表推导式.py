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
INFMIN = float('-inf')
INFMAX = float('inf')
'''
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
'''

if __name__ == '__main__':
    # in后面跟其他可迭代对象,如字符串
    list_c = [7 * c for c in "python"]
    print(list_c)

    # 带if条件语句的列表推导式
    list_d = [d for d in range(6) if d % 2 != 0]
    print(list_d)

    # 多个for循环
    list_e = [(i, j * j) for i in range(3) for j in range(5, 15, 5)]
    print(list_e)
    list_e1 = [[i, j * j] for i in range(3) for j in range(5, 15, 5)]
    print(list_e1)

    # 嵌套列表推导式,多个并列条件
    list_g = [[i for i in range(j - 3, j)] for j in range(22) if j % 3 == 0 and j != 0]
    print(list_g)
