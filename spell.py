class Spell:
    def __init__(self, attacker, ntargets = 1, damageDice=[], modifer=lambda a, t: 0, modiferDesc='', name='spell'):
        self.attacker = attacker
        self.ntargets = ntargets
        self.damageDice = damageDice
        self.modifer = modifer
        self.modiferDesc = modiferDesc
        self.name = name
    def damage(self, target):
        return sum(d.roll() for d in self.damageDice) + self.modifer(self.attacker, target)
    def min_damage(self):
        return len(self.damageDice)
    def max_damage(self):
        return sum(d.sides for d in self.damageDice)
    def __str__(self):
        return '{}({}-{}){}'.format(self.name,
                                    self.min_damage(), 
                                    self.max_damage(),
                                    self.modiferDesc)
        
class MeleeBasic(Spell):
    def __init__(self, attacker):
        super().__init__(attacker, name='attack')
    def damage(self, target):
        return self.attacker.weapon().damage()
    def crit_damage(self, target):
        return self.damage() + self.damage()
    def min_damage(self):
        return self.attacker.weapon().min_damage()
    def max_damage(self):
        return self.attacker.weapon().max_damage()