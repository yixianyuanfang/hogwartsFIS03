from save_money import money


def send_money():
    print("发工资啦！存款又多了1000块")
    money.saved_money = money.saved_money + 1000


if __name__ == '__main__':
    send_money()
