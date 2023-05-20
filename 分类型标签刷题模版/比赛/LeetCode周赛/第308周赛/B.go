package main

func removeStars(s string) string {
	/*
		string 底层是一个包含多个字节（1字节=8bit）的集合。
		string 可以被拆分为一个包含多个字节的序列  byte
		string 可以被拆分为一个包含多个字符的序列  rune
	*/
	var st []rune
	for _, c := range s {
		if c == '*' {
			//切片操作
			st = st[:len(st)-1]
		} else {
			st = append(st, c)
		}
	}
	return string(st)

}
