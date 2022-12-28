'''
#字符串类型
#字符串由数字、字母、下标组成，由''，"" 括号创建
#字符串的索引下表有正向和逆向两个顺序，由[]以及下标索引 （切片索引）
#字符串类型数据操作符：+，*，[],[:],not in,in
#内置字符串方法
#字符串格式化
#可用函数：len

#字符串操作
a='hello'
print(a*2)
#print(a+'hello')
asd="addfgdfgfdg"+"asdasd"
#print(len(asd))
#print(asd)
#print(asd[0:5])
#print("asdasd" in asd)
#print("asdasd" not in asd)


#list=[]内置任何数据类型、内容可不一致 列表内可以包含列表
#list [] 可以使用下标索引，截取索引
#可以添加、删除 插入、排序等方法操作列表对象
#很多函数可以操作列表：将列表转为元祖，求列表长度
#列表有很多操作符号



#列表变量、索引、截取
clsdd=['1', 'asd', '123']
csl=[1,2,clsdd]
#print(csl)
#print(clsdd[0:3])
#print(clsdd[2])
#print(csl[2][2])


#列表脚本操作符&函数
ab=['123',345,45]
sd=["asd","sdf",123]
#print(ab+sd)
#print(ab*2)
#print(len(ab))
#print("123" in ab)
#print("sdf" not  in sd)

#列表操作方法
clsdd.append(123)
#print(clsdd)
#print(len(clsdd))
clsdd.insert(2,34)
#print(clsdd)
clsdd.pop(3)
#print(clsdd)

'''
'''

#tuple() 创建元组，创建后元素不可更改 
#元素指向不变，若内置列表，则列表数值可变 可读取

a=(2,"123")
b=(1,) #只包含一个元素
c=() #创建空元组
print(a)
print(b)
print(c)

#元组下表索引和截取索引
print(a[0])
print(a[0:2])

#元组操作符
print(a+b)
print(a*2)
print(2 in a)
print(2 not in a)

#元组函数
#del a
print(len(b))
 
#无关闭分隔符 任何变量以逗号隔开，默认为元组
d='abc',-2323,18
print(d)

'''

#字典
#字典是一种可变容器，且存储任意类型对象，有键值，用：分割，键值对用，分割，字典用{}表示
#键值必须唯一，值可以取任何数据类型，如字符串、数字、元组
#同一个键值不允许出现两次，否则会覆盖
#键值不可以改变，所以可以用数字、字符串、元组充当，不能用列表
d={"名字：":"Li","年龄：":18,"账号：":32323214153,"列表：":[1,2,3],"元组：":(1,2,3)}
print(d)

#通过键值访问字典，访问时用[]索引，如果访问没有的键值，则会出现错误
print(d["年龄："])

#修改字典：添加/删减新的键值对，或者修改已有键值对
d["名字："]="Y"
d["列表："]=[3,4,5]
del d["元组："]
print(d)


#函数&方法
#字典长度
#print(len(d))
#清空字典条目
#d.clear() 
#print(d)
#删除字典
#del d
#print(d)

