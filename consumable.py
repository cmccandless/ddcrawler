from item import Item
class Consumable(Item):
    def __init__(self, name='consumable', value=0, effect=None):
        super().__init__(name, value, True)
        self.effect = effect
    def use(self, fighter):
        if self.effect is not None:
            self.effect(fighter)
            
class HealthPotion(Consumable):
    def __init__(self, name='health potion', value=7, factor=25):
        def heal(fighter, factor=factor):
            fighter.health = min(fighter.health + factor, fighter.maxhealth)
        super().__init__('{}({})'.format(name, factor), value, heal)