#这个是在其他的学习过程中零散的记忆，不知道把他归为哪一类就把他放这里了
#--------------------------------------------方法用途
#---------------方法注释和类注释
#在方法的名的下一行用三个双引号来写注释可以在调用的时候有提示，类也一样
#---------------随机生成函数
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step]) 	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random() 	随机生成下一个实数，它在[0,1)范围内。
# seed([x]) 	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst) 	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
import random
number = [1,2,3,4,5,6,7,7,8,99,0]
index = random.sample(range(0,10),3)#[4, 0, 3]
print(random.choice(range(0,3)))#0
print(random.shuffle(number))#[4, 2, 7, 6, 8, 99, 0, 5, 3, 1, 7]
print(number,index)
print(random.random())#0.4036665511092772
#---------------range有三个参数我主要说第三个
#第三个时时每个要增加的数
range(0,10,3)
#---------------input
#input可以将用户输入的表达式计算之后在输出
#-----------------------join
#他会给每一个list的元素都添加
abc = "nihao"
print(",".join(abc))
print(",".join('?fasdklfjd'))#?,f,a,s,d,k,l,f,j,d

#--------------------------------------------基础
#-----------------转换类型
max = 24423423-234324325
id = f"10=={max}"
#----------------数值运算
#在python中有怎么一个奇葩的写法
# print('x3'*3)#x3x3x3他真的会输出三遍
# print(3//3)#一个/返回的是浮点数，//返回的是一个整数
# print(3**3)#表示3的s次方
#在同一行显示多条语句但是要加;
a = 0
print();print()
#----------------作用域
#如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
#需要加上global varname他才会把他当作成全局变量
#----------------循环补充
#可以时用for else 和wile else 他们的else都是在(除了break跳出)循环完之后运行
print(",".join("?" for _ in range(10)))#?,?,?,?,?,?,?,?,?,?

#---------------------------------------------------用法比较
#------------isinstance和type的区别
#可以使用isinstance([变量]，[类型])
#在使用isin的时候他会认为子类是父类的一种类型
#isin认为爸爸和儿子是一样的类型
#type认为爸爸就是爸爸儿子就是儿子怎么可能是一样的
#代码（菜鸟教程基本数据类型）
# class A:
# ...     pass
# ... 
# >>> class B(A):
# ...     pass
# ... 
# >>> isinstance(A(), A)
# True
# >>> type(A()) == A 
# True
# >>> isinstance(B(), A)
# True
# >>> type(B()) == A
# False
#-----------------is and ==
#is判断的是对象的引用时否是一样的
#==是判断对象的值是否是一样的
print()
#-----------------------------------python os 文件处理
# os.sep是一个分割线应为Windows和Linux系统分割线不一样



