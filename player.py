from fighter import Fighter
from inventory import Inventory
from weapon import Weapon

MAX_LEVEL = 10

class Player(Fighter):
    def __init__(self, name, print=print):
        super().__init__(Weapon.preset('sword'), 50, 0, name, ac=8, print=print)
        self.inventory = Inventory([self.weapon, self.armor])
        self.level = 1
        self.needed = 100
    def addexp(self, xp):
        self.xp += xp
        while self.level < MAX_LEVEL and self.xp >= self.needed:
            level += 1
            self.xp -= self.needed
            self.needed = int(self.needed * 1.1)
            self.print('You leveled up! You are now level {}'.format(self.level))
    def __str__(self, verbose=False):
        s = super().__str__() + ' {}/{}XP'.format(self.xp, self.needed)
        if verbose:
            s += ' {}G\n{}'.format(self.gold, self.inventory)
        return s