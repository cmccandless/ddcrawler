import dice
from item import Item
from itertools import groupby

class Weapon(Item):
    presets = ['sword', 'axe']
    def __init__(self, damageDice, name='weapon', crit_handler=lambda w: w.damage() + w.damage()):
        super().__init__(name)
        self.damageDice = list(sorted(damageDice))
        self.crit_handler = crit_handler
    def damage(self):
        return sum(d.roll() for d in self.damageDice)
    def min_damage(self):
        return len(self.damageDice)
    def max_damage(self):
        return sum(d.sides for d in self.damageDice)
    @staticmethod
    def preset(name):
        if name == 'sword':
            return Weapon([dice.D4(), dice.D4()], 'sword')
        elif name == 'axe':
            return Weapon([dice.D10()], 'axe')
        else:
            raise ValueError('unknown preset "{}"'.format(name))
    def __str__(self):
        # groupedDice = groupby(self.damageDice, lambda d: d.sides)
        # dmgStr = ' + '.join('{}D{}'.format(len(list(g)), k) for k, g in groupedDice)
        dmgStr = '{}-{}'.format(self.min_damage(), self.max_damage())
        return '{}({})'.format(self.name, dmgStr)
        
unarmed = Weapon([dice.D4()], 'unarmed')