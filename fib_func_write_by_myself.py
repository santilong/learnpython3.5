#-*- coding: utf-8 -*-
def fibs(max):
        n, a, b = 1, 1, 1
        while n <= 2:
                #print(b)
		yield b
                n = n + 1
        while n <= max:
                c = a + b
                #print(c)
		yield c
                a = b
                b = c
                n = n + 1
       #return 'done'

for x in fibs(10):
	print(x)
