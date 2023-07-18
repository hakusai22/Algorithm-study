'''
Author: hakusai
Date: 2023-07-18 08:13:25
LastEditTime: 2023-07-18 09:05:39
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


class Solution:

    # intervals 数组和 queries 数组的长度，分别为 m 和 n。
    # O((m+n)logm)
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        result = [-1] * len(queries)
        heap = []
        i = 0
        for j, query in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                length = intervals[i][1]-intervals[i][0]+1
                heappush(heap, (length, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < query:
                heappop(heap)
            if heap:
                result[j] = heap[0][0]
        return result

    # O(n2)
    def minInterval1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            answer = inf
            for l in intervals:
                if l[1] >= q and l[0] <= q:
                    answer = min(answer, l[1]-l[0]+1)
            res.append(-1 if answer == inf else answer)
        return res


if __name__ == "__main__":
    print(Solution.minInterval(self=None, intervals=[[1, 4], [2, 4], [
                         3, 6], [4, 4]], queries=[2, 3, 4, 5]))
