'''
Author: hakusai
Date: 2023-04-21 08:33:31
LastEditTime: 2023-04-21 08:35:06
'''
from math import lcm


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(2, n)
