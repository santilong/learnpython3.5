#!/usr/bin/evn python3
#-*- coding: utf-8 -*-
names = ['Bart','Lisa','Adam']
n = 0
print('result of for:\n')
for name in names:
	print('Hello,%s.' % name)

print('\n')
print('result of while:\n')
while n < 3:
	print('Hello,%s' % names[n])
	n = n + 1

