class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()

        def dfs(root):
            if not root:
                return False
            else:
                if k - root.val in s:
                    return True
                s.add(root.val)
                if dfs(root.left) or dfs(root.right):
                    return True
            return False

        return dfs(root)