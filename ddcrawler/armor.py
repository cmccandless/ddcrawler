from item import Item


class Armor(Item):
    def __init__(self, ac=0, name='armor'):
        Item.__init__(self, name)
        self.ac = ac


no_armor = Armor(0, 'no armor')
