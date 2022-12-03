from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

MOD = int(1e9 + 7)
INF = int(1e20)
'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''

def I():
    return input()

def II():
    return int(input())

def FI():
    return float(input())

def MII():
    return map(int, input().split())

def MFI():
    return map(float, input().split())

def LI():
    return list(input().split())

def LMII():
    return list(map(int, input().split()))

def LMFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/12/04 01:39

class Node:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        """
        left:   左孩子
        right:  右孩子
        val:    值
        lazy:   懒惰标记，是0说明没有懒惰标记，是正数说明这里的懒惰标记还未下放
        """
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy

    def __repr__(self):
        return f'<Node val: {self.val} lazy: {self.lazy} {self.left} {self.right}>'


class MySegTree:
    def __init__(self, size):
        """
        size:   线段树的总大小（根节点管理的区间的长度）
        """
        self.size = size
        self.root = Node()
        return

    def push_down(self, node, s, e):
        """
        向下更新，并传递懒惰更新标志
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        """
        mid = s + ((e - s) >> 1)
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if not node.lazy:
            return
        node.left.val += node.lazy
        node.right.val += node.lazy
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0
        return

    def push_up(self, node):
        """
        向上更新，要求node的两个子节点均已更新完
        node:   当前节点
        """
        node.val = max(node.left.val, node.right.val)
        return

    def update(self, node, s, e, l, r, add):
        """
        更新闭区间[l, r]，给此区间内的每个值，都加上add
        闭区间[l, r]和当前区间[s, e]的交集一定非空
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        l:      left，要更改的区间的左边界
        r:      right，要更改的区间的右边界
        add:    addition，增量
        """
        if l <= s and e <= r:
            node.val += add
            node.lazy += add
            return

        self.push_down(node, s, e)
        mid = s+((e-s)>>1)

        if l <= mid:
            self.update(node.left, s, mid, l, r, add)
        if r > mid:
            self.update(node.right, mid+1, e, l, r, add)

        self.push_up(node)
        return

    def query(self, node, s, e, l, r):
        """
        查询闭区间[l, r]的区间最大值
        闭区间[l, r]和当前区间[s, e]一定是有交集的
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        l:      left，要更改的区间的左边界
        r:      right，要更改的区间的右边界
        """
        if l <= s and e <= r:
            return node.val

        self.push_down(node, s, e)
        mid = s + ((e - s) >> 1)

        ans = float('-inf')
        if l <= mid:
            ans = max(ans, self.query(node.left, s, mid, l, r))
        if r > mid:
            ans = max(ans, self.query(node.right, mid + 1, e, l, r))

        return ans

class MyCalendarThree:

    def __init__(self):
        self.size = 10 ** 9
        self.seg_tree = MySegTree(size=self.size)

    def book(self, start: int, end: int) -> int:
        # 如果预定当前请求，为预定到的时间段内的每个时间片的占用次数+1
        self.seg_tree.update(self.seg_tree.root, 0, self.size, start, end-1, 1)
        return self.seg_tree.query(self.seg_tree.root, 0, self.size, 0, self.size)

