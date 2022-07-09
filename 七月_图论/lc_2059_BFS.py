# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/8 08:02

from collections import deque, defaultdict


class Solution:
    def minimumOperations(self, nums, start: int, goal: int) -> int:
        queue = deque([start])
        visited = defaultdict(bool)
        now_distance = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_elem = queue.popleft()
                for elem in nums:
                    plus = cur_elem + elem
                    sub = cur_elem - elem
                    xor = cur_elem ^ elem
                    if plus == goal or sub == goal or xor == goal:
                        return now_distance
                    if 0 <= plus <= 1000 and not visited[plus]:
                        visited[plus] = True
                        queue.append(plus)
                    if 0 <= sub <= 1000 and not visited[sub]:
                        visited[sub] = True
                        queue.append(sub)
                    if 0 <= xor <= 1000 and not visited[xor]:
                        visited[xor] = True
                        queue.append(xor)
            now_distance += 1
        return -1
