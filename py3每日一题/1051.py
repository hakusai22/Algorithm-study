# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/13 20:57
from typing import List


# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# heights = [1,1,4,2,1,3]
# sorted(heights) [1,1,1,2,3,4]
# zip() [(1,1),(1,1),(4,2),(2,3),(1,3),(3,4)]
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))
