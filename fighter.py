from dice import D20
from weapon import Weapon, unarmed
from armor import Armor, no_armor
from spell import MeleeBasic
from event import *

class Fighter:
    presets = ['orc', 'thief']
    def __init__(self, weapon=None, health=5, xp=0, name='fighter', armor=None, ac=6, gold=0):
        self.__weapon__ = weapon
        self.__armor__ = armor
        self.baseac = ac
        self.maxhealth = health
        self.health = health
        self.xp = xp
        self.gold = gold
        self.name = name
        self.spells = {'attack':MeleeBasic(self)}
    def weapon(self):
        return self.__weapon__ or unarmed
    def armor(self):
        return self.__armor__ or no_armor
    def isdead(self):
        return self.health <= 0
    def ac(self):
        return self.baseac + self.armor().ac
    def attack(self, target, spell_name='attack'):
        roll = D20().roll()
        critical = roll == 20
        if critical:
            hit = True
        else:
            hit = roll > target.ac()
        spell = self.spells[spell_name]
        dmg = spell.crit_damage(target) if critical else spell.damage(target)
        if hit:
            target.health -= max(0, dmg)
        eventhandler(AttackEvent(self, target, hit, dmg, critical))
    def stats(self):
        return '{name} [{{}}] {health}/{maxhealth}HP'.format(**self.__dict__).format(self.weapon())
    def __str__(self):
        return self.name
    @staticmethod
    def preset(name):
        if name == 'orc':
            return Fighter(Weapon.preset('axe'), 12, 15, 'orc', gold=5)
        elif name == 'thief':
            return Fighter(Weapon.preset('sword'), 9, 10, 'thief', gold=5)
        else:
            raise ValueError('unknown preset "{}"'.format(name))
            