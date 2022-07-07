# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/7 21:07
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pos_wall = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    pos_wall.add((i, j))
                elif grid[i][j] == 'T':
                    pos_t = (i, j)
                elif grid[i][j] == 'B':
                    pos_b = (i, j)
                elif grid[i][j] == 'S':
                    pos_s = (i, j)

        # 判断箱子在block，墙壁为pos_wall时，从start是否可到达end
        def can_arrive(start, end, block, pos_wall):
            que = [start]
            visited = set([start])
            while que:
                # print('que={}'.format(que))
                i, j = que.pop(0)
                if (i, j) == end: return True
                for d_i, d_j in direcs:
                    i1, j1 = i + d_i, j + d_j
                    if 0 <= i1 < m and 0 <= j1 < n and (i1, j1) != block and \
                            (i1, j1) not in pos_wall and (i1, j1) not in visited:
                        que.append((i1, j1))
                        visited.add((i1, j1))
            return False

        # que保存箱子的位置 人的位置 已走步数
        que = [[pos_b[0], pos_b[1], pos_s[0], pos_s[1], 0]]
        visited_b = set()
        while que:
            i_b, j_b, i_s, j_s, steps = que.pop(0)
            if (i_b, j_b) == pos_t:
                return steps
            for d_i, d_j in direcs:
                i1, j1 = i_b + d_i, j_b + d_j
                i_push, j_push = i_b - d_i, j_b - d_j
                start, end, block = (i_s, j_s), (i_push, j_push), (i_b, j_b)
                if 0 <= i1 < m and 0 <= j1 < n and 0 <= i_push < m and 0 <= j_push < n \
                        and (i1, j1) not in pos_wall and (i_push, j_push) not in pos_wall \
                        and (i_b, j_b, i1, j1) not in visited_b \
                        and can_arrive(start, end, block, pos_wall):
                    # 人站在(i_push, j_push)把石头从(i_b, j_b)推到(i1, j1) 然后人站在(i_b,j_b)
                    que.append([i1, j1, i_b, j_b, steps + 1])
                    visited_b.add((i_b, j_b, i1, j1))

        return -1
