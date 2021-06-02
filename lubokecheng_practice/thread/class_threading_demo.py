import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)  # 主动去调Thread初始化函数？？？为什么
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)  # *self.args:解元组


def loop(nloop, nsec):
    logging.info(f"loop{nloop} start at " + ctime())
    sleep(nsec)
    logging.info(f"loop{nloop} end at " + ctime())


def main():
    nloops = range(len(loops))
    threads = []
    logging.info("all start at " + ctime())
    for i in nloops:
        t = MyThread(loop, (i, nloops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("all end at " + ctime())


if __name__ == '__main__':
    main()
