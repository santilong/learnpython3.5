#!/usr/bin/env python

from random import *

num = input('how many dice? ')
sides = input('how many sides per dice? ')

sum = 0

for i in range(num): sum += randrange(sides) + 1
print 'The result is %d' % sum
