#!/usr/bin/env python3
#-*- coding: utf-8 -*-
T = 1.75
W = 80.5
R = W / T ** 2
if R < 18.5:
	print('太轻')
elif R >= 18.5 and R < 25:
	print('正常')
elif R >= 25 and R < 28:
	print('太重')
elif R >= 28 and R < 32:
	print('肥胖')
elif R >= 32:
	print('严重肥胖')
pass
print(R)

	


