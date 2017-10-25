from dice import D20
from weapon import Weapon, unarmed
from armor import no_armor
from spell import MeleeBasic
from event import (eventhandler,
                   AttackEvent)

import helper
presets = helper.import_presets(__file__)


class Fighter:
    def __init__(self, weapon=None, health=5, xp=0, level=1, name='fighter',
                 armor=None, ac=6, gold=0):
        self.__weapon__ = weapon
        self.__armor__ = armor
        self.baseac = ac
        self.maxhealth = health
        self.health = health
        self.xp = xp
        self.level = level
        self.gold = gold
        self.name = name
        self.spells = {'Attack': MeleeBasic(self)}

    def weapon(self):
        return self.__weapon__ or unarmed

    def armor(self):
        return self.__armor__ or no_armor

    def isdead(self):
        return self.health <= 0

    def ac(self):
        return self.baseac + self.armor().ac

    def attack(self, target, spell_name='Attack'):
        roll = D20.roll()
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
        fmt = '{name} [{{}}] {health}/{maxhealth}HP'
        return fmt.format(**self.__dict__).format(self.weapon())

    def __str__(self):
        return '{} Lv{}'.format(self.name, self.level)

    @staticmethod
    def preset(name):
        if name in presets:
            data = {'name': name}
            for k, v in presets[name].items():
                if k == 'weapon':
                    data[k] = Weapon.preset(v)
                else:
                    data[k] = v
            return Fighter(**data)
        else:
            raise ValueError('unknown preset "{}"'.format(name))
