from fighter import Fighter
from weapon import Weapon

class Player(Fighter):
	def __init__(self, name):
		Fighter.__init__(Weapon.presets['sword'], 14)
		self.level = 1
		self.exp = 0
		self.name = name
	