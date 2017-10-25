import sys
import unittest
from ddt import ddt, data, unpack

from testutils import AnnotatedList

sys.path.insert(0, '../ddcrawler')
import dice # NOQA


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

    @unpack
    @data(AnnotatedList('2 number dice',
                        [dice.D10, dice.D8],
                        [1, 0]),
          AnnotatedList('3 number dice',
                        [dice.D20, dice.D4, dice.Dice(15)],
                        [1, 2, 0]),
          AnnotatedList('2 list dice',
                        [dice.Dice(['rock', 'paper', 'scissors']),
                         dice.Dice(['heads', 'tails'])],
                        [1, 0]),
          AnnotatedList('Mixed dice',
                        [dice.Dice(['rock', 'paper', 'scissors']),
                         dice.Dice([dice.D20, dice.D4]),
                         dice.D20,
                         dice.D4],
                        [3, 2, 0, 1]))
    def test_dice_are_sortable(self, dice, sort_order):
        sorted_dice = sorted(dice)
        result_order = [dice.index(d) for d in sorted_dice]
        self.assertEqual(result_order, sort_order)


if __name__ == '__main__':
    unittest.main()
