package _03_21

var target int
var h map[int]bool
var res bool

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findTarget(root *TreeNode, k int) bool {
	h = map[int]bool{}
	res = false
	target = k
	dfs(root)
	return res
}

func dfs(root *TreeNode) {
	if root != nil {
		dfs(root.Left)
		if h[target-root.Val] {
			res = true
			return
		}
		h[root.Val] = true
		dfs(root.Right)
	}
}
