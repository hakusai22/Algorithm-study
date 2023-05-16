/*
 * @Author: hakusai
 * @Date: 2023-05-15 08:30:49
 * @LastEditTime: 2023-05-15 08:51:12
 */

import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        int ans = 0, n = matrix[0].length;
        var cnt = new HashMap<String, Integer>();
        for (var row : matrix) {
            var r = new char[n];
            for (int j = 0; j < n; j++)
                r[j] = (char) (row[j] ^ row[0]); // 翻转第一个数为 1 的行
            // merge() 方法会先判断指定的 key 是否存在，如果不存在，则添加键值对到 hashMap 中。
            // 如果 key 对应的 value 不存在，则返回该 value 值，如果存在，则返回通过 remappingFunction 重新计算后的值
            int c = cnt.merge(new String(r), 1, Integer::sum);
            ans = Math.max(ans, c);
        }
        return ans;
    }
}
