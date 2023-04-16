#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/18 15:13
*/


class Solution {
public:
    vector<int> searchRange(vector<int> &nums, int target) {
        if (nums.empty()) return {-1, -1};

        int l = 0, r = nums.size() - 1; //二分范围
        while (l < r)                    //查找元素的开始位置
        {
            int mid = (l + r) / 2;
            if (nums[mid] >= target) r = mid;
            else l = mid + 1;
        }
        if (nums[r] != target) return {-1, -1};  //查找失败
        int L = r;
        l = 0, r = nums.size() - 1;     //二分范围
        while (l < r)                   //查找元素的结束位置
        {
            int mid = (l + r + 1) / 2;
            if (nums[mid] <= target) l = mid;
            else r = mid - 1;
        }
        return {L, r};
    }
};

