package main

import "strings"

func garbageCollection(garbage []string, travel []int) (ans int) {
	right := [3]int{}
	for i, s := range garbage {
		ans += len(s)
		for j, c := range "MPG" {
			if strings.ContainsRune(s, c) {
				right[j] = i
			}
		}
	}

	for _, r := range right {
		for _, t := range travel[:r] {
			ans += t
		}
	}
	return
}
