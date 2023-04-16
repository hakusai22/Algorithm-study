package main

import (
	"fmt"
	"reflect"
)

type Kind uint

const (
	Invalid       Kind = iota //非法类型
	Bool                      //布尔型
	Int                       //有符号整型
	Int8                      //有符号8位整型
	Int16                     //有符号16位整型
	Int32                     //有符号32位整型
	Int64                     //有符号64位整型
	Uint                      //无符号整型
	Uint8                     //无符号8位整型
	Uint16                    //无符号16位整型
	Uint32                    //无符号32位整型
	Uint64                    //无符号64位整型
	Uintptr                   //指针
	Float32                   //单精度浮点类型
	Float64                   //双精度浮点类型
	Complex64                 //64位复数类型
	Complex128                //128位复数类型
	Array                     //数组
	Chan                      //通道
	Func                      //函数
	Interface                 //接口
	Map                       //字典
	Ptr                       //指针
	Slice                     //切片
	String                    //字符串
	Struct                    //结构体
	UnsafePointer             //底层指针
)

type mystruct struct {
	Name string
	Sex  int
	Age  int `json:"age"`
}

func main() {

	typeofmystruct := reflect.TypeOf(mystruct{})

	fmt.Println(typeofmystruct.Name()) //获取反射类型对象  mystruct

	fmt.Println(typeofmystruct.Kind()) //获取反射类型种类  struct

}
