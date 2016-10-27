#-*- coding: utf-8 -*-
#age = 20
age = input('请输入你的年龄：')    
age = int(age) 		###input返回的数据类型是str，str不能和整数比较，必须先把str转换成整数
if age <= 14:
    print('滚吧，小屁孩！')
elif age > 14 and age < 20:
    print('青少年！')
else:
    print("青年人！")

