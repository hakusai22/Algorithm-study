# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 17:35

from py_itertools import *


def multiplier_func(a, b):
    return a * b


def square_it_func(a):
    return a * a


def filter_odd_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(range(5))
    print(list(range(5)))

    print(zip([1, 2, 3], [4, 5, 6]))
    print(list(zip([1, 2, 3], [4, 5, 6])))
    print(list(zip([1, 2, 3], [4, 5, 6]))[0][0])
    print(list(zip([1, 2, 3], [4, 5, 6]))[0][1])

    a = {1: 10, 2: 4}
    print(a.get(1))
    print(a.keys())
    print(list(a.keys()))

    a = [1, 2, 3]
    i = a.__iter__()
    print(i.__next__())

    x = lambda a, b: a * b

    print(x(5, 6))  # prints  30

    x = lambda a: a * 3 + 3

    print(x(3))  # prints  12

    x = map(square_it_func, [1, 4, 7])

    print(list(x))  # prints  [1, 16, 49]

    x = list(map(multiplier_func, [1, 4, 7], [2, 5, 8]))

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    filtered_numbers = filter(filter_odd_numbers, numbers)

    print(list(filtered_numbers))

