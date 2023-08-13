'''
Author: hakusai
Date: 2023-08-13 12:03:37
LastEditTime: 2023-08-13 12:19:16
Description: https://github.com/hakusai22
'''
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List, Optional
from sortedcontainers import SortedList

def minAbsoluteDifference(nums: List[int], x: int) -> int:
    stl = SortedList()
    n = len(nums)
    ans = inf
    for i in range(n):
        if i >= x:
            stl.add(nums[i-x])
            pos = stl.bisect_left(nums[i])
            # 查看二分位置的两边
            for j in range(pos-1, pos+1):
                if 0 <= j < len(stl):
                    ans = min(ans, abs(nums[i] - stl[j]))
    return ans


if __name__ == "__main__":
    print(minAbsoluteDifference(nums = [4,3,2,4], x = 2))

