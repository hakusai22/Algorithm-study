import bisect
import math
import collections
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from sortedcontainers import SortedList
from itertools import permutations, combinations
from queue import PriorityQueue
from itertools import chain
from functools import lru_cache

'''
1.heapify(list):将序列list改变成heap结构
2.heappush(heap, item):向序列heap中插入一个item元素
3.heappop(heap):pop出heap堆中的最小值
4.heapreplace(heap, item):先pop出最小值，再向heap中添加item元素
5.heappushpop(heap, item): 与heapreplace方向相反
6.nlargest(n, iterable, key=None):返回heap的前n个最大的元素的list
7.nsmallest(n, iterable, key=None):返回heap的前n个最小的元素的list
'''


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/6 14:04

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapify(pre)
            suf = costs[-candidates:]
            heapify(suf)
            i, j = candidates, n - 1 - candidates
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return ans + sum(costs[:k])
