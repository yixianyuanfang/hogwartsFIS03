import pytest


# @pytest.fixture()
# def login():
#     print("登录操作")
#     username = 'freedom'
#     password = '123456'
#     token = 'token123456'
#     # yield 前面的内容相当于 setup,后面的内容相当于 teardown
#     # yield 后面可以返回值，相当于 return
#     yield [username, password, token]
#     print("退出登录")


class TestFix:
    # 调用 fxiture，直接传入函数名即可
    def test_demo1(self, login):
        print("测试用例demo1")
        # 调用 fixture 返回值，直接输入函数名作为变量名即可
        print(f"登录用户信息：{login}")

    def test_demo2(self):
        print("测试用例demo2")

    def test_demo3(self, login):
        print("测试用例demo3")

    # 使用 usefixtures 调用需要以字符串传入函数名
    @pytest.mark.usefixtures("login")
    def test_demo4(self):
        print("测试用例demo4")
