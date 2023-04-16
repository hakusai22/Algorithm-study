#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wink
    @Time    : 2023/02/19 21:22
*/

/*
    c++中map与unordered_map的区别
        运行效率方面：unordered_map最高，而map效率较低但 提供了稳定效率和有序的序列。
        占用内存方面：map内存占用略低，unordered_map内存占用略高,而且是线性成比例的。

    内部实现机理
        map： map内部实现了一个红黑树，该结构具有自动排序的功能，因此map内部的所有元素都是有序的，红黑树的每一个节点都代表着map的一个元素，因此，对于map进行的查找，删除，添加等一系列的操作都相当于是对红黑树进行这样的操作，故红黑树的效率决定了map的效率。
        unordered_map: unordered_map内部实现了一个哈希表，因此其元素的排列顺序是杂乱的，无序的

 */

int main() {
    // 构造函数
    map<string, int> dict;

    // 插入数据的三种方式
    dict.insert(pair<string, int>("apple", 2));
    dict.insert(map<string, int>::value_type("orange", 3));
    dict["banana"] = 6;

    // 判断是否有元素
    if (dict.empty())
        cout << "该字典无元素" << endl;
    else
        cout << "该字典共有" << dict.size() << "个元素" << endl;

    // 遍历
    map<string, int>::iterator iter;
    for (iter = dict.begin(); iter != dict.end(); iter++)
        cout << iter->first << ends << iter->second << endl;

    // 查找
    if ((iter = dict.find("banana")) != dict.end()) //  返回一个迭代器指向键值为key的元素，如果没找到就返回end()
        cout << "已找到banana,其value为" << iter->second << "." << endl;
    else
        cout << "未找到banana." << endl;

    if (dict.count("watermelon") == 0) // 返回键值等于key的元素的个数
        cout << "watermelon不存在" << endl;
    else
        cout << "watermelon存在" << endl;



    // unordered_map
    unordered_map<string, int> dict2; // 声明unordered_map对象

    // 插入数据的三种方式
    dict2.insert(pair<string, int>("apple", 2));
    dict2.insert(unordered_map<string, int>::value_type("orange", 3));
    dict2["banana"] = 6;

    // 判断是否有元素
    if (dict2.empty())
        cout << "该字典无元素" << endl;
    else
        cout << "该字典共有" << dict2.size() << "个元素" << endl;

    return 0;
}
