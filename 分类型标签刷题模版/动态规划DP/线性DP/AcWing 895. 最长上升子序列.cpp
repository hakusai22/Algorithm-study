#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/01 11:12
*/

/**
 * 给定一个长度为 N 的数列，求数值严格单调递增的子序列的长度最长是多少。
     1≤N≤1000，
    −109≤数列中的数≤109

    状态表示：f[i]表示从第一个数字开始算，以w[i]结尾的最大的上升序列。(以w[i]结尾的所有上升序列中属性为最大值的那一个)
    状态计算（集合划分）：j∈(0,1,2,..,i-1), 在w[i] > w[j]时，
    f[i] = max(f[i], f[j] + 1)。
    有一个边界，若前面没有比i小的，f[i]为1（自己为结尾）。
    最后在找f[i]的最大值。
 */


const int N = 1010;

int n;
int w[N], f[N];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> w[i];

    int mx = 1;    // 找出所计算的f[i]之中的最大值，边算边找
    for (int i = 0; i < n; i++) {
        f[i] = 1;    // 设f[i]默认为1，找不到前面数字小于自己的时候就为1
        for (int j = 0; j < i; j++) {
            if (w[i] > w[j]) f[i] = max(f[i], f[j] + 1);    // 前一个小于自己的数结尾的最大上升子序列加上自己，即+1
        }
        mx = max(mx, f[i]);
    }

    cout << mx << endl;
    return 0;
}

