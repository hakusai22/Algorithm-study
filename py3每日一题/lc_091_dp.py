# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 11:50
from typing import List


# 当前最小花费由当前刷红、刷蓝、刷绿中最小的花费决定。
# 当前刷红，上一个只能是蓝或绿，所以由上一次蓝绿最小值加上当前红的代价得到。
# https://leetcode.cn/problems/JEj789/


class Solution:
    def minCost(costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g
        return min(red, blue, green)


if __name__ == '__main__':
    print(Solution.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
