#module是一个python文件，便于开发
#模块的引入 import module，就可以使用一个完整的模块里面的所有内容，但是需要.来引用
import main
main.a(1,3)



#from...import... 从模块中导入一个指定部分到当前空间中
#import模块后，可以用模块名字调用模块内部，from import后，可以直接引用模块函数等
#from...import * 从模块中导入全部到当前空间中
from main import*
a(1,3)
print(PI)


#dir函数返回一个模块中给定义的所有模块信息，变量和函数

import main

main.a(1,3)
print(main.PI)
c=dir(main)
print(c)






