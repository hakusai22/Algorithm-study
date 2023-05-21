'''
Author: hakusai
Date: 2023-05-21 10:35:58
LastEditTime: 2023-05-21 19:20:54
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
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        mx = max(vat)
        if mx == 0:
            return 0
        ans = inf
        # 蓄水的次数
        for x in range(1, mx + 1):
            # 升级次数累加，记为 y
            y = 0
            for v, b in zip(vat, bucket):
                # (v + x - 1) // x 向上取整
                temp = max(0, (v + x - 1) // x - b)
                y += temp
            ans = min(ans, x + y)
        return ans


if __name__ == "__main__":
    print(Solution.storeWater(self=None, bucket=[1, 3], vat=[6, 8]))
