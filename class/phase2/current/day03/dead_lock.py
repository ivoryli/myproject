import time
import threading

#交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id   #用户
        self.balance = balance  #存款
        self.lock = lock() #锁

    #取钱
    def withdraw(self,amount):
        self.balance -= amount

    #存钱
    def deposit(self,amount):
        self.balance += amount

    #查看账号金额
    def get_balance(self):
        return self.balance

#转账函数
def transfer(from_,to,amount):
    #上锁成功返回True
    if from_.lock.acquire():  #锁住自己的账户
        from_.withdraw(amount)  #自己账户金额减少
        # time.sleep(5)   #模拟网络延迟,产生死锁  #不加睡眠,运行过快,无法体现死锁,可屏蔽其他语句，只留print,出现运行完一个进程再运行另一个
        # print(bool(to.lock.acquire()))
        if to.lock.acquire():   #对方账户上锁
            to.deposit(amount)  #对方账户金额增加
            to.lock.release()  #对方账户解锁
        from_.lock.release() #自己账号解锁
    print("转账完成")

#创建两个账户
Abby = Account("Abby",5000,threading.Lock)
Levi = Account("Levi",3000,threading.Lock)

t1 = threading.Thread(target = transfer,args = (Abby,Levi,1500))
t2 = threading.Thread(target = transfer,args = (Levi,Abby,1000))
t1.start()
# time.sleep(2)   #处理死锁方法
t2.start()
t1.join()
t2.join()
print("Abby",Abby.get_balance())
print("Levi",Levi.get_balance())