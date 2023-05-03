'''
Author: hakusai
Date: 2023-05-03 10:45:53
LastEditTime: 2023-05-03 10:47:48
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        t = []
        for c in s:
            t.append(c)
            if "".join(t[-3:]) == 'abc':
                t[-3:] = []
        return not t
