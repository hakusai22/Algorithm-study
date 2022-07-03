# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/3 16:03

# 1111169741的下一个排列是，从右到左找到第一个不满足单调增的地方，即9和6。
# 交换6和1479中第一个比6大的（这样下一个排列尽可能小），即变为1111179641。
# 然后将9641这部分倒序得到1111171469即可。

MAX_32 = 2147483647


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        return nxt if (nxt := int(
            "".join(map(str, self.nextPermutation(list(map(int, list(str(n))))))))) > n and nxt <= MAX_32 else -1

    def nextPermutation(self, nums):
        n = len(nums)
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return nums

        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        left, right = index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
