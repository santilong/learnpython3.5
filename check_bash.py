#!/usr/bin/env python
#
f1 = open('/tmp/passwd','r+')
l1 = f1.readlines()
def fn(x):
	if '/bin/bash' in x:
		return True
	else:
		return False

l2 = filter(fn,l1)
print l2
