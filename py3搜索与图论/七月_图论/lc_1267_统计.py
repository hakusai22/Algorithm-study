# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/7 21:24
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_m = [0 for _ in range(m)]
        count_n = [0 for _ in range(n)]
        for i, g in enumerate(grid):
            count_m[i] = g.count(1)
        grid_b = list(zip(*grid))
        for i, g in enumerate(grid_b):
            count_n[i] = g.count(1)
            # print(count_n)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (count_m[i] > 1 or count_n[j] > 1):
                    ans += 1
        return ans
