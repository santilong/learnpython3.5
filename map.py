###map函数的使用，map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
###此脚本编译器可以正常运行，但是python3 map.py就出错；


def f(x):
	return x * x

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = map(f,l1)
print(z)
