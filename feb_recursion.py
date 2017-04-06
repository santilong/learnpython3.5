#!/usr/bin/env python
#coding: utf-8

def feb(n):
	if n < 0:
		print("输入有误")
	if n == 1 or n == 2:
		return 1
	else:
		return feb(n-1) + feb(n-2)

number = int(input("请输入一个正整数："))
feb1 = feb(number)
print(feb1)
	
