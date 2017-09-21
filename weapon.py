from dice import *
from item import Item

with open('weapon.json', 'r') as f:
    from json import load
    presets = load(f)

class Weapon(Item):
    presets = ['sword', 'axe']
    def __init__(self, damageDice, value=2, name='weapon', crit_handler=lambda w: w.damage() + w.damage()):
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
        if name in presets:
            data = {'name':name}
            for k, v in presets[name].items():
                if k == 'damageDice':
                    data[k] = eval(v)
                else:
                    data[k] = v
            return Weapon(**data)
        else:
            raise ValueError('unknown preset "{}"'.format(name))
    def __str__(self):
        dmgStr = '{}-{}'.format(self.min_damage(), self.max_damage())
        return '{}({})'.format(self.name, dmgStr)
        
unarmed = Weapon([D4], 'unarmed')