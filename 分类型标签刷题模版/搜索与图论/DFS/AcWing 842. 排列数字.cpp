#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 10:10
*/


const int N = 10;
int path[N];
int state[N];
int n;

void dfs(int u) {
    if (u > n) {
        for (int i = 1; i <= n; ++i) {
            cout << path[i] << " ";
        }
        cout << endl;
    }

    for (int i = 1; i <= n; ++i) {
        if (!state[i]) {
            path[u] = i;
            state[i] = 1;
            dfs(u + 1);
            state[i] = 0;
        }
    }
}


int main() {
    cin >> n;
    dfs(1);
}
