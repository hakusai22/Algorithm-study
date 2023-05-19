'''
Author: hakusai
Date: 2023-05-18 09:42:51
LastEditTime: 2023-05-18 09:47:42
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


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = len(arr1)-1
        j = len(arr2)-1
        res = []
        c = 0
        while i >= 0 or j >= 0 or c != 0:
            if i >= 0:
                c += arr1[i]
                i -= 1
            if j >= 0:
                c += arr2[j]
                j -= 1
            res.append(c & 1)
            c = -(c >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        res.reverse()
        return res


if __name__ == "__main__":
    print(Solution.addNegabinary(self=None, arr1=[1, 1, 1, 1, 1], arr2=[1, 0, 1]))
