#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/19 17:59
*/

/*
  isalpha() / isdigit() / isalnum() / islower() / isupper()参数为字符型变量，
  分别用于判断字符是否为字母 / 数字(注意是字符型) / 字母或数字 / 小写字母 / 大写字母。如果是，返回非0；如果不是，返回0。
 */

int main() {


    char ch = 'Z';
    cout << "isalpha: " << isalpha(ch) << endl;
    cout << "isdigit: " << isdigit(ch) << endl;
    cout << "isalnum: " << isalnum(ch) << endl;
    cout << "islower: " << islower(ch) << endl;
    return 0;
}
