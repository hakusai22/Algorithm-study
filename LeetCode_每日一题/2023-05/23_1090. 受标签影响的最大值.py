'''
Author: hakusai
Date: 2023-05-23 13:25:37
LastEditTime: 2023-05-23 13:35:25
Description:
'''
'''
Author: hakusai
Date: 2023-05-23 13:25:37
LastEditTime: 2023-05-23 13:31:59
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
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        ans = num = 0
        cnt = Counter()
        print(zip(values, labels))
        arr = sorted(zip(values, labels), key=lambda x: x[1], reverse=True)
        print(arr)
        for v, i in arr:
            if cnt[i] < useLimit:
                cnt[i] += 1
                num += 1
                ans += v
                if num == numWanted:
                    break
        return ans


if __name__ == "__main__":
    print(Solution.largestValsFromLabels(self=None, values=[5, 4, 3, 2, 1], labels=[
        1, 1, 2, 2, 3], numWanted=3, useLimit=1))
