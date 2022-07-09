
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/9 14:50
from functools import lru_cache
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        @lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return [[n - 1]]
            ans = []
            for nxt in graph[node]:
                for res in dfs(nxt):
                    ans.append([node] + res)
            return ans

        return dfs(0)

