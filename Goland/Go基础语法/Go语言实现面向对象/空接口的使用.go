package main

import "fmt"

// Test 空接口既然可以传任意类型，利用这个特性可以把空接口interface{}当做容器使用。
func Test() {
	//创建一个map类型 key为string val为空接口，这样值就可以存储任意类型了
	m := make(map[string]interface{})
	m["a"] = "zhangsan"
	m["b"] = 1.1
	m["c"] = true
	fmt.Println(m)
}

// Dictionary 字典结构
type Dictionary struct {
	data map[string]interface{} // 数据key为string值为interface{}类型
}

// GetData 获取值
func (d *Dictionary) GetData(key string) interface{} {
	return d.data[key]
}

// SetData 设置值
func (d *Dictionary) SetData(key string, value interface{}) {
	d.data[key] = value
}

// NewDict 创建一个字典
func NewDict() *Dictionary {
	return &Dictionary{
		data: make(map[string]interface{}), //map类型使用前需要初始化，所以需要使用make创建 防止空指针异常。
	}
}

func main() {
	// 创建字典实例
	dict := NewDict()
	// 添加数据
	dict.SetData("001", "第一条数据")
	dict.SetData("002", 3.1415)
	dict.SetData("003", false)
	// 获取值
	d := dict.GetData("001")
	fmt.Println(d)
}
