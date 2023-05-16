#include <bits/stdc++.h>

#include<iostream>
#include<string>
#include<cstdlib>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/19 17:22
*/

int main() {
    string str = "Be yourself";

    //提取字符串, 从第三位开始, 长度为8
    string sub_str = str.substr(3, 8);
    cout << "Substr:" << sub_str << endl;

    //在字符串末尾添加字符, 不能是字符串
    str.push_back('!');
    cout << "Push_back:" << str << endl;

    //插入字符串
    string insert_str = "-->";
    str.insert(2, insert_str);
    cout << "Insert:" << str << endl;
    //从第二位开始插入字符串的一部分(第0位开始后的2个字符)
    str.insert(2, insert_str, 0, 2);
    cout << "New_Insert:" << str << endl;
    //2018.10.8补充
    //string &insert(int p0, int n, char c); 在p0处插入n个字符c

    //替换字符串, 替换从下标为2的位置开始, 长度为2的字符串
    str.replace(2, 2, " ");
    cout << "Replace:" << str << endl;

    //删除字符串, 下标为2开始后的3个字符
    str.erase(2, 4);
    cout << "Erase:" << str << endl;
    //str.begin(), str.end()返回的是迭代器
    str.erase(str.begin() + 1, str.end() - 1);
    cout << "Erase:" << str << endl;

    str = "abcdefabc";
    //正向匹配
    cout << "Find:" << str.find("abc") << endl;
    //逆向匹配
    cout << "Rfind:" << str.rfind("abc") << endl;

    //拷贝从0开始的4个字符
    string copy_str;
    copy_str.assign(str, 0, 4);
    cout << "Copy:" << copy_str << endl;

    //比较字符串, 大于返回1, 相等返回0, 小于返回-1
    string cmp_str1 = "abc";
    string cmp_str2 = "abb";
    int cmp_result = cmp_str1.compare(cmp_str2);
    cout << "Compare:" << cmp_result << endl;

    //把整数写入到字符数组中
    char num_to_char[5];
    sprintf(num_to_char, "%d", 2333);
    cout << "Num_to_char:" << num_to_char << endl;

    //string转化为int, 标准库<cstdlib>
    string str_to = "1.314";
    int str_to_int_result = atoi(str_to.c_str());
    cout << "Str_to_int.c_str():" << str_to.c_str() << endl;
    cout << "Str_to_int_result:" << str_to_int_result << endl;

    //string转化为float
    double str_to_float_result = atof(str_to.c_str());
    cout << "Str_to_float_result:" << str_to_float_result << endl;

    //int转化为string, 语言标准需设置成C++11
    int int_to_str = 20;
    cout << "To_String:" << to_string(int_to_str) << endl;

    // stoll 此函数将在函数调用中作为参数提供的字符串转换为long int
    string s = "1234";
    cout << stoll(s) << endl;
}
