
#类：创建实例的模板
#对象：具体实例
#类方法：与实例相关的函数，在类中定义，其中init为初始化方法
#类变量：在实例中是公用的，定义在类中，且在方法外
#属性：在方法中新增的变量
#内置类属性：doc、name、module等


class student:

    #类的私有属性
    __name__="该属性标识类名"
    __doc__="该属性标识类的文档"
    #类变量
    ID=None
    

#init 方法第一个参数必须是self，表示创建的实例本身，在init内部可以将各种属性绑定到self
#init方法在创建实例时必须传入与之相匹配的参数，以此来绑定属性，但是self不用传
#类中访问属性，不需要从外面的函数去访问，这些函数与类本身关联，成为类的方法，属于数据的封装

    def __init__(self,__instancename__,age,name):
        self.age=age
        self.name=name
        print("this is a instance:",__instancename__)
        print('age is：',self.age)
        print('name is：',self.name)


#类的方法与普通函数无区别，也可以用默认参数，可变参数，关键字参数
#方法就是与实例绑定的函数，但是和函数不同，方法可以直接访问实例数据
#在实例上调用方法，可以直接操作实例内部数据，但无需知道内部实现细节

    def getname(self):
        self.name=input("please input your name :")
        print(self.name)

    def getage(self):
        self.age=input("please input your age:")
        print(self.age)

    def family(self):
        self.family=input("please input your family number:")
        print(self.family)

    def grade(self):
        self.grade=input("please input your grade:")
        print(self.grade)


#实例地址
a=student(1,2,'yfq')  

#给一个实例变量绑定属性
a.ID=3
print(a.ID)
#. 访问实例对象的属性 
a.grade()


#删除实例
del a
print(a.__doc__)
