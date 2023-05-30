'''
Author: hakusai
Date: 2023-05-30 20:21:16
LastEditTime: 2023-05-30 20:25:18
Description: 
'''

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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            root.left, root.right = dfs(root.left), dfs(root.right)
            if root.val not in s:
                return root
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            return None

        s = set(to_delete)
        ans = []
        if dfs(root):
            ans.append(root)
        return ans
