from fighter import Fighter
from inventory import Inventory
from weapon import Weapon
from event import (eventhandler,
                   LevelUpEvent)
from console import Console

MAX_LEVEL = 10
BASE_XP_NEEDED = 25


class Player(Fighter):
    def __init__(self, name):
        super().__init__(Weapon.preset('Rusty Sword'),
                         health=50,
                         name=name,
                         ac=8)
        self.inventory = Inventory([self.__weapon__])
        self.needed = BASE_XP_NEEDED

    def addexp(self, xp):
        self.xp += xp
        while self.level < MAX_LEVEL and self.xp >= self.needed:
            self.level += 1
            self.xp -= self.needed
            self.needed = int(self.needed * 1.1)
            eventhandler(LevelUpEvent(self, self.level))

    def stats(self, verbose=False):
        s = super().stats() + ' {}/{}XP'.format(self.xp, self.needed)
        if verbose:
            s += ' {}G\nInventory:\n{}'.format(self.gold, self.inventory)
        return s

    def select_spell(self):
        choices = dict((i + 1, s) for i, s in enumerate(self.spells.keys()))
        if len(choices) == 1:
            return list(self.spells.keys())[0]
        choices['b'] = None
        return Console.inst.menu(choices, 'Select attack/spell:')
