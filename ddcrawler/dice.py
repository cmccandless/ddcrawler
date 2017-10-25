from random import randint
import re

pattern = re.compile('(D\d+)')


class Dice:

    def __init__(self, sides):
        if isinstance(sides, list):
            self.__name__ = 'D[{}]'.format(','.join(map(str, sides)))
        elif isinstance(sides, int):
            self.__name__ = 'D{}'.format(sides)
        else:
            raise ValueError('"{}" is not a valid sides format'.format(sides))
        self.sides = sides

    def __iter__(self):
        if isinstance(self.sides, list):
            return iter(self.sides)
        return iter(range(1, self.sides + 1))

    def roll(self):
        if isinstance(self.sides, list):
            return self.sides[randint(0, len(self.sides) - 1)]
        return randint(1, self.sides)

    def __str__(self):
        return self.__name__

    def __lt__(self, other):
        return self.sides < other.sides


D20 = Dice(20)
D12 = Dice(12)
D10 = Dice(10)
D8 = Dice(8)
D6 = Dice(6)
D4 = Dice(4)
