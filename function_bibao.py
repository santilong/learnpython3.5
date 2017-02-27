#!/usr/bin/env python
#

x = 'from global'
def f1():
	y = 'from f1'
#	print x,y
	def f2():
		z = 'from f2'
		print y,z
	return f2
f1()
