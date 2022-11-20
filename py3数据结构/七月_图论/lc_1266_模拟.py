# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/7 21:14
from typing import List

# 统计下一个点与当前点x,y差值中最大的之和

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = 0
        for i in range(len(points) - 1):
            x = abs(points[i + 1][0] - points[i][0])
            y = abs(points[i + 1][1] - points[i][1])
            n += max(x, y)
        return n
