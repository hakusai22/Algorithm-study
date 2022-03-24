package c._03_21;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    List<Integer> list=new ArrayList<>();
    public boolean findTarget(TreeNode root, int k) {
        dfs(root);
        Set<Integer> set=new HashSet<>();
        for(int v:list){
            if(set.contains(k-v)) return true;
            set.add(v);
        }
        return false;
    }
    public void dfs(TreeNode root){
        if(root==null) return;
        dfs(root.left);
        list.add(root.val);
        dfs(root.right);
    }
}