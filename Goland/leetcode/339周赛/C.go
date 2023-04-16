package _39周赛

import "sort"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/02 23:29
*/

func miceAndCheese(a []int, b []int, k int) (ans int) {
	type pair struct {
		x int
		y int
	}
	ps := make([]pair, len(a))
	for i, v := range a {
		ps[i] = pair{v, b[i]}
	}
	sort.Slice(ps, func(i, j int) bool {
		a, b := ps[i], ps[j]
		return a.x-a.y > b.x-b.y
	})

	for _, p := range ps[:k] {
		ans += p.x
	}
	for _, p := range ps[k:] {
		ans += p.y
	}

	return
}
