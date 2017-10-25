import sys
import unittest
from ddt import ddt, data

sys.path.insert(0, '../ddcrawler')
import fighter


@ddt
class FighterTest(unittest.TestCase):
    @data(*fighter.presets.keys())
    def test_load_preset(self, name):
        fighter.Fighter.preset(name)


if __name__ == '__main__':
    unittest.main()
