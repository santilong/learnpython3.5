#!/usr/bin/env python
#-*- coding: utf8 -*-
try:
	print 'A'
except:
	print 'B'
else:
	print 'C'


while True:
	try:
		x = input("first num:")
		y = input("second num:")
		value = x / y
		print "x / y is %d : " % value
	except Exception, e:
		print e
	else:
		break
	
