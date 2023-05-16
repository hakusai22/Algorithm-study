package main

// 通过reflect.Type的Field()方法返回的StructField结构信息，
// 这个结构信息包含了成员字段的所有信息。这个结构的定义如下。

//type StructField struct {
//	Name string	        // 字段名
//	PkgPath string      // 字段路径
//	Type      Type      // 字段反射类型对象
//	Tag       StructTag // 字段的结构体标签
//	Offset    uintptr   // 字段在结构体中的相对偏移
//	Index     []int     // Tpye.FieldByIndex中的返回索引值
//	Anonymous bool      // 是否为匿名字段
//}
