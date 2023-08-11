package main

/*
 * @Author: hakusai
 * @Date: 2023-08-11 15:46:34
 * @LastEditTime: 2023-08-11 16:37:07
 * @Description: https://github.com/hakusai22
 */

func diagonalSum(mat [][]int) int {
	row := len(mat)
	col := len(mat[0])
	ans := 0
	for i := 0; i < row; i++ {
		ans += mat[i][i] + mat[row-1-i][i]
	}
	if row%2 == 1 {
		ans -= mat[row/2][col/2]
	}
	return ans
}
