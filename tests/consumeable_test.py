import sys
import unittest
from ddt import ddt, data

sys.path.insert(0, '../ddcrawler')
import consumeable as cable # NOQA


@ddt
class ConsumeableTest(unittest.TestCase):
    def test_generic_consumeable(self):
        item = cable.Consumeable()
        self.assertEqual(item.name, 'consumeable')

    def test_is_consumeable(self):
        item = cable.Consumeable()
        self.assertIs(item.consumeable, True)

    def test_can_specify_value(self):
        item = cable.Consumeable(value=5)
        self.assertEqual(item.value, 5)

    def test_cannot_use_on_none(self):
        item = cable.Consumeable()
        with self.assertRaisesRegexp(ValueError, 'cannot be None'):
            item.use(None)

    @data(*cable.presets.keys())
    def test_load_presets(self, name):
        cable.Consumeable.preset(name)


if __name__ == '__main__':
    unittest.main()
