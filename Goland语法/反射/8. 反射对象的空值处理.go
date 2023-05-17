package main

import (
	"fmt"
	"reflect"
)

type haojiahuo struct {
	Name string
	Age  int
}

func main() {
	var a *int                              //声明一个变量a为nil的空指针
	fmt.Println(reflect.ValueOf(a).IsNil()) //判断是否为nil 返回true

	//当reflect.Value不包含任何信息，值为nil的时候IsValid()就返回false
	fmt.Println(reflect.ValueOf(nil).IsValid())
}
