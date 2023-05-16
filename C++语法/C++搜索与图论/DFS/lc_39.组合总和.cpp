#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/18 17:13
*/


class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;

    void backtracking(vector<int> &candidates, int target, int sum, int startIndex) {
        if (sum == target) {
            result.push_back(path);
            return;
        }

        // 如果 sum + candidates[i] > target 就终止遍历
        for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++) {
            sum += candidates[i];
            path.push_back(candidates[i]);
            backtracking(candidates, target, sum, i);
            sum -= candidates[i];
            path.pop_back();

        }
    }

public:
    vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
        result.clear();
        path.clear();
        sort(candidates.begin(), candidates.end()); // 需要排序
        backtracking(candidates, target, 0, 0);
        return result;
    }
};

