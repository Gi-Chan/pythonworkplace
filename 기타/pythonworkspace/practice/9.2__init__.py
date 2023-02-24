# __init__ 파이썬에서 쓰이는 생성자
# 객채라는건 클래스로부터 만들어지는거
# 마린과 탱크는 유닛 클래스의 인스턴드라고 함

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 별 내용이 없네?