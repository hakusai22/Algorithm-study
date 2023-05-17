package main

import (
	"fmt"
	"reflect"
)

/**
使用反射修改值的方法

SetInt(x) 设置值为x, 类型必须是int类型。
SetUint(x) 设置值为x, 类型必须是uint类型。
SetFloat(x) 设置值为x, 类型必须是float32或者float64类型。
SetBool(x) 设置值为x, 类型必须是bool类型。
SetBytes(x) 设置值为x, 类型必须是[]Byte类型。
SetString(x) 设置值为x, 类型必须是string类型。
*/
func main() {
	//声明变量a
	a := 100
	fmt.Printf("a的内存地址为：%p\n", &a)
	//获取变量a的反射类型reflect.Value 的地址
	rf := reflect.ValueOf(&a)
	fmt.Println("通过反射获取变量a的地址:", rf)

	//获取a的地址的值
	rval := rf.Elem()
	fmt.Println("反射a的值：", rval)

	//修改a的值
	rval.SetInt(200)
	fmt.Println("修改之后反射类型的值为：", rval.Int())

	//原始值也被修改
	fmt.Println("原始a的值也被修改为：", a)
}
