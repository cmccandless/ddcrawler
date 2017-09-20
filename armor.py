from item import Item

class Armor(Item):
    def __init__(self, ac=0, name='no armor'):
        super().__init__(name)
        self.ac = ac