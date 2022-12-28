'''
#定义一个函数
#def 开头 函数名称 (入口参数) :
#函数体用同一缩进
#retun[表达式] 结束函数，返回一个或多个值，不带表达式等于返回NONE
#函数调用

def ab():
    a=input("please input a string:")
    print(a)
    return a

ab()

#定义一个空函数
def a():
    pass
a()
'''


'''
#参数传递 
# 数字、字符串、元组为不可变类型变量，传递的是变量的值，没有影响变量本身
#列表、字典为可变类型变量，传递是变量本身

b=2
def a(a):
    a=10
    print(a)

a(b)
print(b)


#参数检查
#函数返回多个参数，返回的是一个tuple，即元祖，不可改变

def ab(x):
    if not isinstance(x,(int,str)):
        print("error")
    if x>0 :
        print(x)
        return x,x+1;
    else:
      print(-x)
      return -x,-x-1;

c=ab(-2)
print(c)

'''

'''
#函数名是一个指向函数对象的引用，把函数名赋给一个变量，相当于给函数起了别名

a=abs
print(a(-2))

#python 内置转换函数
print(int (12.155))
print(float (12))
print(hex (12))
print(str(100))
print(list(range(1,5)))

'''


#参数类型：必备参数、默认参数、关键字参数、不定长参数
#位置参数 调用函数时，传入的两个值按照位置顺序依次赋值给
def power(x,n):
    s=1
    while(n>0):
        n=n-1
        s=s*x
        print(s)
    return s

#power(1,2)

#默认参数 在定义函数时，定义一个默认参数，简化函数的调用
#必选参数在前，默认参数在后
#默认参数的设置，一般设置为变化小的参数
#只有在与默认参数不同的参数时，才需要更新默认参数


def powerful(x,n=2):
    s=1
    while(n>0):
        n=n-1
        s=s*x
     
    print(s)
    return s

#powerful(2,3)
#powerful(2)


#默认参数必须指向不变的对象，否则肯定会改变

#可变参数（不定长参数）


#关键字参数 扩展函数功能 作为可选选项
def person(name,age,**other):
    print('name:',name,'age:',age,'other',other)

person('yfq',25,city='nj')




'''
#全局变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外面的拥有全局作用域
#局部变量只能在声明的函数内部访问
#全局变量可以在整个程序范围访问
#全局变量可以通过global声明在函数内部，在函数内部改变变量值

a=1

def hh(x):
    global a
    a=3
    print(a)

hh(2)
print(a)


'''