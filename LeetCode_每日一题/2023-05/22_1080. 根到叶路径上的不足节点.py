'''
Author: hakusai
Date: 2023-05-22 20:36:00
LastEditTime: 2023-05-22 20:38:42
Description: 
'''
# Definition for a binary tree node.
from collections import Counter, defaultdict, deque
from typing import List, Optional
from cmath import inf
from math import factorial, gcd
from bisect import bisect_left, bisect_right
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from itertools import accumulate, combinations, permutations, product
from functools import cache, lru_cache, reduce, cmp_to_key


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None:
            return None
        limit -= root.val
        # 叶子结点
        if root.left is None and root.right is None:
            return None if limit > 0 else root
        # 递归左右
        root.left = self.sufficientSubset(root.left, limit)
        root.right = self.sufficientSubset(root.right, limit)
        return None if root.left is None and root.right is None else root
