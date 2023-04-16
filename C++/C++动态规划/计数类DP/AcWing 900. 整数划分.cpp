#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/02 15:00
*/

/**
 """
    一个正整数 n 可以表示成若干个正整数之和，形如：n=n1+n2+…+nk ，其中 n1≥n2≥…≥nk,k≥1。
    我们将这样的一种表示称为正整数 n 的一种划分。
    现在给定一个正整数 n，请你求出 n 共有多少种不同的划分方法。

    f[i][j]表示所有总和是i，并且恰好表示成j个数的和的方案的数量
    此时集合的划分是：
        1.该方案中最小值是1  方案数等于舍弃该1后的方案数，因此此时的方案数是：f[i−1][j−1]
        2.该方案中最小值大于1 把每一个数都减去1后每一个数仍大于等于1，仍合法，因此此时方案数等于把当前每个数减1的方案数，即：f[i−j][j]
    状态转移方程：
        f[i][j]=f[i−1][j−1]+f[i−j][j];
"""
 */

const int N = 1010, mod = 1e9 + 7;

int n;
int a[N];
int f[N][N];//f[i][j]表示 总和是i，并且由j个数组成的方案数

int main() {
    cin >> n;

    f[0][0] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++)
            f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % mod;

    int res = 0;
    for (int i = 1; i <= n; i++) res += f[i][n];

    cout << res << endl;
    return 0;
}

