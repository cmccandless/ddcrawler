#!/usr/bin/env python
import unittest
from ddt import ddt, data, unpack

from dice import (Dice, D4, D6, D8, D10, D12, D20)


@ddt
class DiceTest(unittest.TestCase):
    @data(D4, D6, D8, D10, D12, D20, Dice(7), Dice(['heads', 'tails']))
    def test_die(self, die):
        for _ in range(100):
            roll = die.roll()
            self.assertIn(roll, die)

    @data((9, True),
          (['rock', 'paper', 'scissors'], True),
          ([D4, D6, D8], True),
          ('invalid', False),
          (2.3, False))
    @unpack
    def test_valid_die(self, sides, is_valid):
        if is_valid:
            Dice(sides)
        else:
            with self.assertRaises(ValueError):
                Dice(sides)


if __name__ == '__main__':
    unittest.main()
