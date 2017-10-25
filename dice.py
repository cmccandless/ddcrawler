from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.__name__ = 'D{}'.format(sides)

    def roll(self):
        return randint(1, self.sides)

    def __str__(self):
        return 'D{}'.format(self.sides)

    def __lt__(self, other):
        return self.sides < other.sides


D20 = Dice(20)
D12 = Dice(12)
D10 = Dice(10)
D8 = Dice(8)
D6 = Dice(6)
D4 = Dice(4)
