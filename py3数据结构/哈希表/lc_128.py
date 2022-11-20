# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/20 08:16


def longestConsecutive(nums):
    hash_dict = dict()
    max_length = 0
    for num in nums:
        if num not in hash_dict:
            # 判断左右是否可以连起来
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)
            # 记录长度
            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            hash_dict[num] = cur_length
            # 把头尾都设置为最长长度
            hash_dict[num - left] = cur_length
            hash_dict[num + right] = cur_length
    return max_length
