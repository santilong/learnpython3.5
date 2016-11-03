#-*- coding: utf-8 -#-
def calc(*args):
	sum = 0
	for n in args:
		sum = sum + n * n
	return sum

num = list(input('Input the numbers: '))
print(calc(*num))
