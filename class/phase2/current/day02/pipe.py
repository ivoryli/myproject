#管道通信,管道在内存中开辟   通过字节流传递


# from multiprocessing import Process,Pipe
# import os,time
#
# fd1,fd2 = Pipe()
# # fd1,fd2 = Pipe(False)   fd1只能读,fd2只能写
#
# def fun(name):
#     # time.sleep(3)
#     #向管道写入内容
#     fd1.send({name:os.getpid()})
#
# jobs = []
# for i in range(5):
#     p = Process(target = fun,args = (i,))
#     jobs.append(p)
#     p.start()
#
# time.sleep(2)
# for i in range(2):
#     #读取管道
#     data = fd2.recv()   #recv会引起阻塞
#     print(data)
#
# for i in jobs:
#     i.join()

# 应该特别注意管道端点的正确管理问题。如果是生产者或消费者中都没有使用管道的某个端点，就应将它关闭。这也说明了为何在生产者中关闭了
# 管道的输出端，在消费者中关闭管道的输入端。如果忘记执行这些步骤，程序可能在消费者中的recv（）操作上挂起。管道是由操作系统进行引用计数的，
# 必须在所有进程中关闭管道后才能生成EOFError异常。因此，在生产者中关闭管道不会有任何效果，除非消费者也关闭了相同的管道端点。
# https://www.cnblogs.com/xiao987334176/articles/9036763.html


from multiprocessing import Process, Pipe


def f(parent_conn, child_conn):
    parent_conn.close()  # 不写close将不会引发EOFError
    while True:
        try:
            print(child_conn.recv())
        except EOFError:
            child_conn.close()
            break


if __name__ == '__main__':
    # 在进程之间创建一条管道，并返回元组（conn1,conn2），其中conn1和conn2是表示管道两端的Connection对象
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(parent_conn, child_conn,))
    p.start()
    child_conn.close()  # 关闭连接
    parent_conn.send('hello')
    parent_conn.send('hello')
    parent_conn.send('hello')
    parent_conn.close()
    p.join()  # 等待子进程结束
