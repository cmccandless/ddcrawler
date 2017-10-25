import unittest

from dice import (Dice, D4, D6, D8, D10, D12, D20)


class DiceTest(unittest.TestCase):
    def test_die(self, die):
        for _ in range(100):
            roll = die.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, die.sides)

    def test_presets(self):
        for die in [D4, D6, D8, D10, D12, D20]:
            self.test_die(die)

    def test_arbitrary_die(self):
        die = Dice(7)
        self.test_die(die)


if __name__ == '__main__':
    unittest.main()
