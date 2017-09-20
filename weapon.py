import dice

class Weapon:
    presets = {
        'sword': Weapon([dice.D4(), dice.D4()]),
        'axe': Weapon([dice.D10()])
    }
	def __init__(self, attackDice):
		self.attackDice = attackDice
		
	def damage(self):
		return sum(d.roll() for d in self.attackDice)
        