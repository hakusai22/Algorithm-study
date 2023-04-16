#include <bits/stdc++.h>

using namespace std;
#define int long long

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/01 13:27
*/


const int N = 1e3 + 5;
int n, m, dp[N][N];
char a[N], b[N];

signed main() {
    cin >> n >> m >> a + 1 >> b + 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            if (a[i] == b[j]) dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
        }
    cout << dp[n][m] << endl;
}

