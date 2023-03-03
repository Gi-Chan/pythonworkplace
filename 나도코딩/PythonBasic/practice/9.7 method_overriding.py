# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location): # move라는 함수를 정의해 지상 유닛이 움직이는걸 표현
        print("[지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format( \
            self.name, location, self.speed))
# 공격유닛
class AttackUnit(Unit): # 클래스 이름뒤에 부모 클래스 이름 적으면 내용 넘어옴
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 부모의 객채들을 받아오는 것
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력  {2}]".format( \
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다..".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flayable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(\
            name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flayable): # 공격 유닛과  날 수 있는 클래스를 상속받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flayable.__init__(self, flying_speed)

    def move(self, location): # move를 새롭게 정의하면서 공중유닛도 move로 움직일 수 있음.
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 공격 유닛 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 공격 유닛, 체력이 높고, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")