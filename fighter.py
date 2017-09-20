from weapon import Weapon

class Fighter:
    presets = ['orc', 'thief']
    def __init__(self, weapon, health, xp=0, name='fighter'):
        self.weapon = weapon
        self.maxhealth = health
        self.health = health
        self.xp = xp
        self.name = name
    def isdead(self):
        return self.health <= 0
    def attack(self, other):
        dmg = self.weapon.damage()
        print('{} did {} damage to {}'.format(self.name, dmg, other.name))
        other.health -= dmg
    def __str__(self):
        return '{name} ({xp}XP)'.format(**self.__dict__)
    @staticmethod
    def preset(name):
        if name == 'orc':
            return Fighter(Weapon.preset('axe'), 12, 15, 'orc')
        elif name == 'thief':
            return Fighter(Weapon.preset('sword'), 9, 10, 'thief')
        else:
            raise ValueError('unknown preset "{}"'.format(name))
            