import yaml


# yaml.safe_load() 将 yaml 数据流转成 python 对象
# yaml.safe_dump() 将python 对象转成 yaml 数据格式
def get_datas():
    with open('data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)

    return datas


print(get_datas())

yamlstr = yaml.safe_dump({'languages': ['Ruby', 'Perl', 'Python'],
                          'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org',
                                       'Perl': 'use.perl.org'}})
# print(yamlstr)
