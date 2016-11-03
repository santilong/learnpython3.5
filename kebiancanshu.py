#-*- coding: utf-8 -*-

###用列表或元组实现可变参数效果；
def calc(number):
	sum = 0
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

#print(calc([1,2,3]))

###可变参数:*number
def calckb(*number):
	sum = 0
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

print(calckb(1,3,5,7))
