package _39周赛

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/02 23:29
*/

func findTheLongestBalancedSubstring(s string) (ans int) {
	a := []int{}
	for i, n := 0, len(s); i < n; {
		st := i
		v := s[st]

		for ; i < n && s[i] == v; i++ {

		}
		a = append(a, i-st)
	}
	if s[0] == '1' {
		a = a[1:]
	}
	for i := 1; i < len(a); i += 2 {
		ans = max(ans, min(a[i], a[i-1])*2)
	}
	return
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
