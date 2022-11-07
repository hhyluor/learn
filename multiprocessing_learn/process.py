import os
from multiprocessing import Process
import time

n = 0


def pro_func(name, age, **kwargs):
    for i in range(5):
        print("子进程正在运行中,name=%s,age=%d,pid=%d" % (name, age, os.getpid()))
        print(kwargs)
        # print(n)
        # n = n + 1
        time.sleep(0.2)


if __name__ == '__mian__':
    # 创建Process 对象
    print('dadsa')
    # p = Process(target=pro_func, args=('小明', 18), kwargs={'m': 20})
    # # 启动进程
    # p.start()
    # time.sleep(10)
    # # 1秒钟后,立即结束子进程
    # p.terminate()
    # p.join()
