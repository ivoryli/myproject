from multiprocessing import Process,Array

#创建共享内存
# 共享内存开辟5个整型元素列表空间
# shm = Array('i',[1,2,3])

#字节串
shm = Array('c',b'hello')

def fun():
    #共享内存对象可迭代
    for i in shm:
        print(i)
    #修改共享内存
    # shm[1] = 10000
    shm[0] = b'H'

p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i,end = ' ')

print()
#通过value属性访问字节串
print(shm.value)