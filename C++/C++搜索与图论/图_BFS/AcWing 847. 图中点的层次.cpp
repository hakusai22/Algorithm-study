#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 13:40
*/



const int N = 1e5 + 10;

int h[N], e[N], idx, ne[N];
int d[N]; //存储每个节点离起点的距离  d[1]=0
int n, m; //n个节点m条边
int q[N]; //存储层次遍历序列 0号节点是编号为1的节点

void add(int a, int b) {
    e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}

int bfs() {
    int hh = 0, tt = 0;

    q[0] = 1; //0号节点是编号为1的节点

    memset(d, -1, sizeof d);

    d[1] = 0; //存储每个节点离起点的距离

    //当我们的队列不为空时
    while (hh <= tt) {
        //取出队列头部节点
        int t = q[hh++];

        //遍历t节点的每一个邻边
        for (int i = h[t]; i != -1; i = ne[i]) {
            int j = e[i];
            //如果j没有被扩展过
            if (d[j] == -1) {
                d[j] = d[t] + 1; //d[j]存储j节点离起点的距离，并标记为访问过
                q[++tt] = j; //把j结点 压入队列
            }
        }
    }

    return d[n];
}

int main() {
    cin >> n >> m;
    memset(h, -1, sizeof h);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        add(a, b);
    }

    cout << bfs() << endl;
}


