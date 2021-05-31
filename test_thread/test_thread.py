import _thread
import logging
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info(f"loop{nloop} start at " + ctime())
    sleep(nsec)
    logging.info(f"loop{nloop} end at " + ctime())
    lock.release()  # 释放锁


def main():
    locks = []
    nloops = range(len(loops))
    logging.info("all start at " + ctime())
    for i in nloops:
        lock = _thread.allocate_lock()  # 申明一个锁
        lock.acquire()  # 加锁
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 开启一个线程
    for i in nloops:
        while locks[i].locked(): pass  # 判断锁是否锁住，锁住为True,已释放锁为False
    logging.info("all end at " + ctime())


if __name__ == '__main__':
    main()
