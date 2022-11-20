# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/26 21:11
import calendar
import time

if __name__ == '__main__':
    print("当前时间戳:", time.time())

    print("本地时间", time.localtime(time.time()))

    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    cal = calendar.month(2016, 1)
    print("以下输出2016年1月份的日历:")
    print(cal)

    print(help('zip'))

    print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
