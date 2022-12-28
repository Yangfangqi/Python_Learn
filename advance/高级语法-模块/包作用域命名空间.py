'''
1.package包
①package包是一个分层次的文件目录结构，定义了一个由模块及子包等组成的python应用环境
包目录下的模块文件，可以调用同一级别的模块或者子包中的模块文件
②一个package 包需要一个__init__.py文件标识当前文件夹是一个包
通常__inti__.py 文件是空文件，导入一个包时，实际上是导入了他的init文件
因此，再init文件中批量导入我们所需要的模块即可



2.作用域
前缀_XXX的变量是非公开的变量，仅在模块内部使用;
其余变量是公开的，可以直接被引用;
__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途;
如：__author__,__name__

#__name__ 指向引入模块的名字
#__file__指向引入文件的名

3.每个python文件，若未命名__name__，则若单独运行该文件，则为__main__
若每个python文件是被import，则当前文件不是__main_

4.模块类引入同级目录下的所有模块

'''


#reload()
#global()
#local()


"this is a package test"
__author__="YFQ"
__name__="包和作用域"


import main
print(main.PI)

if __name__ == '__main__':
    print("the file is package")
