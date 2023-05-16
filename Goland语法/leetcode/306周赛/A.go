package main

// 把最大值直接保存在 3\times 33×3 矩阵的左上角
func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	for i, row := range grid[:n-2] {
		for j := 0; j < n-2; j++ {
			mx := 0
			for _, r := range grid[i : i+3] {
				for _, v := range r[j : i+3] {
					mx = max(mx, v)
				}
			}
			row[j] = mx
		}
		grid[i] = row[:n-2]
	}
	return grid[:n-2]
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
