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

    使用记忆化数组 记录每个点的最大滑动长度
    遍历每个点作为起点
    然后检测该点四周的点 如果可以滑动到其他的点
    那么该点的最大滑动长度 就是其他可以滑到的点的滑动长度+1
    dp[i][j] = max(dp[i][j-1], dp[i][j+1],dp[i-1][j],dp[i+1][j])

    由于滑雪是必须滑到比当前低的点 所以不会存在一个点多次进入的问题
    如果该点的dp[][] 不为初始化值 那么就说明计算过 不必再次计算。
"""
 */


const int N = 310;
int R, C;

int arr[N][N];
int dp[N][N];

int maxlen = -1;

int addx[] = {1, -1, 0, 0};
int addy[] = {0, 0, 1, -1};

int Dfs(int x, int y) {
    if (dp[x][y] != 0) return dp[x][y];

    for (int i = 0; i < 4; i++) {
        int newx = x + addx[i];
        int newy = y + addy[i];

        if (newx >= 0 && newx < R && newy >= 0 && newy < C &&
            arr[newx][newy] < arr[x][y]) {
            dp[x][y] = max(dp[x][y], Dfs(newx, newy) + 1);
        }
    }
    return dp[x][y];
}

int main() {
    ios::sync_with_stdio(false);

    cin >> R >> C;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            int len = Dfs(i, j);
            maxlen = max(maxlen, len);
        }
    }
    cout << maxlen + 1 << endl;
    return 0;
}

