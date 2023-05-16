#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/19 17:50
*/



int main() {

    /**
     *  1.lower_bound(起始地址，结束地址，要查找的数值) 返回的是数值第一次出现的位置。
            函数lower_bound()在first和last中的前闭后开区间进行二分查找，返回大于或等于val的第一个元素位置。如果所有元素都小于val，则返回last的位置.
        2.upper_bound(起始地址，结束地址，要查找的数值) 返回的是数值最后一次出现之后的位置。
            函数upper_bound()返回的在前闭后开区间查找的关键字的上界，返回大于val的第一个元素位置
        3.binary_search(起始地址，结束地址，要查找的数值)  返回的是是否存在这么一个数，是一个bool值。
     */

    int a[8] = {1, 3, 3, 7, 8, 8, 8, 9};
    bool is_exist = binary_search(a, a + 8, 3);
    int lower_index = lower_bound(a, a + 8, 3) - a;
    int upper_index = upper_bound(a, a + 8, 3) - a;
    cout << "is_exist: " << is_exist << endl;
    cout << "lower_index: " << lower_index << endl;
    cout << "upper_index: " << upper_index << endl;
    cout << "upper_index: " << upper_index << endl;

    return 0;
}
