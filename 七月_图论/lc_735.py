# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/13 21:42
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            add = True
            # 只有新来的向左的，才有可能和原来的发生碰撞 (想象最后一个是向右的话，没有人能和它相撞)
            if ast < 0:
                # 依次遍历栈顶全部向右的，它们会和当前的相撞，如果它们大小小于当前的大小，它们会被撞没
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                # 如果还存在向右的，说明当前的大小撞不过栈顶
                if stack and stack[-1] > 0:
                    add = False
                    # 两个一样大的都要消失
                    if stack[-1] == -ast:
                        stack.pop()
            if add:
                stack.append(ast)
        return stack
