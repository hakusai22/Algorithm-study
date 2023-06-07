
/*
 * @Author: hakusai
 * @Date: 2023-06-07 23:26:35
 * @LastEditTime: 2023-06-07 23:41:08
 * @Description: 
 */
import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        int ans = 0;
        int n = reward1.length;
        for (int i = 0; i < n; i++) {
            ans += reward2[i];
            reward1[i] -= reward2[i];
        }
        Arrays.sort(reward1);
        for (int i = 0; i < k; i++) {
            ans += reward1[n - i - 1];
        }
        return ans;
    }
}