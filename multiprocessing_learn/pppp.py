import os
from multiprocessing import Process, Queue
import time

n = []


def pro_func(name, age, **kwargs):
    print("子进程正在运行中,name=%s,age=%d,pid=%d" % (name, age, os.getpid()))
    print(kwargs)
    global n
    print(n)
    n.append(1)
    print(n)
    time.sleep(0.2)


if __name__ == '__main__':
    # 创建Process 对象
    print('dadsa')
    for i in range(5):
        p = Process(target=pro_func, args=('小明', 18), kwargs={'m': 20})
        # 启动进程
        p.start()
        time.sleep(1)
        # 1秒钟后,立即结束子进程
        p.terminate()
        p.join()
