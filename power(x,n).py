#-*- coding: utf-8 -*-
def power121(x,n):
	s = 1
	while n > 0:
		n = n -	1
		s = s * x
	return s

#m = power121(2,5)
x = int(raw_input("x: "))
n = int(raw_input("n: "))
print(power121(x,n))
