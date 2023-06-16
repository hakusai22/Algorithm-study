'''
Author: hakusai
Date: 2023-06-15 20:46:05
LastEditTime: 2023-06-15 23:00:43
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
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 计算s前i个字符中,字符j出现了多少次
        # 题目是某个区间中 字符出现的次数 如果是偶数不用考虑（可以重新排列）奇数的话就是我们需要替换的数 /2 就是结果了

        dp = [[0]*26 for _ in range(len(s)+1)]
        for i, c in enumerate(s, 1):
            #切片浅拷贝
            dp[i] = dp[i-1][:]
            dp[i][ord(c)-ord("a")] += 1
        ans = []
        print(dp)
        for l, r, k in queries:
            cnt = sum((dp[r+1][j]-dp[l][j]) & 1 for j in range(26))
            ans.append(cnt//2 <= k)
        return ans
