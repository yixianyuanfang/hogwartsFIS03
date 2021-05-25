import yaml

# 定义字典类型
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
dic = yaml.safe_load(document)
print(type(dic))
print(yaml.safe_load(document))

# ymal格式 定义列表类型
print(yaml.safe_load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
"""))
