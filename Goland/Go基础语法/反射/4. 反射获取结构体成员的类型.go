package main

import (
	"fmt"
	"reflect"
)

/**
任意一个类型通过反射 reflect.TypeOf() 获取反射类型对象，
通过反射类型对象可以获取当前结构具体是什么样的类型，
如果是结构体时，可以通过反射类型对象的NumField()和Field()方法获得结构体的详细成员信息。
*/
type mystruct struct {
	Name string
	Sex  int
	Age  int `json:"age"`
}

func main() {

	typeofmystruct := reflect.TypeOf(mystruct{})

	fmt.Println(typeofmystruct)
	fieldnum := typeofmystruct.NumField() //获取结构体成员字段的数量
	fmt.Println(fieldnum)

	for i := 0; i < fieldnum; i++ {
		fieldname := typeofmystruct.Field(i) //索引对应的字段信息
		fmt.Println(fieldname)
		fmt.Println(fieldname.Type)
		fmt.Println(fieldname.Name)
		fmt.Println(fieldname.Index)
	}
	name, err := typeofmystruct.FieldByName("Name") //根据指定的字符串返回对应的字段信息
	fmt.Println(name, err)

}
