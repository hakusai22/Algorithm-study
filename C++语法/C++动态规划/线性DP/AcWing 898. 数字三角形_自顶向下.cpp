#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/01 11:05
*/
/**
 * """
    给定一个如下图所示的数字三角形，从顶部出发，
    在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，
    一直走到底层，要求找出一条路径，使路径上的数字的和最大。
                    7
                  3   8
                8   1   0
              2   7   4   4
            4   5   2   6   5
"""
 */

const int N = 5e2 + 5;
int n, a[N][N], dp[N][N], res = -2e9;

signed main() {
    memset(dp, -0x3f, sizeof dp);
    dp[0][0] = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cin >> a[i][j];
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j];
        }
    }
    for (int i = 1; i <= n; i++) res = max(res, dp[n][i]);
    cout << res << endl;
}
