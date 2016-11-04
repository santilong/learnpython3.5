#-*- coding: utf-8 -*-

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b)
		yield b    ### print(b)改为yield b，函数就变成了一个生成器；
		a, b = b,a + b
		n = n + 1
	return 'done'
fib(10)



