from item import Item
from itertools import groupby


class Inventory:
    def __init__(self, items=[]):
        self.items = items
        self.current = 0

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self.items.__iter__()

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

    def grouped(self, key=lambda i: True):
        items = sorted(filter(key, self.items), key=lambda i: i.name)
        return dict((k, list(g)) for k, g in
                    groupby(items, key=lambda i: i.name))

    def select(self, handler=None, key=lambda i: True):
        items = self.grouped(key)
        if handler is not None:
            return handler(items)
        return []

    def use(self, handler=None):
        return self.select(handler, lambda i: i.consumeable)

    def __str__(self):
        grp = self.grouped()
        grp_s = ['{}x{}'.format(k, len(g)) for k, g in grp.items()]
        return '\n'.join(sorted(grp_s))
