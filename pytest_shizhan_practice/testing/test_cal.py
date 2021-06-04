import allure


# import pytest
# import yaml

# with open('datas/datas.yml') as f:
#     # 读取配置文件
#     datas = yaml.safe_load(f)
#     # 加法计算参数
#     add_datas = datas['add']['datas']
#     add_myids = datas['add']['myids']
#     # 减法计算参数
#     sub_datas = datas['sub']['datas']
#     sub_myids = datas['sub']['myids']
#     # 乘法计算参数
#     mul_datas = datas['mul']['datas']
#     mul_myids = datas['mul']['myids']
#     # 除法计算参数
#     div_datas = datas['div']['datas']
#     div_myids = datas['div']['myids']
#
#
# @pytest.fixture(params=add_datas, ids=add_myids)
# def get_add_datas(request):
#     datas = request.param
#     return datas
#
#
# @pytest.fixture(params=sub_datas, ids=sub_myids)
# def get_sub_datas(request):
#     datas = request.param
#     return datas
#
# @pytest.fixture(params=mul_datas, ids=mul_myids)
# def get_mul_datas(request):
#     datas = request.param
#     return datas
#
# @pytest.fixture(params=div_datas, ids=div_myids)
# def get_div_datas(request):
#     datas = request.param
#     return datas


# @pytest.fixture()
# def get_calc():
#     # 实例化计算器
#     calc = Calculate()
#     print("开始计算")
#     yield calc
#     print("计算结束")

@allure.feature("测试计算器")
class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器，用实例变量self.calc接收
    #     self.calc = Calculate()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_myids)
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        # 实例化计算器类
        # calc = Calculate()
        with allure.step("计算两个数的相加和"):
            # 调用加法
            result = get_calc.fun_add(get_add_datas[0], get_add_datas[1])
        # 判断 result 是浮点数，作保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 对结果进行断言
        print(f"a = {get_add_datas[0]}, b = {get_add_datas[1]}, result = {result}")
        assert result == get_add_datas[2]

    # @pytest.mark.parametrize('a,b,expect', sub_datas, ids=sub_myids)
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_sub_datas):
        with allure.step("计算两个数相减"):
            result = get_calc.fun_sub(get_sub_datas[0], get_sub_datas[1])
        print(f"a = {get_sub_datas[0]}, b = {get_sub_datas[1]}, result = {result}")
        assert result == get_sub_datas[2]

    # @pytest.mark.parametrize('a,b,expect', mul_datas, ids=mul_myids)
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        with allure.step("计算两个数相乘"):
            result = get_calc.fun_mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 3)
        print(f"a = {get_mul_datas[0]}, b = {get_mul_datas[1]}, result = {result}")
        assert result == get_mul_datas[2]

    # @pytest.mark.parametrize('a,b,expect', div_datas, ids=div_myids)
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("计算两个数相除"):
                result = get_calc.fun_div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
            print(f"a = {get_div_datas[0]}, b = {get_div_datas[1]}, result = {result}")

        except Exception as e:
            print(e)

        assert result == get_div_datas[2]
