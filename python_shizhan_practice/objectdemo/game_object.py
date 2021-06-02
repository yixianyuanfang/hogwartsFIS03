class Game:
    my_hp = 1000
    my_power = 200
    enemy_hp = 2000
    enemy_power = 199

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
            print(f"我的血量：{self.my_hp}")
            print(f"敌人的血量：{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break
    
    def back_home(self):
        print("回城")


class HouYi(Game):
    def __init__(self, defense):
        self.defense = defense

    def fight(self):
        while True:
            if self.defense > self.enemy_power:
                self.my_hp = self.my_hp
            else:
                self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
            print(f"我的血量：{self.my_hp}")
            print(f"敌人的血量：{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break


# game = Game()
# game.fight()
houyi = HouYi(200)
houyi.fight()
houyi.back_home()
