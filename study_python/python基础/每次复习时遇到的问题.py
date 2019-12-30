#如果默认参数指向一个值的话，那么第二次调用这个方法指向的也是这个值（为什么？）
def a(a=[]):
    a.append('n')
    return a
a()
a()
print(a())#>>>['n', 'n', 'n']
#解决方法
def b(a = None):
    if a is None:
        a = []
    a.append('n')
    return a
b()
b()
print(b())#>>>['n']