from weapon import Weapon

class Fighter:
    presets = {
        'orc': Fighter(Weapon.presets['axe'], 12, 'orc'),
        'thief': Fighter(Weapon.presets['sword'], 9, 'thief')
    }
	def __init__(self, weapon, health, name='fighter'):
		self.weapon = weapon
		self.maxhealth = health
		self.health = maxhealth
        self.name = name
	def dead(self):
		return self.health <= 0
	def attack(self, other):
		other.health -= self.weapon.damage()
        