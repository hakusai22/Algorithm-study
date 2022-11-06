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


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/6 13:57

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        ct = Counter(nums[:k])
        st = sum(nums[:k])
        if len(ct) == k:
            res = st
        for i in range(k, len(nums)):
            st += nums[i] - nums[i - k]
            ct[nums[i]] += 1
            ct[nums[i - k]] -= 1
            if ct[nums[i - k]] == 0:
                ct.pop(nums[i - k])
            if len(ct) == k:
                res = max(res, st)
        return res
        s = ""
        s.endswith()
