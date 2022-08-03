# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/3 23:30
import random


# 空间换时间的典型题型
# 字典存储数字及其在stack中的索引，插入时直接在stack后面加入，删除时交换val和stack中最后一个数字，随后pop并更新字典中的值
# stack存储数字，用来实现在常数时间内返回随机值
#
class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val in self.h:  return False
        self.stack.append(val)
        self.h[val] = len(self.stack) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h: return False
        last = len(self.stack) - 1
        tar = self.h[val]
        tar_num = self.stack[-1]
        self.stack[last], self.stack[tar] = self.stack[tar], self.stack[last]
        self.stack.pop()
        self.h[tar_num] = tar
        del self.h[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


