# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/13 22:23

if __name__ == '__main__':
    # 1. python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
    print(divmod(7, 2))  # (3, 1)

    # 2. map() 会根据提供的函数对指定序列做映射。
    print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

    # 提供了两个列表，对相同位置的列表数据进行相加 # 使用 list() 转换为列表
    print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

    # 3. 列表list，元素都不为空或0
    print(all(['a', 'b', 'c', 'd']))  # True

    print(all(('a', 'b', '', 'd')))  # 元组tuple，存在一个为空的元素

    # 4. enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    print(list(enumerate(
        ['Spring', 'Summer', 'Fall', 'Winter'])))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

    for i, element in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
        print(i, element)

    # 5. sorted() 函数对所有可迭代的对象进行排序操作。
    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]  # 按年龄排序
    print(sorted(students, key=lambda s: s[2]))

    print(sorted(students, key=lambda s: s[2], reverse=True))  # 降序

    # 6.cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

    # 7. filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
    def is_odd(n):
        return n % 2 == 1

    print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

    # 8. slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr[:])

    # oct() 函数将一个整数转换成 8 进制字符串。
    print(oct(10))

    # hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
    print(hex(255))

    # dict() 函数用于创建一个字典。
    print(dict(a='a', b='b', t='t'))

    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    print(eval('3 * 2'))

    # float() 函数用于将整数和字符串转换成浮点数。
    print(float(1))

    # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
    print(any(['a', 'b', 'c', 'd']))

    # len() 方法返回对象（字符、列表、元组等）长度或项目个数。
    print(len("asdawsdasd"))

    # range() 函数可创建一个整数列表，一般用在 for 循环中。
    print(list(range(10)))
    print(list(range(1, 11)))
    print(list(range(0, 30, 5)))
    print(list(range(0, -10, -1)))

    # type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
    print(type({0: 'zero'}))
