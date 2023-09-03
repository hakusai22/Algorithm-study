/*
 * @Author: hakusai
 * @Date: 2023-04-22 18:00:29
 * @LastEditTime: 2023-04-22 21:51:59
 */
package main

import "fmt"

func supplyWagon(a []int) (ans []int) {
	m := len(a) / 2
	for len(a) > m {
		mii := 1
		for i := 1; i < len(a); i++ {
			if a[i]+a[i-1] < a[mii]+a[mii-1] {
				mii = i
			}
		}
		a[mii-1] += a[mii]
		a = append(a[:mii], a[mii+1:]...)
	}
	return a
}

func main() {
	fmt.Println("hello")
	a := []int{1, 2, 3, 4, 5}
	fmt.Println(supplyWagon(a))
}
