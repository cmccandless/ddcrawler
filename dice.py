from random import randint
import re

class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)
    def __str__(self):
        return 'D{}'.format(self.sides)
    def __lt__(self, other):
        return self.sides < other.sides
        
class D20(Dice):
    def __init__(self):
        super().__init__(20)
        
class D10(Dice):
    def __init__(self):
        super().__init__(10)
        
class D8(Dice):
    def __init__(self):
        super().__init__(8)
        
class D6(Dice):
    def __init__(self):
        super().__init__(6)
        
class D4(Dice):
    def __init__(self):
        super().__init__(4)