import os
from typing import List

import pytest
import yaml
from pytest_shizhan_practice.python_code.calculate import Calculate


# scope 参数决定 fixture 的作用域，默认是 function,还支持 class, module, session
@pytest.fixture(scope='module')
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库连接")


@pytest.fixture()
def login():
    print("登录操作")
    username = 'freedom'
    password = '123456'
    token = 'token123456'
    # yield 前面的内容相当于 setup,后面的内容相当于 teardown
    # yield 后面可以返回值，相当于 return
    yield [username, password, token]
    print("退出登录")


@pytest.fixture(scope='class')
def get_calc():
    # 实例化计算器
    calc = Calculate()
    print("开始计算")
    yield calc
    print("计算结束")


yaml_file_path = os.path.dirname(__file__) + '/datas/datas.yml'
print(yaml_file_path)
with open(yaml_file_path) as f:
    # 读取配置文件
    datas = yaml.safe_load(f)
    # 加法计算参数
    add_datas = datas['add']['datas']
    add_myids = datas['add']['myids']
    # 减法计算参数
    sub_datas = datas['sub']['datas']
    sub_myids = datas['sub']['myids']
    # 乘法计算参数
    mul_datas = datas['mul']['datas']
    mul_myids = datas['mul']['myids']
    # 除法计算参数
    div_datas = datas['div']['datas']
    div_myids = datas['div']['myids']


@pytest.fixture(params=add_datas, ids=add_myids)
def get_add_datas(request):
    datas = request.param
    return datas


@pytest.fixture(params=sub_datas, ids=sub_myids)
def get_sub_datas(request):
    datas = request.param
    return datas


@pytest.fixture(params=mul_datas, ids=mul_myids)
def get_mul_datas(request):
    datas = request.param
    return datas


@pytest.fixture(params=div_datas, ids=div_myids)
def get_div_datas(request):
    datas = request.param
    return datas


# hook 函数学习
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param pytest.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 实现用例反转执行
    items.reverse()

    # 修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # item.nodeid 拿到的是测试用例的名称
        # 自动给测试用例加上标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.dir)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
