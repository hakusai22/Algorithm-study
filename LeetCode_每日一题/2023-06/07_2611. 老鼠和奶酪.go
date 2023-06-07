/*
 * @Author: hakusai
 * @Date: 2023-06-07 23:26:40
 * @LastEditTime: 2023-06-07 23:43:41
 * @Description:
 */
package main

import "sort"

func miceAndCheese(reward1 []int, reward2 []int, k int) (ans int) {
	for i, x := range reward2 {
		ans += x
		reward1[i] -= x
	}
	sort.Ints(reward1)
	n := len(reward1)
	for i := 0; i < k; i++ {
		ans += reward1[n-i-1]
	}
	return
}
