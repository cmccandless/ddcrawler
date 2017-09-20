from random import randint
from fighter import Fighter

class Encounter:
	presets = [
		Encounter([Fighter.presets['orc'], Fighter.presets['orc']]),
        Encounter([Fighter.presets['thief'], Fighter.presets['orc']])
	]
	def __init__(self, fighters = None):
		self.fighters = fighters or presets[randint(0,len(presets))]