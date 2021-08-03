'''''
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
'''
'''''
from multiprocessing import Process,Queue
import os,time,random

#写数据
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A','N','C','D']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


#读数据
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue,' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
'''
'''''
from multiprocessing import Pipe,Process
import os,time
def prcoessFunc(conn,name):
    print(os.getpid())
    print('进程发送数据',name)
    conn.send(name)
if __name__ == '__main__':
    cons,conr = Pipe()
    prcoess = Process(target=prcoessFunc,args=(cons,"你好！"))
    prcoess.start()
    prcoess.join()

    print(os.getpid())
    print( "接受数据:")
    print(conr.recv())
'''
'''''
import threading,time

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running..' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.'% threading.current_thread().name)
'''
'''''
import time,threading

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - 1
balance = 0
look = threading.Lock()
def run_thread(n):
    for i in range(100000):
        look.acquire()
        try:
            change_it(n)
        finally:
            look.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
import re
re_email = re.compile(r'^[\w]+\.?[\w]+@[\w]+\.com$')
def is_valid_email(addr):
    if __name__ == '__main__':
        if re_email.match(addr):
            return True

assert is_valid_email('some@djhf.com')
