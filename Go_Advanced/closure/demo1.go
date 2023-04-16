package main

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/14 16:05
*/

func incr() func() int {
	var x int
	return func() int {
		x++
		return x
	}
}

func main() {

	i := incr()
	println(i()) // 1
	println(i()) // 2
	println(i()) // 3

	println(incr()())
	println(incr()())
	println(incr()())

	x := 1
	f := func() {
		println(x)
	}
	x = 2
	x = 3
	f() // 3

	y := 1
	func() {
		println(y) // 1
	}()
	y = 2
	y = 3
}
