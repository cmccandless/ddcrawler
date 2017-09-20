from random import randint
import re

class Dice:
	def __init__(self, sides):
		self.sides = sides
	def roll(self):
		return randint(1,self.sides)
		
class D20(Dice):
	def __init__(self):
        Dice.__init__(self, 20)
        
class D10(Dice):
	def __init__(self):
        Dice.__init__(self, 10)
        
class D8(Dice):
	def __init__(self):
        Dice.__init__(self, 8)
        
class D6(Dice):
	def __init__(self):
        Dice.__init__(self, 6)
        
class D4(Dice):
	def __init__(self):
        Dice.__init__(self, 4)