#!/usr/bin/env python
import unittest
from ddt import ddt, data

from dice import (Dice, D4, D6, D8, D10, D12, D20)


@ddt
class DiceTest(unittest.TestCase):
    @data(D4, D6, D8, D10, D12, D20, Dice(7))
    def test_die(self, die):
        for _ in range(100):
            roll = die.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, die.sides)


if __name__ == '__main__':
    unittest.main()
