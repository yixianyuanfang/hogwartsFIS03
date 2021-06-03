import allure
import pytest


@allure.feature("搜索模块")
class TestSearch:
    def test_searcha(self):
        print("case1")

    def test_searchb(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("输入用户名和密码")
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例，登录失败")
        pass

    @allure.story("用户名缺失")
    def test_login_lost_username(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_lost_password(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass


if __name__ == '__main__':
    pytest.main()
