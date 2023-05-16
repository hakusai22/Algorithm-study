#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/03 16:10
*/


/**
 """
    给定一张 n 个点的带权无向图，点从 0∼n−1 标号，求起点 0 到终点 n−1 的最短 Hamilton 路径。
    Hamilton 路径的定义是从 0 到 n−1 不重不漏地经过每个点恰好一次。

    数据范围
     1≤n≤20
     0≤a[i,j]≤107

        用二进制来表示要走的所以情况的路径,这里用i来代替
        例如走0,1,2,4这三个点,则表示为:10111; 走0,2,3这三个点:1101;
        状态表示:f[i][j];
            集合:所有从0走到j,走过的所有点的情况是i的所有路径
            属性:MIN
            状态计算:如1中分析一致,0–>·····–>k–>j中k的所有情况
            状态转移方程:f[i][j]=min(f[i][j],f[i-(1<<j)][k]+w[k][j])
"""
 */

const int N = 20, M = 1 << N;

int f[M][N], w[N][N];//w表示的是无权图

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> w[i][j];

    memset(f, 0x3f, sizeof(f));//因为要求最小值，所以初始化为无穷大
    f[1][0] = 0;//因为零是起点,所以f[1][0]=0;

    for (int i = 0; i < 1 << n; i++)//i表示所有的情况
        for (int j = 0; j < n; j++)//j表示走到哪一个点
            if (i >> j & 1)
                for (int k = 0; k < n; k++)//k表示走到j这个点之前,以k为终点的最短距离
                    if (i >> k & 1)
                        f[i][j] = min(f[i][j], f[i - (1 << j)][k] + w[k][j]);//更新最短距离

    cout << f[(1 << n) - 1][n - 1] << endl;//表示所有点都走过了,且终点是n-1的最短距离
    //位运算的优先级低于'+'-'所以有必要的情况下要打括号
    return 0;
}

