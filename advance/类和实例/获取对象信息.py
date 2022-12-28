#type()函数可以判断对象类型、函数类型

from  test_module import*
print(type(a))
print(type('123'))


#使用isinstance 判断class的类型
aa=a(1,2)
print(isinstance(aa,object))

#使用isinstance 判断类型
print(isinstance((1,2,3),(tuple)))


#dir() 获得一个对象的所有属性和方法，它返回一个list
#其中，__xxx___的属性和方法在python中都是有特殊用途的
print(dir(aa))





