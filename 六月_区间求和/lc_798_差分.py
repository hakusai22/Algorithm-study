# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/29 08:13

# 我们的每个数都是在某个靠后的连续的区间内会对得分产生贡献，在某个靠左的区间内则不会产生贡献；从而我们要记录分数，最高效的记录手段就是记录每次移动导致贡献与否产生变化的位置；这就是差分。
# 和前缀和一样，我们需要预处理，我们遍历一遍每个数，通过直接计算得到产生分数贡献变化的分界点，将对应的移动值和变化记录下来。
# 最后求总分的时候再遍历累计求和即可；相当于用积分恢复差分对应的原始值。

# 一个数num,最终和坐标差小于等于0，只有一个范围，那就是坐标在[num, n-1]之间，而坐标在[0, num-1]之间时差显然会大于0。

# 当i最开始的位置在[num, n-1]之间时，不移动本身就会对答案作出一个贡献，即diff[0]+=1；
# 当k逐渐变大时，i会向左移动出num，那个时候对答案不作出贡献了，即diff[i - num + 1] -= 1；
# 持续移动超过最左端0以后会回到n-1，又会对答案作出贡献，即diff[i + 1] += 1。
#
# 当i最开始的位置在[0, num - 1] 之间时，不移动本身不会对答案作出贡献。移动超过最左端0回到n-1，会对答案作出贡献，即diff[i + 1] += 1；
# 当继续移动，超过num回到[0, num - 1] 之间时，又不会再对答案做出贡献了，即diff[i - num + n + 1] -= 1。
#
# 我们只需要对diff进行遍历，维护每个时刻有多少个坐标满足差小于等于0，最终返回最大且最小的k即可。

from typing import List


# https://leetcode.cn/problems/smallest-rotation-with-highest-score/
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        # num ---> n - 1
        for i, num in enumerate(nums):
            if i >= num:
                diff[0] += 1
                diff[i - num + 1] -= 1
                diff[i + 1] += 1
            else:
                diff[i + 1] += 1
                diff[i - num + n + 1] -= 1
        ans = cur = mx = 0
        for i in range(n):
            cur += diff[i]
            if cur > mx:
                ans, mx = i, cur
        return ans
