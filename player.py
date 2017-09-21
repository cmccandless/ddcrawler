from fighter import Fighter
from inventory import Inventory
from weapon import Weapon
from event import *

MAX_LEVEL = 10

class Player(Fighter):
    def __init__(self, name):
        super().__init__(Weapon.preset('sword'), 50, 0, name, ac=8)
        self.inventory = Inventory([self.weapon])
        self.level = 1
        self.needed = 100
    def addexp(self, xp):
        self.xp += xp
        while self.level < MAX_LEVEL and self.xp >= self.needed:
            level += 1
            self.xp -= self.needed
            self.needed = int(self.needed * 1.1)
            eventhandler(LevelUpEvent(self, self.level))
    def stats(self, verbose=False):
        s = super().stats() + ' {}/{}XP'.format(self.xp, self.needed)
        if verbose:
            s += ' {}G\n{}'.format(self.gold, self.inventory)
        return s