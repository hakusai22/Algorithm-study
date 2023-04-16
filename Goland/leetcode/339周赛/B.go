package _39周赛

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/02 23:29
*/

func findMatrix(a []int) (ans [][]int) {
	cnt := map[int]int{}
	for _, v := range a {
		cnt[v]++
	}
	for len(cnt) > 0 {
		b := []int{}
		for v := range cnt {
			b = append(b, v)
		}
		ans = append(ans, b)
		for _, v := range b {
			cnt[v]--
			if cnt[v] == 0 {
				delete(cnt, v)
			}
		}
	}
	return
}
