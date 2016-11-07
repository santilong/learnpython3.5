###reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
###此脚本在编译器里正常运行，但是用python3 reduce.py报错  日她妈
def fn(x,y):
	return x * 10 + y
l1 = [1,3,5,7,9]

reduce(fn,l1)
