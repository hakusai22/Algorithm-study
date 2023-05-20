package main

import "sort"

func answerQueries(nums, queries []int) []int {
	sort.Ints(nums)
	//原地前缀和
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	//在前缀和数组中进行搜索小于等于q的下标
	for i, q := range queries {
		queries[i] = sort.SearchInts(nums, q+1)
	}
	return queries
}
