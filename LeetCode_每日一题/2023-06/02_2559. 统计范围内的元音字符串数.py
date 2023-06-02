'''
Author: hakusai
Date: 2023-06-02 23:36:02
LastEditTime: 2023-06-02 23:37:13
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


vowels = set('aeiou')
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        acc = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                acc.append(acc[-1] + 1)
            else:
                acc.append(acc[-1])
        return [acc[r+1] - acc[l] for l, r in queries]

