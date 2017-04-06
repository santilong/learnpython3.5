#!/usr/bin/env python
#coding: utf-8

def feb(n):
	if n < 1:
		print("输入错误!")
		return 1
	n1 = 1
	n2 = 1
	n3 = 1
	while (n-2) > 0:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		n -= 1
	return n3
number = int(input("请输入一个正整数："))
feb1 = feb(number)
print(feb1)	



