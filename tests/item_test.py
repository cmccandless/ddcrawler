import sys
import unittest

sys.path.insert(0, '../ddcrawler')
from item import Item


class ItemTest(unittest.TestCase):
    def test_can_specify_value(self):
        item = Item('my_item', 5)
        self.assertEqual(item.name, 'my_item')
        self.assertEqual(item.value, 5)

    def test_not_consumeable_by_default(self):
        item = Item('my_item')
        self.assertIs(item.consumeable, False)

    def test_create_consumeable_item(self):
        """
            Note: it is best practice to use the Consumeable class
        """
        item = Item('my_item', consumeable=True)
        self.assertIs(item.consumeable, True)


if __name__ == '__main__':
    unittest.main()
