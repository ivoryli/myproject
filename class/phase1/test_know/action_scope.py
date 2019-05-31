'''
   作用域
'''

name = 'PythonTab'
def func1():
    # print('my name is %s' %(name))
    #可查不可用,可用前提:之后没有同名变量赋值
    name.count(y)
    name = 'PythonTab.com'
    print('my name is %s' %(name))
func1()
print(name)