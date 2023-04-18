'''
Author: hakusai
Date: 2023-04-18 00:17:15
LastEditTime: 2023-04-18 17:47:15
FilePath: /Algorithm-study/每日一题_Py3/2023-04/18_1026. 节点与其祖先之间的最大差值.py
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node: Optional[TreeNode],mn: int, mx:int)-> None:
            if node is None:
                return
            mn=min(mn,node.val)
            mx=max(mx,node.val)
            nonlocal ans
            ans=max(ans,node.val-mn,mx-node.val)
            dfs(node.left,mn,mx)    
            dfs(node.right,mn,mx)
        dfs(root,root.val,root.val)
        return ans