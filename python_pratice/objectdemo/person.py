class Person:
    name: str = "None"
    age: int = 0
    gender: str = "女"
    __money: float = 0

    def __init__(self, name, age, gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")


class FunnyMan(Person):
    skill: str = "技能"

    def __init__(self, skill, name, age, gender, money):
        self.skill = skill
        super(FunnyMan, self).__init__(name, age, gender, money)

    def funny(self):
        print(f"{self.name} is funny, his skill is {self.skill}")


# p_zs = Person("张三", 20, "男", 1000)
# print(p_zs.name)
# p_zs.eat()

st = FunnyMan("抡大锤", "王爷", 25, "男", 1500)
print(st.name)
st.funny()
# 输出实例对象的内存地址
print(st)
