import time
# 1. 상속
class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp =hp
        self.max_hp = hp
        self.power = power

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격합니다.")
        damage = self.power
        target.take_damage(damage)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.name}이(가) 쓰러졌습니다.")

        print(f'{self.name}은 {amount}의 피해를 입고 {self.hp}의 체력이 남았습니다. : {self.hp} / {self.max_hp}')

    def show_status(self):
        print(f'이름: {self.name}, 체력: {self.hp} / {self.max_hp}, 공격력: {self.power}')

    def is_alive(self):
        return self.hp > 0

class Hero(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

        self.level=1
        self.inventory=[]
        print(f'{self.name}이(가) 모험을 시작합니다.')

    def eat_item(self, item):
            print(f'{self.name}이(가) {item}을(를) 먹었습니다.')

    def show_status(self):
        print(f'[영웅] 이름: {self.name}, 체력: {self.hp} / {self.max_hp}, 공격력: {self.power}')


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.drop_item = None
        print(f'몬스터 {self.name}이(가) 나타났습니다.')
class Slime(Monster):
    def attack(self, target):
        print(f'{self.name}의 몸통박치기!')
        damage = self.power
        target.take_damage(damage)

class Dragon(Monster):
    def attack(self, target):
        print(f'{self.name}의 화염구! ')
        damage = int(self.power * 1.5)
        target.take_damage(damage)


# 전투 시스템
def battle(hero, monster):
    print(f"{monster.name}이 나타났다!")
    print(f"(HP: {monster.hp}, 공격력: {monster.power})")
    while hero.is_alive() and monster.is_alive():
        print("-" * 30 )

        print("선택!")
        print("1. 공격")
        print("2. 도망")
        choice = input("행동을 선택하세요: ")

        if choice == "1":
            hero.attack(monster)
            if not monster.is_alive():
                print(f"{monster.name}을(를) 물리쳤습니다!")
                break

            time.sleep(1)
            print( "몬스터의 반격!")
            monster.attack(hero)
            if not hero.is_alive():
                print(f"{hero.name}이(가) 쓰러졌습니다.")
                break

        elif choice == "2":
            print("도망쳤습니다!")
            break
        else:
            print("잘못된 선택입니다.")

# 게임 실행
if __name__ == "__main__":
    print("=== 게임 시작 ===")
    hero = Hero("주인공", 100, 10)
    slime = Slime("슬라임", 50, 5)
    dragon = Dragon("드래곤", 200, 20)

    #battle(hero, slime)
    battle(hero, dragon)