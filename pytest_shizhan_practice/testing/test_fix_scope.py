import pytest


# # scope 参数决定 fixture 的作用域，默认是 function,还支持 class, module, session
# @pytest.fixture(scope='module')
# def connectDB():
#     print("登录操作")
#     yield
#     print("退出登录")


class TestFix:
    # 调用 fixture，直接传入函数名即可
    def test_demo1(self, connectDB):
        print("测试用例demo1")

    def test_demo2(self):
        print("测试用例demo2")

    def test_demo3(self, connectDB):
        print("测试用例demo3")

    # 使用 usefixtures 调用需要以字符串传入函数名
    @pytest.mark.usefixtures('connectDB')
    def test_demo4(self):
        print("测试用例demo4")


class TestFix2:
    def test_demo1(self, connectDB):
        print("测试用例demo1")

    def test_demo2(self):
        print("测试用例demo2")

    def test_demo3(self, connectDB):
        print("测试用例demo3")

    @pytest.mark.usefixtures('connectDB')
    def test_demo4(self):
        print("测试用例demo4")
