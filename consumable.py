from item import Item
class Consumable(Item):
    def __init__(self, name='consumable', value=0, effect=None):
        super().__init__(name, value, True)
        self.effect = effect
    def use(self, target):
        if self.effect is not None:
            self.effect(target)
            
class HealthPotion(Consumable):
    def __init__(self, name='health potion', value=7, factor=25):
        self.print=print
        super().__init__('{}({})'.format(name, factor), value)
        self.factor = factor
    def use(self, fighter):
        healed = min(self.factor, fighter.maxhealth - fighter.health)
        if healed == 0:
            fighter.print('This item cannot be used now!')
            return False
        fighter.health += healed
        fighter.print('{} was healed by {}HP.'.format(fighter.name, healed))
        return True