'''
Author: hakusai
Date: 2023-05-16 21:53:16
LastEditTime: 2023-05-17 00:59:41
Description: 
'''
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


# https://leetcode.cn/problems/determine-if-two-events-have-conflict/

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # 第一个事件的开始时间不晚于第二个事件的结束时间
        # 第二个事件的开始时间不晚于第一个事件的结束时间
        return event1[0] <= event2[1] and event2[0] <= event1[1]
