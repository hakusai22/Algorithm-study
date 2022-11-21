# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/13 21:41
import collections
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        nums = ''.join(str(num) for row in board for num in row)
        q = collections.deque()
        # 只能移动0, 每次记录0的位置
        q.append((nums, nums.index('0')))

        visited_set = set(nums)
        steps, rows, cols = 0, len(board), len(board[0])
        while q:
            for _ in range(len(q)):
                cur_nums, idx = q.popleft()

                if cur_nums == '123450':
                    return steps

                # 数字当前行和列 x,y
                x, y = idx // cols, idx % cols
                directions = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
                for r, c in directions:
                    if rows > r >= 0 and 0 <= c < cols:
                        cur_nums_lst = list(cur_nums)
                        # 交换 0 与一个相邻的数字， 交换后 0在 num_idx 的位置
                        num_idx = r * cols + c
                        cur_nums_lst[idx], cur_nums_lst[num_idx] = cur_nums_lst[num_idx], '0'

                        nums = ''.join(cur_nums_lst)
                        if nums not in visited_set:
                            visited_set.add(nums)
                            q.append((nums, num_idx))
            steps += 1
        return -1
