#!/usr/bin/env python
#-*- coding: utf8 -*-

'''类的构造函数'''
class bird():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaaah...'
			self.hungry = False
		else:
			print "No,thanks"

'''子类中也定义了构造函数，那么超类中的构造函数就失效，除非在子类构造函数中调用或使用super()函数'''
class songbird(bird):
	def __init__(self):
		self.sound = 'gagaga'
	def sing(self):
		print self.sound

'''子类构造函数中调用超类构造函数'''
class songbird(bird):
	def __init__(self):
		self.sound = 'gagaga'
		bird.__init__(self)
	def sing(self):
		print self.sound

'''super()函数：只能在新式类中使用，新类就是class A(object)，经典类就是class A()，将当前类喝对象作为super函数的参数试用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法'''
class songbird2(bird):
	def __init__(self):
		super(songbird2,self).__init__()
		self.sound = 'gagaga'
	def sing(self):
		print self.sound



	
