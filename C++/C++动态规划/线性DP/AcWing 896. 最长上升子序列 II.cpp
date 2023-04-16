#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/01 11:20
*/


/**
    7
    3 1 2 1 8 5 6

    3 ----
    1 ----
    1 2 ----
    1 2 ----
    1 2 8 ----
    1 2 5 ----
    1 2 5 6 ----
    4
 */

const int N = 100010;

int n;
int a[N];
int q[N]; //使用q[]存储所有不同长度的上升子序列结尾的最小值

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int len = 0;
    for (int i = 0; i < n; i++) {
        int l = 0, r = len;
        // 进来一个数a[i]时，通过二分在q[]中找到最大的小于ai的数，就能够将ai接到该数的后面，即更新q[r + 1] = a[i]
        while (l < r) {
            int mid = l + r + 1 >> 1;
            if (q[mid] < a[i]) l = mid;
            else r = mid - 1;
        }
        len = max(len, r + 1);
        q[r + 1] = a[i];
    }

    printf("%d\n", len);

    return 0;
}


