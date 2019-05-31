'''
   形参传递方式
     默认形参

     位置形参
        -- 星号元组形参:位置实参数量无限

     命名关键字形参:要求必须使用关键字实参
        --双星号命名关键字形参形参:关键字实参数量无限
'''

def fun01(a,b,c):
    pass

def fun02(*args):
    #对于方法而言，就是元组
    #对于调用者而言,可以传递数量无线的位置实参
    print(args)

fun02()
fun02(1)
fun02(1,2,3,4)

#命名关键字形参
#a,b是命名关键字形参
#*代表后面是命名关键字形参,不能传入任意对象
def fun03(*,a,b):
    print(a)
    print(b)

#b是命名关键字形参
def fun04(*args,b):
    print(args)
    print(b)

fun03(a = 1,b = 2)
fun04(2,3,4,b = 22)

#双星号字典形参
def fun05(**kwargs):
    # 对于方法而言，就是字典
    #对于调用者而言, 可以传递数量无线的关键字实参
    for key,value in kwargs.items():
        print(key,value)

fun05(a = 1,b = 2)

def fun06(*args,**kwargs):
    print(args)
    print(kwargs)

fun06(2,3,4,[2,3,4],b = 2,c = 4,**{"a":18,"d":12})

def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun07(1,2,4,5,6,c = 1,d = 5,**{"s":5,"r":7})
