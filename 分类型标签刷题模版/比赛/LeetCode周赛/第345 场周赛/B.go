package main

import "fmt"

/*
 * @Author: hakusai
 * @Date: 2023-05-14 12:37:30
 * @LastEditTime: 2023-05-14 12:48:01
 */

func doesValidArrayExist(derived []int) bool {
	xor := 0
	for _, x := range derived {
		xor ^= x
	}
	return xor == 0
}

func main() {
	var aa = [...]int{1, 1, 0}
	fmt.Println(doesValidArrayExist(aa[:]))
}
