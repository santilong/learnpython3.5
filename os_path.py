#!/usr/bin/env python
#
import os
import os.path

fn = '/tmp/os.test.txt'

if os.path.isfile(fn):
	f1 = open(fn,'a+')

while True:
	x = raw_input('Enter a entry : ')
	if x == 'q' or x == 'quit':
		break
	f1.write(x + '\n')
f1.flush()
f1.close()
