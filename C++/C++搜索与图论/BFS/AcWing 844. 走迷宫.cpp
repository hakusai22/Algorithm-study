#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 11:28
*/



typedef pair<int, int> PII;
const int N = 110;
int g[N][N];//存储地图
int f[N][N];//存储距离
int n, m;

void bfs(int a, int b)//广度优先遍历
{
    queue<PII> q;
    q.push({a, b});
    while (!q.empty()) {
        PII start = q.front();
        q.pop();
        g[start.first][start.second] = 1;
        int dx[4] = {0, 1, 0, -1}, dy[4] = {-1, 0, 1, 0};
        for (int i = 0; i < 4; i++)//往四个方向走
        {
            int x = start.first + dx[i], y = start.second + dy[i];
            if (g[x][y] == 0)//如果还没有走过
            {
                g[x][y] = 1;
                f[x][y] = f[start.first][start.second] + 1;//从当前点走过去，则距离等于当前点的距离+1.
                q.push({x, y});
            }

        }
    }
    cout << f[n][m];
}

int main() {
    memset(g, 1, sizeof(g));
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> g[i][j];
        }
    }
    bfs(1, 1);

}

