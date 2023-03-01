from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/23 20:32

"""
编程题
输入任意一种物质，要求输出其每种元素的数量。
比如
输入 CaCO3，其组成分别为 Ca:1，C:1，O:3，输出 Ca1C1O3
输入 Fe2(SO4)3，其组成分别为 Fe:2，S:3，O:12，输出 Fe2S3O12 (注意:元素名称首字母大写，剩余字母都小写;括号括起来表示括号中的结构作 为整体出现多少次)
"""

def countOfAtoms(formula: str) -> str:
    n = len(formula)
    map = defaultdict(lambda: 1)
    d = deque([])
    i = idx = 0
    while i < n:
        c = formula[i]
        if c == '(' or c == ')':
            d.append(c)
            i += 1
        else:
            if str.isdigit(c):
                # 获取完整的数字，并解析出对应的数值
                j = i
                while j < n and str.isdigit(formula[j]):
                    j += 1
                cnt = int(formula[i:j])
                i = j
                # 如果栈顶元素是 )，说明当前数值可以应用给「连续一段」的原子中
                if d and d[-1] == ')':
                    tmp = []
                    d.pop()
                    while d and d[-1] != '(':
                        cur = d.pop()
                        map[cur] *= cnt
                        tmp.append(cur)
                    d.pop()

                    for k in range(len(tmp) - 1, -1, -1):
                        d.append(tmp[k])
                # 如果栈顶元素不是 )，说明当前数值只能应用给栈顶的原子
                else:
                    cur = d.pop()
                    map[cur] *= cnt
                    d.append(cur)
            else:
                # 获取完整的原子名
                j = i + 1
                while j < n and str.islower(formula[j]):
                    j += 1
                cur = formula[i:j] + "_" + str(idx)
                idx += 1
                map[cur] = 1
                i = j
                d.append(cur)

    #  将不同编号的相同原子进行合并
    mm = defaultdict(int)
    for key, cnt in map.items():
        atom = key.split("_")[0]
        mm[atom] += cnt

    # 对mm中的key进行排序作为答案
    ans = []
    for key in sorted(mm.keys()):
        if mm[key] > 1:
            ans.append(key + str(mm[key]))
        else:
            ans.append(key)
    return "".join(ans)

if __name__ == '__main__':
    countOfAtoms("Fe2(SO4)3")
    print()
