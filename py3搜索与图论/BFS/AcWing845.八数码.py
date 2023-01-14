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
INFMIN = float('-inf')
INFMAX = float('inf')
'''
    @functools.lru_cache(None) 记忆化搜索
    字符串切片 str[::-1] # 字符串翻转  str[0:1]  左闭右开
    列表 l.append(1) l.extend([1,2,3]) l.insert(1,3) l.remove(1),(del list[0]) ,l.pop() ,l.pop(0), l.sort(reverse=True) ,l.reverse() 列表操作 
    ASCII ord('a'), chr(98), /ASCII字符数值/数值ASCII字符
    字符串 s.lower(), s.upper() ,s.title() /小写/大写/首字母大写
    字符串 str.replace('k','8',2) ,str.strip() ,str.rstrip(), str.lstrip(),  #将字符串里的k替换为8,前两个/删除空白
    字符串 str.startswith(s), str.endswith(s), str.find(s), str.index(s), str.count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找s返回的是索引/获取s的索引
    字符串 s.isalpha(), s.isdigit(), s.isspace(), "_".join([1,2])  判断是否全为字符/判断是否全为数字/判断是否为空格/使用_拼接列表
    字典 m.keys(), m.values(), m.items() 字段key的列表/value的列表/ key,value值对
    eval("1,2,3") 字符串转换成列表、元组或者字典/
    公式 gcd(a,b), lcm(a,b), pow(a,b), sqrt(x), ceil(x), floor(x) /最大公约数/最小公倍数/ x的y次方/ x的平方根 /向上/向下
    堆 heapfiy([]),heappush(1), heappop(),nlargest(3,list),nsmallest(3,list),heapreplace(list,4) list转为最小堆/添加元素/弹出最小值并返回/返回堆最大的3个元素/返回堆中最小的3个元素/弹出堆顶元素,压入4
    双端队列 d.append(1), appendleft(1), d.pop(), d.popleft(), d.clear(),d.count(1), d.reverse() /队尾添加/队头添加
    栈(列表) s.append(1) s.pop() /压栈/弹出栈顶元素
    
    列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
    字典推倒式 {key: len(key) for key in list}
    集合推倒式 {i ** 2 for i in (1, 2, 3) if i % 3 == 0}  不可索引,不可切片,不可重复元素
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
# @Author  : wheat
# @Time    : 2023/01/13 15:54

"""
	 * 使用BFS找出最短的距离
	 * 使用map存储交换后的字符串和交换次数
"""

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(start):
        end = "12345678x"
        # 记录每个状态的交换次数，初始状态为0
        d = {start: 0}
        # 记录队列头结点到了哪个状态
        q = deque([start])
        while len(q):
            # 头结点出队
            t = q.popleft()
            # 保存当前头结点距离初始状态的交换次数
            distance = d[t]
            if t == end:
                return distance

            # 找下表，交换顺序
            idx = t.find('x')
            x = idx // 3
            y = idx % 3
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if 0 <= a < 3 and 0 <= b < 3:
                    # 字符串不能够交换，所以先转成列表再交换
                    t = list(t)
                    t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]
                    t = ''.join(t)
                    # 如果新的状态不在字典里
                    if t not in d:
                        # 添加新的状态进入字典并且赋值为上一个状态的交换次数 + 1
                        d[t] = distance + 1
                        # 将新的状态入队
                        q.append(t)
                    # 记得一定要回退状态
                    t = list(t)
                    t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]
                    t = ''.join(t)

        return -1

    n = input().split()
    start = ''
    for c in n:
        start += c

    print(bfs(start))
