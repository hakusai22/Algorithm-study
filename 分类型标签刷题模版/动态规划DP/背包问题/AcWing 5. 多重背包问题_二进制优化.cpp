#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/31 17:23
*/

#define N 15000//N*logs(注意是以2为底，s的对数)=1000*log2000≈11000，开15000保险
#define M 2010
int n, m;
int v[N], w[N];
int dp[N];//01背包优化，用一维数组
int main() {
    int a, b, s;
    cin >> n >> m;
    int cnt = 0;//存储新物品的编号
    /*多重背包二进制优化操作*/
    for (int i = 1; i <= n; ++i) {
        cin >> a >> b >> s;//第i种物品的体积，价值，数量
        int k = 1;
        while (k <= s) {
            v[++cnt] = a * k, w[cnt] = b * k, s -= k, k *= 2;
        }
        if (s > 0) { v[++cnt] = a * s, w[cnt] = b * s; }
    }
    /*01背包*/
    n = cnt;//更新物品数量，此时为若干个新物品
    for (int i = 1; i <= n; ++i) {
        for (int j = m; j >= v[i]; --j)
            dp[j] = max(dp[j], dp[j - v[i]] + w[i]);
    }
    cout << dp[m] << endl;
    return 0;
}


