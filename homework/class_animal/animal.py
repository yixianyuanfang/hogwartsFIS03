import yaml


# 定义一个动物类
class Animal:
    # 默认值
    # name = "None"
    # color = "白"
    # age = 0
    # gender = "男"

    # 初始化
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 定义方法 叫
    def shout(self):
        print(f"{self.name}会叫")

    # 定义方法 跑
    def run(self):
        print(f"{self.name}会跑")


# 定义一个子类 猫
class Cat(Animal):
    # 初始化
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        # 继承父类属性
        super().__init__(name, color, age, gender)

    # 定义额外的技能
    def extra_skill(self):
        print(f"{self.name}会捉老鼠")

    # 定义方法 喵喵叫
    def jiao(self):
        print(f"{self.name}会喵喵叫")


# 定义一个子类 狗
class Dog(Animal):
    # 初始化
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        # 继承父类属性
        super().__init__(name, color, age, gender)

    # 定义额外的技能
    def extra_skill(self):
        print(f"{self.name}会看家")

    # 定义方法 汪汪叫
    def jiao(self):
        print(f"{self.name}会汪汪叫")


if __name__ == '__main__':
    # cat = Cat("短发", "凯蒂", "白色", 10, "女")
    # cat.extra_skill()
    # dog = Dog("长发", "八公", "黄色", 5, "男")
    # dog.extra_skill()

    # 读取配置文件中的属性
    with open("shuxing.yml") as f:
        datas = yaml.safe_load(f)
    # 赋值猫的属性
    name = datas['cat']['name']
    color = datas['cat']['color']
    age = datas['cat']['age']
    gender = datas['cat']['gender']
    hair = datas['cat']['hair']
    # 实例化 猫
    cat = Cat(hair, name, color, age, gender)
    print(f"姓名：{cat.name}\t颜色：{cat.color}\t年龄：{cat.age}岁\t性别：{cat.gender}\t毛发：{cat.hair}")
    cat.extra_skill()

    # 赋值狗的属性
    name = datas['dog']['name']
    color = datas['dog']['color']
    age = datas['dog']['age']
    gender = datas['dog']['gender']
    hair = datas['dog']['hair']
    # 实例化 猫
    dog = Dog(hair, name, color, age, gender)
    print(f"姓名：{dog.name}\t颜色：{dog.color}\t年龄：{dog.age}岁\t性别：{dog.gender}\t毛发：{dog.hair}")
    dog.extra_skill()
