'''
Author: hakusai
Date: 2023-05-27 18:38:29
LastEditTime: 2023-05-27 18:55:44
Description: 
'''
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List, Optional


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        ans = [0]*5
        ans[0] = next((i for i in range(256) if count[i]), -1)
        ans[1] = next((i for i in range(255, -1, -1) if count[i]), 256)
        ans[2] = sum(i * count[i] for i in range(256))/sum(count)
        head, tail = 0, 255
        ans[4] = next((i for i in range(256) if count[i] == max(count)), -1)
        while head < tail:
            x = min(count[head], count[tail])
            count[head] -= x
            count[tail] -= x
            if count[head] == 0:
                head += 1
            if count[tail] == 0:
                tail -= 1
        ans[3] = ((head+tail)/2)
        return ans
