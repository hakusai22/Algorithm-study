package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := 36

	fmt.Println(reflect.TypeOf(a))  //通过反射获取变量a的type类型对象 int
	fmt.Println(reflect.ValueOf(a)) //通过反射获取变量a的value类型对象 36
}
