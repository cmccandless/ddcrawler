import sys
import unittest
from ddt import ddt, data

sys.path.insert(0, '../ddcrawler')
import spell # NOQA
from player import Player


@ddt
class SpellTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('test_player')

    @data(*spell.presets.keys())
    def test_load_preset(self, name):
        spell.Spell.preset(self.player, name)


if __name__ == '__main__':
    unittest.main()
