#!/usr/bin/env python
import unittest

from dice import (Dice, D4, D6, D8, D10, D12, D20)


class DiceTest(unittest.TestCase):
    def validate_die(self, die):
        for _ in range(100):
            roll = die.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, die.sides)

    def test_presets(self):
        for die in [D4, D6, D8, D10, D12, D20]:
            self.validate_die(die)

    def test_arbitrary_die(self):
        self.validate_die(Dice(7))


if __name__ == '__main__':
    unittest.main()
