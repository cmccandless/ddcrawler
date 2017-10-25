class Item:
    def __init__(self, name, value=0, consumeable=False):
        self.name = name
        self.value = value
        self.consumeable = consumeable

    def __str__(self):
        return self.name + '(C)' if self.consumeable else self.name
