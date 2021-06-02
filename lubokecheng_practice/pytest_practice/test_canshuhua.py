import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(['a', 'b'], yaml.safe_load(open('data.yml')))
    def test_param(self, a, b):
        print(a + b)

# @pytest.mark.parametrize('a,b', [(1, 2), (5, 9), (10, 30)])
# def test_param(a, b):
#     print(a + b)
