#include <bits/stdc++.h>

using namespace std;
#define int long long

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 11:36
*/

string s, state, ended = "12345678x";
int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};

int bfs() {
    queue<string> q;
    unordered_map<string, int> d;
    q.push(state);
    d[state] = 0;
    while (!q.empty()) {
        auto t = q.front();
        q.pop();
        if (t == ended) return d[t];
        int k = t.find('x'), dist = d[t];
        int x = k / 3, y = k % 3;
        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i], yy = y + dy[i];
            if (xx >= 0 && yy >= 0 && xx < 3 && yy < 3) {
                swap(t[xx * 3 + yy], t[k]);
                if (!d.count(t)) {
                    d[t] = dist + 1;
                    q.push(t);
                }
                swap(t[xx * 3 + yy], t[k]);
            }
        }
    }
    return -1;
}

signed main() {
    for (int i = 0; i < 9; i++) {
        cin >> s;
        state += s;
    }
    cout << bfs() << endl;
}

