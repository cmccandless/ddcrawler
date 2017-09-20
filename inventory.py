from getch import getch
from item import Item
from itertools import groupby

class Inventory:
    def __init__(self, items=[]):
        self.items = items
    def add(self, item):
        if not isinstance(item, Item):
            raise ValueError('not an item')
        self.items.append(item)
    def remove(self, item):
        if not isinstance(item, Item):
            raise ValueError('not an item')
        elif item not in self.items:
            raise ValueError('cannot remove item: item not in inventory')
        self.items.remove(item)
    def use(self, handler=None):
        consumables = sorted(filter(lambda i: i.consumable, self.items), key=lambda i: i.name)
        consumables = dict((k, list(g)) for k, g in groupby(consumables, key=lambda i: i.name))
        if handler is not None:
            return handler(consumables)
        return []
    def __str__(self):
        return '\n'.join(str(i) for i in self.items)