package main

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/14 17:13
*/

func main() {

	var funcSlice []func()
	for i := 0; i < 3; i++ {
		println(&i)
		funcSlice = append(funcSlice, func() {
			println(i)
		})
	}
	// 这三个函数引用的都是同一个变量（i）的地址，所以之后 i 递增，解引用得到的值也会递增，所以这三个函数都会输出 3。
	for j := 0; j < 3; j++ {
		funcSlice[j]() // 3, 3, 3
	}

	var funcSlice1 []func()
	for i := 0; i < 3; i++ {
		func(i int) {
			println(&i)
			funcSlice1 = append(funcSlice1, func() {
				println(i)
			})
		}(i)

	}
	for j := 0; j < 3; j++ {
		funcSlice1[j]() // 0, 1, 2
	}
}
