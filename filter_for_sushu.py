def su(x):
	n = 0
	for i in range(1,x + 1):
		if x % i == 0:
			n = n + 1
	if n == 2:
		return x
print filter(su,range(101))

