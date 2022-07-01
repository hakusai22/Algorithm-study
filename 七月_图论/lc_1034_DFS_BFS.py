# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/1 08:23
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        explored = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n:
                return True
            if (r, c) in explored:
                return False
            if grid[r][c] != grid[row][col]:
                return True
            explored.add((r, c))
            ans = False
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                if dfs(r + dx, c + dy):
                    ans = True
            if ans:
                grid[r][c] = color
            return False

        dfs(row, col)
        return grid
