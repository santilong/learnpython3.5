#-*- coding: utf-8 -*-
###n的阶乘：fact(n) = n! = 1 X 2 X 3 X 4 X 5 X 6.....X (n-1) X n ==> (n-1)! X n ==> fact(n-1) X n
###但是n=1需要特殊处理；
def fact(n):
	if n == 1:
		return n
	return fact(n-1) * n

print(fact(100))
