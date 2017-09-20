from fighter import Fighter
from weapon import Weapon

MAX_LEVEL = 10

class Player(Fighter):
    def __init__(self, name):
        super().__init__(Weapon.preset('sword'), 50, 0, name)
        self.level = 1
        self.needed = 100
    def addexp(self, xp):
        self.xp += xp
        while self.level < MAX_LEVEL and self.xp >= self.needed:
            level += 1
            self.xp -= self.needed
            self.needed = int(self.needed * 1.1)
            print('You leveled up! You are now level {}'.format(self.level))
    def __str__(self):
        return super().__str__() + ' {}/{}XP'.format(self.xp, self.needed)