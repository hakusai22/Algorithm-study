#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/31 11:01
*/

/*
    有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
    第 i 件物品的体积是 vi，价值是 wi。
    求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
    输出最大价值。
 */

const int N = 1005;

int v[N];
int w[N];
int f[N][N];  // f[i][j], j体积下前i个物品的最大价值


int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        cin >> v[i] >> w[i];
    }

    // 状态f[i][j]定义：前 i 个物品，背包容量 j下的最优解（最大价值）
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            //  当前背包容量装不进第i个物品，则价值等于前i-1个物品
            if (j < v[i]) {
                f[i][j] = f[i - 1][j];
            } else {
                // 能装，需进行决策是否选择第i个物品
                f[i][j] = max(f[i - 1][j], f[i - 1][j - v[i]] + w[i]);
            }
        }
    }
    cout << f[n][m] << endl;

    return 0;
}
