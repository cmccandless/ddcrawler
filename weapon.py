import dice
from item import Item
from itertools import groupby

class Weapon(Item):
    presets = ['sword', 'axe']
    def __init__(self, attackDice, name='weapon'):
        super().__init__(name)
        self.attackDice = list(sorted(attackDice))
        
    def damage(self):
        return sum(d.roll() for d in self.attackDice)
    @staticmethod
    def preset(name):
        if name == 'sword':
            return Weapon([dice.D4(), dice.D4()], 'sword')
        elif name == 'axe':
            return Weapon([dice.D10()], 'axe')
        else:
            raise ValueError('unknown preset "{}"'.format(name))
    def __str__(self):
        groupedDice = groupby(self.attackDice, lambda d: d.sides)
        dmgStr = ' + '.join('{}D{}'.format(len(list(g)), k) for k, g in groupedDice)
        return '{} {}'.format(self.name, dmgStr)