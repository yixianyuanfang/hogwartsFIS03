a = 1


def fun():
    global a
    a = 2
    # 打印a的内存地址
    print(id(a))
    print(f"变量a的值：{a}")
    print("这是一个方法")


# print(a)
# fun()
# # 打印a的内存地址
# print(id(a))
# print(a)
# print(fun())

if __name__ == "__main__":
    print("start")
    fun()
    print("end")
