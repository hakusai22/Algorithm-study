#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/02 14:37
*/

/**
 """
    题意：合并 N 堆石子，每次只能合并相邻的两堆石子，求最小代价
    关键点：最后一次合并一定是左边连续的一部分和右边连续的一部分进行合并

    状态表示：f[i][j] 表示将 i 到 j 这一段石子合并成一堆的方案的集合，
    属性 Min
    前缀和数组 a[i]=a[i−1]+x[i] x[i-j]=a[j]−a[i−1]
    状态转移方程式:
        f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]+a[j]−a[i−1])
    枚举顺序：
        很明显，长的区间由短的区间合并而成
        所以先枚举区间长度 len 接着枚举左端点 l(右端点由左端点和区间长度去确定)
        最后枚举分段点 k，计算 dp 方程
"""
 */

const int N = 3e2 + 5;
int n, dp[N][N], s[N], x;

signed main() {
    cin >> n;
    //前缀和
    for (int i = 1; i <= n; i++) {
        cin >> x;
        s[i] += s[i - 1] + x;
    }
    for (int len = 2; len <= n; len++) { //枚举len
        for (int l = 1; l + len - 1 <= n; l++) { //枚举左端点
            int r = l + len - 1; //计算右端点
            dp[l][r] = 1e9; //初始化f[i][j]
            for (int k = l; k < r; k++) { //枚举k
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + s[r] - s[l - 1]);
            }
        }
    }
    cout << dp[1][n] << endl;
}


