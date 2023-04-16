#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/03 17:17
*/

/**
 """
    给定一个 R行 C列的矩阵，表示一个矩形网格滑雪场。
    矩阵中第 i行第 j列的点表示滑雪场的第 i行第 j列区域的高度。
    一个人从滑雪场中的某个区域内出发，每次可以向上下左右任意一个方向滑动一个单位距离。
    当然，一个人能够滑动到某相邻区域的前提是该区域的高度低于自己目前所在区域的高度。
    // 25出发 从高到低转圈 1结束 经过25个点
    1  2  3  4  5
    16 17 18 19 6
    15 24 25 20 7
    14 23 22 21 8
    13 12 11 10 9
"""
 */


const int N = 310;
int n, m;
int maxlen = -1;
vector<vector<int>> vv;

int addx[] = {1, -1, 0, 0};
int addy[] = {0, 0, 1, -1};

void dfs(int x, int y, int len) {
    if (len > maxlen) maxlen = len;

    for (int i = 0; i < 4; i++) {
        int newx = x + addx[i];
        int newy = y + addy[i];

        if (newx >= 0 && newx < n && newy >= 0 && newy < m &&
            vv[newx][newy] < vv[x][y]) {
            dfs(newx, newy, len + 1);
        }
    }
}


int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        vector<int> v;
        vv.push_back(v);
        for (int j = 0; j < m; j++) {
            int t = 0;
            cin >> t;
            vv[i].push_back(t);
        }
    }


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int len = 0;
            dfs(i, j, len);
        }
    }

    cout << maxlen + 1 << endl;

    return 0;
}


