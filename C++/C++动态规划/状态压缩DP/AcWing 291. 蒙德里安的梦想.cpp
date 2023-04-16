#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/03 15:55
*/

/**
 * """
    求把 N×M 的棋盘分割成若干个 1×2 的长方形，有多少种方案。
    例如当 N=2，M=4 时，共有 5种方案。当 N=2，M=3 时，共有 3种方案。

    1. 所谓的状态压缩DP，就是用二进制数保存状态。为什么不直接用数组记录呢？因为用一个二进制数记录方便作位运算
    2. 本题等价于找到所有横放 1 X 2 小方格的方案数，因为所有横放确定了，那么竖放方案是唯一的。
    3. 用f[i][j]记录第i列第j个状态。j状态位等于1表示上一列有横放格子，本列有格子捅出来。转移方程很简单，本列的每一个状态都由上列所有“合法”状态转移过来f[i][j] += f[i - 1][k]
    4. 两个转移条件： i 列和 i - 1列同一行不同时捅出来 ； 本列捅出来的状态j和上列捅出来的状态k求或，得到上列是否为奇数空行状态，奇数空行不转移。
    5. 初始化条件f[0][0] = 1，第0列只能是状态0，无任何格子捅出来。返回f[m][0]。第m + 1列不能有东西捅出来。
"""
 */

const int N = 12, M = 1 << N;
int st[M];
long long f[N][M];


int main() {
    int n, m;
    while (cin >> n >> m && (n || m)) {

        for (int i = 0; i < 1 << n; i++) {
            int cnt = 0;
            st[i] = true;
            for (int j = 0; j < n; j++)
                if (i >> j & 1) {
                    if (cnt & 1) st[i] = false; // cnt 为当前已经存在多少个连续的0
                    cnt = 0;
                } else cnt++;
            if (cnt & 1) st[i] = false; // 扫完后要判断一下最后一段有多少个连续的0
        }

        memset(f, 0, sizeof f);
        f[0][0] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 0; j < 1 << n; j++)
                for (int k = 0; k < 1 << n; k++)
                    if ((j & k) == 0 && (st[j | k]))
                        // j & k == 0 表示 i 列和 i - 1列同一行不同时捅出来
                        // st[j | k] == 1 表示 在 i 列状态 j， i - 1 列状态 k 的情况下是合法的.
                        f[i][j] += f[i - 1][k];
        cout << f[m][0] << endl;
    }
    return 0;
}

