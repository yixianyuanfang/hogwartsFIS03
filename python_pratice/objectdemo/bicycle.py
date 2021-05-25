class Bicycle:
    def run(self, km):
        print(f"健康环保，骑行里程数为：{km}")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化变量
        self.battery_level = battery_level

    def fill_charge(self, vol):
        # 充电
        self.battery_level = self.battery_level + vol

    def run(self, km):
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"已经使用电行驶:{self.battery_level * 10} km")
            super().run(miles)
        else:
            print(f"已经使用电行驶完：{km} km")


if __name__ == '__main__':
    eb = EBicycle(10)
    eb.fill_charge(10)
    eb.run(201)
