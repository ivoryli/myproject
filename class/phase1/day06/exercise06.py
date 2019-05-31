'''
   扩展练习(定义函数，返回指定范围内的素数)
   例如：１－－１００　　
'''

def is_prime(number):
    '''
       判断是否为素数
    :param number: 判断该数是否为素数
    :return: 如果是素数,返回True,否则返回False
    '''
    if number < 2:
        return False
    for x in range(2,number):
        if number % x == 0:
            return False
    return True

def prime(begin,end):
    '''
        生成由begin开始到end结束的素数
    :param begin: 开始值
    :param end: 结束值(不包括本身)
    :return: 返回是素数的列表
    '''
    L = []
    for x in range(begin,end):
        if is_prime(x):
            L.append(x)
    return L

