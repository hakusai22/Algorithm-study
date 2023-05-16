/*
 * @Author: hakusai
 * @Date: 2023-05-15 08:30:39
 * @LastEditTime: 2023-05-15 08:52:30
 */
package main

func maxEqualRowsAfterFlips(matrix [][]int) (ans int) {
	cnt := map[[5]uint64]int{}
	for _, row := range matrix {
		r := [5]uint64{}
		for i, x := range row {
			r[i/64] |= uint64(x^row[0]) << (i % 64)
		}
		cnt[r]++
	}
	for _, c := range cnt {
		ans = max(ans, c)
	}
	return ans
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
