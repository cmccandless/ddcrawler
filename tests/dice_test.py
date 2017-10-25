#!/usr/bin/env python
import sys
import unittest
from ddt import ddt, data, unpack

from testutils import AnnotatedList

sys.path.insert(0, '../ddcrawler')
import dice


@ddt
class DiceTest(unittest.TestCase):
    @data(dice.D4,
          dice.D6,
          dice.D8,
          dice.D10,
          dice.D12,
          dice.D20,
          dice.Dice(7),
          dice.Dice(['heads', 'tails']))
    def test_die(self, die):
        for _ in range(100):
            roll = die.roll()
            self.assertIn(roll, die)

    @unpack
    @data(AnnotatedList('D9', 9, True),
          AnnotatedList('str_list', ['rock', 'paper', 'scissors'], True),
          AnnotatedList('D_multi', [dice.D4, dice.D6, dice.D8], True),
          AnnotatedList('str', 'invalid', False),
          AnnotatedList('float', 2.3, False))
    def test_valid_die(self, sides, is_valid):
        if is_valid:
            dice.Dice(sides)
        else:
            with self.assertRaises(ValueError):
                dice.Dice(sides)


if __name__ == '__main__':
    unittest.main()
