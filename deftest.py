def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
		#print("TypeError('bad operand type')")
	if x > 0:
		return x
	else:
		return -x
#x = input(': ')
#x = int(x)
print(my_abs(-100))
