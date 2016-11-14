##def up(x):
#	n = len(x)
#	l = []
#	s = ''
#	for i in range(n):
#		if i == 0:
#			l.append(x[i].upper())
#			s = s + l[i]
#			continue
#		l.append(x[i])
#		s = s + l[i]
#	return s

#print up('abc')

def upper(x):
	return x[0:1].upper() + x[1:].lower()



l2 = ['adam', 'LISA', 'barT']

print map(upper,l2)
