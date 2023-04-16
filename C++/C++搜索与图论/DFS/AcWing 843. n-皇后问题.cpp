#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 10:23
*/


const int N = 20;
int n;
bool col[N], dg[N], udg[N];
char g[N][N];

void dfs(int u) {
    if (u == n) {
        for (int i = 0; i < n; ++i) {
            puts(g[i]);
        }
        puts("");
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (!col[i] && !dg[u + i] && !udg[n - u + i]) {
            col[i] = dg[u + i] = udg[n - u + i] = true;
            g[u][i] = 'Q';
            dfs(u + 1);
            g[u][i] = '.';
            col[i] = dg[i + u] = udg[n - u + i] = false;
        }
    }
}


int main() {

    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            g[i][j] = '.';
        }
    }
    dfs(0);
    return 0;
}
