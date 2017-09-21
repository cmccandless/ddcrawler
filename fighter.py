from dice import D20
from weapon import Weapon
from armor import Armor
from console import console

class Fighter:
    presets = ['orc', 'thief']
    def __init__(self, weapon=None, health=5, xp=0, name='fighter', armor=None, ac=6, gold=0):
        self.weapon = weapon or Weapon()
        self.armor = armor or Armor()
        self.baseac = ac
        self.maxhealth = health
        self.health = health
        self.xp = xp
        self.gold = gold
        self.name = name
    def isdead(self):
        return self.health <= 0
    def ac(self):
        return self.baseac + self.armor.ac
    def attack(self, other):
        hit = D20().roll() > other.ac()
        if hit:
            dmg = self.weapon.damage()
            console.print('{} did {} damage to {}'.format(self.name, dmg, other.name))
            other.health -= dmg
        else:
            console.print('{} missed!'.format(self.name))
    def __str__(self):
        return '{name} {health}/{maxhealth}HP [{weapon}]'.format(**self.__dict__)
    @staticmethod
    def preset(name):
        if name == 'orc':
            return Fighter(Weapon.preset('axe'), 12, 15, 'orc', gold=5)
        elif name == 'thief':
            return Fighter(Weapon.preset('sword'), 9, 10, 'thief', gold=5)
        else:
            raise ValueError('unknown preset "{}"'.format(name))
            