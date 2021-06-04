from time import sleep

import pytest


# 指定用例失败重跑 flaky
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_rerun1():
    sleep(0.5)
    assert 1 == 2


def test_rerun2():
    sleep(0.5)
    assert 2 == 2


def test_rerun3():
    sleep(0.5)
    assert 3 == 2
