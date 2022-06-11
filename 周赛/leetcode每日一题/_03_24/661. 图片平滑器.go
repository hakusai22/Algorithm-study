package _03_24

func imageSmoother(img [][]int) [][]int {
	m, n := len(img), len(img[0])
	presum, ans := make([][]int, m+1), make([][]int, m)
	presum[0] = make([]int, n+1)
	for i := 0; i < m; i++ {
		presum[i+1] = make([]int, n+1)
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] - presum[i][j] + img[i][j]
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			di, ui, dj, uj := max(0, i-1), min(m, i+2), max(0, j-1), min(n, j+2)
			ans[i][j] = (presum[ui][uj] - presum[ui][dj] - presum[di][uj] + presum[di][dj]) / ((ui - di) * (uj - dj))
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
