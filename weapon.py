import dice

class Weapon:
    presets = ['sword', 'axe']
    def __init__(self, attackDice, name='weapon'):
        self.attackDice = attackDice
        self.name = name
        
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