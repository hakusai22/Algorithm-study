/*
 * @Author: hakusai
 * @Date: 2023-05-20 20:39:15
 * @LastEditTime: 2023-05-20 22:06:05
 * @Description: 
 */

import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    private int ans;

    public int maxSumBST(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int[] dfs(TreeNode node) {
        if (node == null)
            return new int[] { Integer.MAX_VALUE, Integer.MIN_VALUE, 0 };
        int[] left = dfs(node.left); // 递归左子树
        int[] right = dfs(node.right); // 递归右子树
        int x = node.val;
        if (x <= left[1] || x >= right[0]) // 不是二叉搜索树
            return new int[] { Integer.MIN_VALUE, Integer.MAX_VALUE, 0 };
        int s = left[2] + right[2] + x; // 这棵子树的所有节点值之和
        ans = Math.max(ans, s);
        return new int[] { Math.min(left[0], x), Math.max(right[1], x), s };
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}
