package main

import (
	"fmt"
	"reflect"
)

/**
如果要取指针指向的具体的数据时通过* 来获取指针的值。
在反射中获取指针类型的对象时，通过reflect.Elem()方法获取这个指针指向的元素类型。
*/
type mystruct struct {
	Name string
	Sex  int
	Age  int `json:"age"`
}

func main() {

	typeofmystruct := reflect.TypeOf(&mystruct{})

	fmt.Println(typeofmystruct.Elem().Name()) //获取指针类型指向的元素类型的名称 mystruct

	fmt.Println(typeofmystruct.Elem().Kind()) //获取指针类型指向的元素类型的种类 struct

}
