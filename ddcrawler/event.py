from __future__ import print_function
from console import Console


class EventHandler:
    def __init__(self, enable_console=True):
        self.__event_handlers__ = set()
        self.enable_console = enable_console

    def register(self, handler):
        self.__event_handlers__.add(handler)

    def unregister(self, handler):
        self.__event_handlers__.remove(handler)

    def __call__(self, ev):
        if self.enable_console:
            Console.inst.print(ev)
        for handler in self.__event_handlers__:
            handler(ev)


eventhandler = EventHandler()


class Event:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return '{} event'.format(self.type)


class InfoEvent(Event):
    def __init__(self, msg, type='info'):
        Event.__init__(self, type)
        self.msg = msg

    def __str__(self):
        return self.msg


class StatusEvent(Event):
    def __init__(self, fighter, type='status'):
        Event.__init__(self, type)
        self.fighter = fighter

    def __str__(self):
        return '{}\'s status has changed.'.format(self.fighter)


class AttackEvent(Event):
    def __init__(self, attacker, victim, hit, damage=0,
                 critical=False, type='attack'):
        Event.__init__(self, type)
        self.attacker = attacker
        self.victim = victim
        self.hit = hit
        self.damage = damage
        self.critical = critical

    def __str__(self):
        base = '{} attacked {}.\n'.format(self.attacker, self.victim)
        if self.hit:
            if self.critical:
                base += 'Critical hit!\n'
            base += str(DamageEvent(self.victim, self.damage))
        else:
            base += '{} missed!'.format(self.attacker)
        return base


class ItemUsedEvent(Event):
    def __init__(self, user, target, item, quantity=1, type='item used'):
        Event.__init__(self, type)
        self.user = user
        self.target = target
        self.item = item
        self.quantity = quantity

    def __str__(self):
        fmt = '{} used {} {}{} on {}.'
        target = 'themselves' if self.user == self.target else self.target
        return fmt.format(self.user,
                          self.quantity,
                          self.item.name,
                          's' if self.quantity > 1 else '',
                          target)


class DamageEvent(StatusEvent):
    def __init__(self, fighter, damage, type='damage'):
        StatusEvent.__init__(self, fighter, type)
        self.damage = damage

    def __str__(self):
        return '{} took {} damage.'.format(self.fighter, self.damage)


class DeathEvent(StatusEvent):
    def __init__(self, fighter, type='death'):
        StatusEvent.__init__(self, fighter, type)

    def __str__(self):
        return '{} died!'.format(self.fighter)


class HealEvent(StatusEvent):
    def __init__(self, fighter, hp, type='heal'):
        StatusEvent.__init__(self, fighter, type)
        self.hp = hp

    def __str__(self):
        return '{} recovered {}HP.'.format(self.fighter, self.hp)


class EncounterEvent(Event):
    def __init__(self, encounter, type='encounter'):
        Event.__init__(self, type)
        self.encounter = encounter

    def __str__(self):
        return Console.inst.createBanner(self.type.upper())


class EncounterStartEvent(EncounterEvent):
    def __init__(self, encounter, type='encounter start'):
        EncounterEvent.__init__(self, type)


class BattleEvent(EncounterEvent):
    def __init__(self, battle, type='battle'):
        EncounterEvent.__init__(self, battle, 'battle')


class ShopEvent(EncounterEvent):
    def __init__(self, shop):
        EncounterEvent.__init__(self, shop, 'shop')


class EncounterEndEvent(EncounterEvent):
    def __init__(self, encounter, type='encounter end'):
        EncounterEvent.__init__(self, encounter, type)


class VictoryEvent(EncounterEndEvent):
    def __init__(self, battle, type='victory'):
        EncounterEndEvent.__init__(self, battle, type)


class GameOverEvent(EncounterEndEvent):
    def __init__(self, battle, type='game over'):
        EncounterEndEvent.__init__(self, battle, type)


class ShopClosedEvent(EncounterEndEvent):
    def __init__(self, shop, type='shop closed'):
        EncounterEndEvent.__init__(self, shop, type)


class LevelUpEvent(StatusEvent):
    def __init__(self, fighter, level, type='level up'):
        StatusEvent.__init__(self, fighter, type)
        self.level = level

    def __str__(self):
        return '{} leveled up! {} is now level {}'.format(self.fighter,
                                                          self.level)


class XPEarnedEvent(StatusEvent):
    def __init__(self, fighter, xp, type='xp earned'):
        StatusEvent.__init__(self, fighter, type)
        self.xp = xp

    def __str__(self):
        return '{} earned {}XP.'.format(self.fighter, self.xp)


class ItemObtainedEvent(StatusEvent):
    def __init__(self, fighter, item, quantity=1, type='item obtained'):
        StatusEvent.__init__(self, fighter, type)
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return '{} obtained {}x{}'.format(self.fighter,
                                          self.item,
                                          self.quantity)


class GoldObtainedEvent(StatusEvent):
    def __init__(self, fighter, gold, type='gold obtained'):
        StatusEvent.__init__(self, fighter, type)
        self.gold = gold

    def __str__(self):
        return '{} obtained {}G'.format(self.fighter, self.gold)
