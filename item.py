class Item:
    def __init__(self, name, value=0, consumable=False):
        self.name = name
        self.value = value
        self.consumable = consumable
    def __str__(self):
        return self.name + '(C)' if self.consumable else self.name