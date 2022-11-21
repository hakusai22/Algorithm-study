# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/16 19:32

"""
对于时针来说 1小时占30°，时针由于分针运动会有个偏移，总的偏移角度就是 1小时，即30°，
一小时60分钟，所以偏移 minutes/60 * 30.
# 所以时针总的偏移 30*hour + minutes/60 * 30
# 分针的偏移则更简单，分针总共能转 360°，一共60分钟。
# 所以分针偏移 minutes/60 * 360
# 两者之差的绝对值就是两者之间的角度，如果大于180° 就返回其360 - 其角度。
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = hour * 30 + minutes / 60 * 30
        m = minutes / 60 * 360
        ans = abs(h - m)
        if ans > 180:
            return 360 - ans
        return ans
