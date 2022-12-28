'''
#条件判断语句格式 缩近表示同一段 
#if (条件语句):(执行语段) 
# elif (条件语句):(执行语段)
# else (条件语句):(执行语段)
#python 不支持switch 语句
#条件语句中可以添加 or、not、and 逻辑运算

b=input("please input some data:")
if len(b)>10:
    print("b >10")
elif len(b)<10:
    print("b<10")
else:
    print("end")
'''
'''
#while 循环
#while 判断条件() 执行语句()
#while 缩进表示同一断

while(1):

    b=input("please input some data:")
    if len(b)>10:
        print("b >10")
    elif len(b)<10:
        print("b<10")
    else:
        print("end")

    print(len(b))
    print('this is a test')

#while语句中还有continue跳过该次循环
#break 用于退出循环    
while(1):

    b=input("please input some data:")
    if len(b)<5:
        print("b>5")
        continue
    #elif len(b)<9:
    #    print("b<9")
    #else:
    #    break

    print(len(b))
    print('this is a test')

'''

'''
#for 循环可以遍历任何序列，如一个列表，字符串，或者元组、字典(字典遍历的是键值)
#for 循环结合range()生成序列函数，可以按照序列索引号遍历任何一个数据类型
sum=0
a=[123,234,1234456]
for name in a:
    print("a is :",name)
for x in range(len(a)):
    print("a is :",a[x])


a='hello'
for x in range(len(a)):
    print(a[x])


a=('hello',"jaskd")
for x in a:
    print(x)

a={"asd":2,"ds":3,"dsd":4}
for x in a:
    print(a[x])

'''

'''
#continue 跳过当前循环剩余语句，继续执行下一循环
#break 结束整个循环，执行循环外的语句
i=0
while(1):
    if (i <10):
        print("i is :", i)
        i=i+1
    elif(i==10):
        print("i ==10")
        i=i+1
        continue
    else:
        print("i>10")
        break
    print("this is a test")
print("t")
'''

#pass 不做任何事，用作占位句

