#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/01 17:32
*/


const int N = 11, M = 1001;
int n, m, f[N][N];
char str[M][N];

int distans(char a[], char b[]) {
    int l1 = strlen(a + 1), l2 = strlen(b + 1);
    for (int i = 1; i <= l1; i++)
        for (int j = 1; j <= l2; j++) {
            f[i][j] = min(f[i - 1][j], f[i][j - 1]) + 1;
            if (a[i] == b[j]) f[i][j] = min(f[i][j], f[i - 1][j - 1]);
            else f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1);
        }
    return f[l1][l2];
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= 10; i++) f[i][0] = f[0][i] = i;
    for (int i = 0; i < n; i++) scanf("%s", str[i] + 1);
    while (m--) {
        char s[N];
        int limit, res = 0;
        scanf("%s%d", s + 1, &limit);
        for (int i = 0; i < n; i++)
            res += distans(str[i], s) <= limit;
        printf("%d\n", res);
    }
}
