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
字典推倒式 {key: len(key) for key in list}
'''

# 语法1
'''
	new_dictionary = {key_exp:value_exp for key, value in dict.items() if condition}
	字典推导式说明：
    key：dict.items()字典中的key
    value：dict.items()字典中的value
    dict.items()：序列
    condition：if条件表达式
    key_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的key,value当作key_exp,value_exp处理 
    value_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的key,value当作key_exp,value_exp处理
	这样就返回一个新的字典。
'''

# 语法2
'''
	{key_exp:value_exp1 if condition else value_exp2 for key, value in dict.items()}
	字典推导式说明：
    key：dict.items()字典中的key 
    value：dict.items()字典中的value 
    dict.items()：序列 
    condition：if条件表达式的判断内容 
    value_exp1：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp1处理
    value_exp2：在for循环中，如果条件表达式condition不成立(即条件表达式不成立)，返回对应的key,value并作key_exp,value_exp2处理
'''

if __name__ == '__main__':
    dictionary_1 = {'a': '1234', 'B': 'FFFF', 'c': ' 23432', 'D': '124fgr', 'e': 'eeeee', 'F': 'QQQQQ'}

    # 案例一：获取字典中key值是小写字母的键值对
    new_dict_1 = {key: value for key, value in dictionary_1.items() if key.islower()}
    new_dict_2 = {g: h for g, h in dictionary_1.items() if g.islower()}
    # g, h只是一个变量，使用任意字母都行，但是一定要前后保持一致。
    print(new_dict_1)
    print(new_dict_2)

    # 案例二：将字典中的所有key设置为小写
    new_dict_3 = {key.lower(): value for key, value in dictionary_1.items()}
    # 将字典中的所有key设置为小写,value值设置为大写
    new_dict_4 = {key.lower(): value.upper() for key, value in dictionary_1.items()}
    print(new_dict_3)
    print(new_dict_4)

    # 案例三：将字典中所有key是小写字母的value统一赋值为'error'
    new_dict_5 = {key: value if not key.islower() else 'error' for key, value in dictionary_1.items()}  # if条件表达式用到了“非”的逻辑
    # value if not key.islower() else 'error' 这一段的代码的含义是：
    # 如果not key.islouer()--key值不是小写的，那么返回if前面的value值，否则就返回else后面的值。
    print(new_dict_5)