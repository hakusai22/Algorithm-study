#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/06 15:48
*/

/**
     让最大值最小，容易想到二分答案。接下来考虑如何检验二分出来的答案 x
     我们从左到右枚举每座房子，同时记录上一次抢夺的房子的下标j
     如果当前房子可以抢夺（价值小于等于 x，且不和 j 相邻）就进行抢夺
     因为越早抢夺，留给右边的抢夺机会就越多。最后检查是否抢夺了至少 k 座房子即可。
     复杂度 O(nlogA)
     https://leetcode.cn/problems/house-robber-iv/
 */

class Solution {
public:
    int minCapability(vector<int> &nums, int K) {
        int n = nums.size();

        // 检查二分的答案 X 是否合法
        auto check = [&](int X) {
            int cnt = 0;
            // 从左到右枚举每座房子，能抢就抢
            // j 是上一次抢夺的下标
            for (int i = 0, j = -2; i < n; i++)
                if (nums[i] <= X && i - j > 1) {
                    cnt++;
                    j = i;
                }
            return cnt >= K;
        };

        int head = nums[0], tail = nums[0];
        for (int x: nums) {
            head = min(head, x);
            tail = max(tail, x);
        }

        // 二分答案
        while (head < tail) {
            int mid = (head + tail) >> 1;
            if (check(mid)) tail = mid;
            else head = mid + 1;
        }
        return head;
    }
};


