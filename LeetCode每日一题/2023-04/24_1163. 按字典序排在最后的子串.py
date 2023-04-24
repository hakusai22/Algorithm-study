'''
Author: hakusai
Date: 2023-04-24 09:58:19
LastEditTime: 2023-04-24 10:01:20
'''


class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i:] for i in range(len(s)))
