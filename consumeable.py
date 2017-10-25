from item import Item
from event import (eventhandler, DamageEvent, HealEvent, InfoEvent)
from fighter import Fighter

with open('consumeable.json', 'r') as f:
    from json import load
    presets = load(f)


class Consumeable(Item):
    def __init__(self, name='consumeable', value=0, effect=None, scope=None):
        super().__init__(name, value, True)
        self.effect = effect
        self.scope = scope

    def use(self, target):
        if target is None:
            raise ValueError('target cannot be None!')
        if self.effect is not None:
            self.effect(target)

    @staticmethod
    def preset(name):
        if name in presets:
            data = {'name': name}
            _class = None
            for k, v in presets[name].items():
                if k == 'type':
                    _class = eval(v)
                else:
                    data[k] = v
            if _class is None:
                raise ValueError('incomplete preset "{}"!'.format(name))
            return _class(**data)
        else:
            raise ValueError('unknown preset "{}"'.format(name))


class HealthPotion(Consumeable):
    def __init__(self, name='health potion', value=7, factor=25):
        super().__init__(name, value, Fighter)
        self.factor = factor

    def use(self, fighter):
        if fighter is None:
            raise ValueError('fighter cannot be None!')
        healed = min(self.factor, fighter.maxhealth - fighter.health)
        if healed == 0:
            eventhandler(InfoEvent('This item cannot be used now!'))
            return False
        fighter.health += healed
        eventhandler(HealEvent(fighter, healed))
        return True


class Bomb(Consumeable):
    def __init__(self, name='bomb', value=20, damage=10):
        super().__init__(name, value, Fighter)
        self.damage = damage

    def use(self, target):
        if target is None:
            raise ValueError('target cannot be None!')
        target.health -= self.damage
        eventhandler(DamageEvent(target, self.damage))
        return True
