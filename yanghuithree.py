def three(max):
    l = []
    n = 2
    z = 1
   # while n <= 1:
   #     l.append(z)
   #     print(l)
   #     n = n + 1
    if n == 2:
        l.insert(0,z)
        l.insert(n,z)
        #l.insert(1,(l[0] + l[n]))	
        l[1:1] = l[0] + l[1]	
	print(l)
three(1)
