# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 18:01

# lcm为最小公倍数
import math

class Solution:
    def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
        # x的上下界为[1,2*10^9]
        l, r = 1, 2 * 10 ** 9
        ans = 0
        while l <= r:
            x = (l + r) // 2
            # 数字x，小于等于x的丑数个数
            count = x // a + x // b + x // c - x // math.lcm(a, b) - x // math.lcm(a, c) - x // math.lcm(b, c) + x // math.lcm(a, b, c)
            if count >= n:
                ans = x
                r = x - 1
            else:
                l = x + 1
        return ans


if __name__ == '__main__':
    print(Solution.nthUglyNumber(n=3, a=2, b=3, c=5))
