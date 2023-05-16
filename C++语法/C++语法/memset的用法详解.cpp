#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wink
    @Time    : 2023/04/03 11:50
*/


int main() {
    char a[4];
    memset(a, 'a', sizeof(a));
    for (char i: a) {
        cout << i << " ";
    }

    for (const auto &item: a) {
        cout << item << " ";
    }

    int b[4];
    memset(b, 0x3f3f3f3f, sizeof(b));
    for (int i : b) {
        cout << i << " ";
    }
    return 0;
}

