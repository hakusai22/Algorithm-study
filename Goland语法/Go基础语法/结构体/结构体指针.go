package main

import (
	"fmt"
)

//定义结构体
type Person struct {
	name    string
	age     int
	sex     string
	address string
}

func main() {
	p2 := Person{age: 20, address: "浙江杭州", name: "hakusai", sex: "男"}

	//1 使用结构体指针
	var p *Person
	p = &p2 //将p2 的地址赋给p
	fmt.Println(p)
	p.name = "黑乎乎" //修改p的值
	fmt.Println(p)
	fmt.Println(p2) //p2的值也被修改了

	//2 使用new 创建结构体指针
	pnew := new(Person)
	fmt.Println(pnew)
	pnew.address = "江西南昌"
	pnew.age = 23
	pnew.name = "伟子"
	pnew.sex = "男"
	fmt.Println(pnew)
}
