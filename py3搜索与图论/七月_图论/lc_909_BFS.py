# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/2 11:27
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # x -> pos
        def transform(idx):
            i = n - 1 - (idx - 1) // n
            j = idx - 1 - (n - 1 - i) * n if i % 2 != n % 2 else (n - i) * n - idx
            return i, j

        queue = deque([(1, 0)])
        explored = {1}
        while queue:
            x, step = queue.popleft()
            if x == n * n:
                return step
            for dx in range(1, 7):
                nxt = x + dx
                if nxt > n * n:
                    break
                if nxt not in explored:
                    i, j = transform(nxt)
                    explored.add(nxt)
                    # 该位置有跳跃
                    if board[i][j] != -1:
                        queue.append((board[i][j], step + 1))
                    else:
                        queue.append((nxt, step + 1))
        return -1
