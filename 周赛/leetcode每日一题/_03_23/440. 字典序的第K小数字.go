package _03_23

func findKthNumber(n int, k int) int {
	var dfs func(l, r int) int
	dfs = func(l, r int) int {
		if l > n {
			return 0
		}
		if r > n {
			r = n
		}
		return r - l + 1 + dfs(l*10, r*10+9)
	}

	cur := 1
	k--
	for k > 0 {
		cnts := dfs(cur, cur)
		if cnts <= k {
			k -= cnts
			cur++
		} else {
			k--
			cur *= 10
		}
	}
	return cur
}
