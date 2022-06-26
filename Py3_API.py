# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 17:35

import numpy as np

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

    a = np.array([[1, 2], [3, 4]])
