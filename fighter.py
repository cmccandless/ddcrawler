from dice import D20
from weapon import Weapon
from armor import Armor

class Fighter:
    presets = ['orc', 'thief']
    def __init__(self, weapon, health, xp=0, name='fighter', armor=Armor(), ac=6, print=print):
        self.weapon = weapon
        self.armor = armor
        self.baseac = ac
        self.maxhealth = health
        self.health = health
        self.xp = xp
        self.name = name
        self.print = print
    def isdead(self):
        return self.health <= 0
    def ac(self):
        return self.baseac + self.armor.ac
    def attack(self, other):
        hit = D20().roll() > other.ac()
        if hit:
            dmg = self.weapon.damage()
            self.print('{} did {} damage to {}'.format(self.name, dmg, other.name))
            other.health -= dmg
        else:
            self.print('{} missed!'.format(self.name))
    def __str__(self):
        return '{name} {health}/{maxhealth}HP [{weapon}]'.format(**self.__dict__)
    @staticmethod
    def preset(name):
        if name == 'orc':
            return Fighter(Weapon.preset('axe'), 12, 15, 'orc')
        elif name == 'thief':
            return Fighter(Weapon.preset('sword'), 9, 10, 'thief')
        else:
            raise ValueError('unknown preset "{}"'.format(name))
            