from fighter import Fighter
from weapon import Weapon

MAX_LEVEL = 10

class Player(Fighter):
    def __init__(self, name):
        super().__init__(Weapon.preset('sword'), 50)
        self.level = 1
        self.needed = 100
        self.exp = 0
        self.name = name
    def addexp(self, exp):
        self.exp += exp
        while self.level < MAX_LEVEL and self.exp >= self.needed:
            level += 1
            self.exp -= self.needed
            self.needed = int(self.needed * 1.1)
            print('You leveled up! You are now level {}'.format(self.level))
    def __str__(self):
        return '{name} {health}/{maxhealth}HP {exp}/{needed}XP'.format(**self.__dict__)