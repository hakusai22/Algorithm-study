# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/3 23:27

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        n = len(s)
        ans = s
        s = s + s
        for i in range(n):
            ans = min(ans, s[i:n + i])
        return ans
