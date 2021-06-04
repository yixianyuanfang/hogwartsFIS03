from time import sleep

import pytest


@pytest.mark.run(order=2)
def test_foo():
    sleep(1)
    assert True


@pytest.mark.run(order=1)
def test_bar():
    sleep(1)
    assert True


@pytest.mark.run(order=3)
def test_ar():
    sleep(1)
    assert True

# 分布式执行命令：pytest test_xdist.py -n 3
# -n 3:启动3个线程
