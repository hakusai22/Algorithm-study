package main

import (
	"fmt"
	"io/ioutil"
)

/**
错误和异常不同，错误是在程序中正常存在的，可以预知的失败在意料之中。
而异常通常指在不应该出现问题的地方出现问题，比如空指针，这在人们的意料之外。
go语言没有 try......catch 这样的方式来捕获异常所以Go定义属于自己的一种错误类型，用error表示错误。
*/

// 例如：我们在读取一个不存在的文件时候。如果文件正常存在就返回文件的内容，否则就返回一个err信息。
func main() {
	//使用io/ioutil包下的读取文件方法
	conent, err := ioutil.ReadFile("test.txt")
	if err != nil {
		fmt.Println(err) //打印错误信息
	} else {
		fmt.Println(string(conent)) //返回正常信息
	}
}
