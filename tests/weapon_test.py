import sys
import unittest
from ddt import ddt, data

sys.path.insert(0, '../ddcrawler')
import weapon # NOQA


@ddt
class WeaponTest(unittest.TestCase):
    @data(*weapon.presets.keys())
    def test_load_preset(self, name):
        weapon.Weapon.preset(name)


if __name__ == '__main__':
    unittest.main()
