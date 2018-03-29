#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import time
import logging

import db_transfer

# MainThread是一个进程中的主线程
# threading.Thread可以创建一个线程啊
# 主线程的类是继承自threading.Thread
class MainThread(threading.Thread):
    # __init__用来创建实例的属性
    def __init__(self, obj): 
        threading.Thread.__init__(self)
        self.obj = obj

    # 封装类的方法
    def run(self):
        self.obj.thread_db(self.obj)

    def stop(self):
        self.obj.thread_db_stop()

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s %(asctime)s] %(message)s',
    )

    # 创建一个线程  并传入一个参数作为实例属性（方法）
    thread = MainThread(db_transfer.Dbv3Transfer)
    thread.start()

    try:
        while thread.is_alive():
            time.sleep(10)
    except (KeyboardInterrupt, IOError, OSError) as e:
        import traceback
        traceback.print_exc()
        thread.stop()

# __name__表示一个当前模块的内置属性，如果直接运行当前模块
# 就会执行之后的代码啊  所以如果我要 python server.py 则会执行main()
if __name__ == '__main__': 
    main()
