import pytest
import yaml

from pytest_shizhan_practice.python_code.calculate import Calculate


def test_case():
    print("测试用例1")


with open('../datas/datas.yml') as f:
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


class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器，用实例变量self.calc接收
        self.calc = Calculate()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_myids)
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculate()
        # 调用加法
        result = self.calc.fun_add(a, b)
        # 判断 result 是浮点数，作保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 对结果进行断言
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', sub_datas, ids=sub_myids)
    def test_sub(self, a, b, expect):
        result = self.calc.fun_sub(a, b)
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', mul_datas, ids=mul_myids)
    def test_mul(self, a, b, expect):
        result = self.calc.fun_mul(a, b)
        if isinstance(result, float):
            result = round(result, 3)
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', div_datas, ids=div_myids)
    def test_div(self, a, b, expect):
        result = self.calc.fun_div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == expect
