# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/27 11:14

if __name__ == '__main__':
    example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    result_list = sorted(example_list)
    print(result_list)
    result_list = sorted(example_list, key=lambda x: x)
    print(result_list)
    result_list = sorted(example_list, key=lambda x: x * -1)
    print(result_list)

    result_list = sorted(example_list)
    print(result_list)
    result_list = sorted(example_list, reverse=True)
    print(result_list)

    array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
    array = sorted(array, key=lambda x: x["age"] * -1)
    print(array)

    d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
          {'name': 'christ', 'score': 28}]
    l = sorted(d1, key=lambda x: (-x['score'], x['name']))
    print(l)
