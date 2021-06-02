import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec):
    logging.info(f"loop{nloop} start at " + ctime())
    sleep(nsec)
    logging.info(f"loop{nloop} end at " + ctime())


def main():
    nloops = range(len(loops))
    threads = []
    logging.info("all start at " + ctime())
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # 开启一个线程
        threads.append(t)
    for i in nloops:
        threads[i].start()  # 启动线程
    for i in nloops:
        threads[i].join()  # 堵塞运行，直至线程运行结束
    logging.info("all end at " + ctime())


if __name__ == '__main__':
    main()
