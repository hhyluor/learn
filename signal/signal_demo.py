import signal
import sys
from functools import partial


def on_exit(signum, frame, extra_info):
    """
    signum和frame是信号监听函数默认的参数，不可以少
    问题：当我们的信号监听函数内需要使用调用者传入额外的参数怎么办？
    解决：我们可以使用偏函数【partial】
    """
    print(extra_info)


print("获取到信号，我要退出了")
sys.exit(0)


def main():
    signal.signal(signal.SIGINT, partial(on_exit, service_id=service_id))
    signal.signal(signal.SIGTERM, partial(on_exit, service_id=service_id))

    while True:
        print(123123123)


if __name__ == "__main__":
    main()