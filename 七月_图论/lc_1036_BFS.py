# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/3 16:05
from typing import List

BOUND = int(1e6)


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked, MAX = {tuple(p) for p in blocked}, len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            points, idx, explored = [start], 0, {tuple(start)}
            while idx < len(points):
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    nx, ny = points[idx][0] + dx, points[idx][1] + dy
                    if 0 <= nx < BOUND and 0 <= ny < BOUND and (nx, ny) not in blocked and (nx, ny) not in explored:
                        if [nx, ny] == end:
                            return True
                        explored.add((nx, ny))
                        points.append((nx, ny))

                if len(points) > MAX:
                    return True
                idx += 1
            return False

        return bfs(source, target) and bfs(target, source)
