#变量可以指向函数,函数名也是变量
def a():
    ine = input("please input:")
    print(ine)
    return ine

f=a
#f()


#高阶函数：一个函数可以接收另一个函数的函数名作为函数的参数         
def ab(x,y,h):
    x=h()
    y=h()
    return 

#ab(1,2,f())


#返回函数：高阶函数可以把函数作为结果值返回
def sum(*a):
    def su():
        x=0
        for n in a:
            x=x+n
        return x
    return su


f=sum(1,2,3)
print(f())

#闭包




#匿名函数

#装饰器


#偏函数


