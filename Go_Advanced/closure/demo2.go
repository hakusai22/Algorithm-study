package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/14 16:32
*/

func main() {

	for i := 0; i < 3; i++ {
		func() {
			println(i) // 0, 1, 2
		}()
	}
	fmt.Println("------------")

	for i := 0; i < 3; i++ {
		f := func() {
			println(i) // 0, 1, 2
		}
		f()
	}
	fmt.Println("------------")

	var dummy [3]int
	for i := 0; i < len(dummy); i++ {
		println(i) // 0, 1, 2
	}

	fmt.Println("------------")
	var f func()
	for i := 0; i < len(dummy); i++ {
		f = func() {
			println(i)
		}
	}
	f() // 3

	fmt.Println("------------")

	for i := 0; i < len(dummy); {
		f = func() {
			println(i)
		}
		i++
	}
	f() // 3
}
