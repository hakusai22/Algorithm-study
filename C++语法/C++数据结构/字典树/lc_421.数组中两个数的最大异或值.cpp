#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/05 23:42
*/

class Solution {
public:
    int findMaximumXOR(vector<int> &nums) {
        int ans = 0;  // 处理到当前位时，高位的数值
        for (int i = 30; i >= 0; i--) {  // 处理每一位  // for循环里面，我们不考虑整个数，而只关注某个数的前几位
            // 开始预处理，将每个数的前几位放入哈希表
            unordered_set<int> se;
            for (int &t: nums) {
                se.insert(t >> i);
            }
            for (const auto &item: se) {
                cout << item;
            }
            // 我们希望这一位也是1，假设前三位是101，那么我们希望前四位是1011，而1011 = (101 << 1) + 1
            int wantBe = (ans << 1) + 1;
            bool found = false;
            for (int &t: nums) {
                if (se.count(wantBe ^ (t >> i))) {  // 假设 wantBe ^ (t的前几位) = X，那么X ^ (t的前几位)就是wantBe
                    found = true;
                    break;
                }
            }
            ans = found ? wantBe : wantBe - 1;  // 如果没找到，那么这一位只好是0，也就是“1010 = 1011 - 1”
        }
        return ans;
    }
};

