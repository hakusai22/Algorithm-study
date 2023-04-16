#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/18 17:35
*/



class Solution {
public:
    vector<vector<int>> ans;
    int an[10000];

    vector<vector<int>> permute(vector<int> &nums) {
        vector<int> num;
        memset(an, 1, sizeof(an));
        dfs(num, nums);
        return ans;
    }

    void dfs(vector<int> &num, vector<int> &nums) {
        if (num.size() == nums.size()) {
            ans.push_back(num);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (an[i]) {
                num.push_back(nums[i]);
                an[i] = 0;
                dfs(num, nums);
                num.pop_back();
                an[i] = 1;
            }
        }
    }

};
