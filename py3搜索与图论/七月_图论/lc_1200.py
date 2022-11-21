
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/4 08:32
from python3语法基础.Py流式.py_itertools import pairwise
from math import inf
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m, ans = inf, []
        for a, b in pairwise(sorted(arr)):
            if (cur := b - a) < m:
                m, ans = cur, [[a, b]]
            elif cur == m:
                ans.append([a, b])
        return ans


