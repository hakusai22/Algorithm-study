#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/19 19:20
*/

/*
    vector是一个十分有用的容器，是一个能够存放任意类型的动态数组，能够增加和压缩数据。
    vector的优点:
    （1）可将容器中元素翻转、复制元素、找到元素值对应的位置
    （2）迭代器可以按照不同的方式遍历容器
    （3）可在容器的末尾增加或删除元素
    （4）可在任意位置插入数据
    与数组相比，容器在自动处理容量的大小时会消耗更多的内存，但能很好的调整存储空间大小。
 */



int main() {
    // 创建vector对象
    vector<int> array;

    array.push_back(1); //尾部插入数字1
    array.pop_back(); //删除向量的最后一个元素

    // array[0],array[1]......array[n]
    int first = array[0];
    cout << first << endl;

    array.push_back(1); //尾部插入数字1
    array.push_back(1); //尾部插入数字1
    array.at(1); //使用at(),当这个函数越界时会抛出一个异常

    // 使用迭代器访问元素
    vector<int>::iterator it;
    for (it = array.begin(); it != array.end(); it++)
        cout << *it << endl;

    array.insert(array.begin() + 1, 2); //在第1个元素前面插入a;
    for (auto &item: array) {
        cout << item << " ";
    }
    cout << endl;
    array.push_back(1); //尾部插入数字1
    array.push_back(1); //尾部插入数字1
    array.push_back(1); //尾部插入数字1
    array.push_back(1); //尾部插入数字1

    for (auto &item: array) {
        cout << item << " ";
    }
    cout << endl;

    array.erase(array.begin() + 1); //删除第2个元素
    array.erase(array.begin() + 2, array.begin() + 4); //删除区间[1,3],区间从0开始
    for (auto &item: array) {
        cout << item << " ";
    }
    cout << endl;

    // (8) 向量大小: array.size();
    // (9) 清空: array.clear();
    cout << array.size() << endl;
    array.clear();

    array.push_back(1);
    array.push_back(1);
    array.push_back(1);
    array.push_back(1);
    //10. 当元素个数为0时返回true，否则为false
    cout << array.empty() << endl;

    // (11) 返回最后一个元素：array.back();
    cout << array.back() << endl;
    // (12) 返回第一个元素：array.front();
    cout << array.front() << endl;
    // (13) 返回内存中总共可以容纳的元素个数：array.capacity();
    cout << "capacity: " << array.capacity() << endl;

    array.resize(10); //将a的现有元素个数调至10个，多则删，少则补，其值随机
    array.resize(10, 2); //将a的现有元素个数调至10个，多则删，少则补，其值为2
    for (auto &item: array) {
        cout << item << " ";
    }
    cout << endl;
    cout << &array << endl;


    reverse(array.begin(), array.end()); //将元素翻转，即逆序排列

    sort(array.begin(), array.end());

    // 在a中的从a.begin()（包括它）到a.end()（不包括它）的元素中查找10，若存在返回其在向量中的位置
    find(array.begin(), array.end(), 10);


    vector<float> vecClass;
    vecClass.push_back(0.1f);
    vecClass.push_back(0.1f);
    vecClass.push_back(0.1f);
    vecClass.push_back(0.1f);
    int nSize = vecClass.size();

    //方法一（下标方式）打印vecClass
    for (int i = 0; i < nSize; i++) {
        cout << vecClass[i] << "     ";
    }
    cout << endl;

    //方法二（下标方式）打印vecClass
    for (int i = 0; i < nSize; i++) {
        cout << vecClass.at(i) << "     ";
    }
    cout << endl;

    //方法三（遍历器方式）打印vecClass：输出某一指定的数值时不方便
    for (vector<float>::iterator it = vecClass.begin(); it != vecClass.end(); it++) {
        cout << *it << "   ";
    }
    cout << endl;

    for (auto &item: vecClass) {
        cout << item << " ";
    }
    cout << endl;

    return 0;
}


