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
        super().__init__(type)
        self.msg = msg
    def __str__(self):
        return self.msg
        
class StatusEvent(Event):
    def __init__(self, fighter, type = 'status'):
        super().__init__(type)
        self.fighter = fighter
    def __str__(self):
        return '{}\'s status has changed.'.format(self.fighter)

class AttackEvent(Event):
    def __init__(self, attacker, victim, hit, damage=0, critical=False, type='attack'):
        super().__init__(type)
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
        
class DamageEvent(StatusEvent):
    def __init__(self, fighter, damage, type='damage'):
        super().__init__(fighter, type)
        self.damage = damage
    def __str__(self):
        return '{} took {} damage.'.format(self.fighter, self.damage)
        
class DeathEvent(StatusEvent):
    def __init__(self, fighter, type='death'):
        super().__init__(fighter, type)
    def __str__(self):
        return '{} died!'.format(self.fighter)
        
class HealEvent(StatusEvent):
    def __init__(self, fighter, hp, type='heal'):
        super().__init__(fighter, type)
        self.hp = hp
    def __str__(self):
        return '{} recovered {}HP.'.format(self.fighter, self.hp)
        
class EncounterEvent(Event):
    def __init__(self, encounter, type='encounter'):
        super().__init__(type)
        self.encounter = encounter
    def __str__(self):
        return Console.inst.createBanner(self.type.upper())
        
class EncounterStartEvent(EncounterEvent):
    def __init__(self, encounter, type='encounter start'):
        super().__init__(type)
        
class BattleEvent(EncounterEvent):
    def __init__(self, battle, type='battle'):
        super().__init__(battle, 'battle')
        
class ShopEvent(EncounterEvent):
    def __init__(self, shop):
        super().__init__(shop, 'shop')
        
class EncounterEndEvent(EncounterEvent):
    def __init__(self, encounter, type='encounter end'):
        super().__init__(encounter, type)
        
class VictoryEvent(EncounterEndEvent):
    def __init__(self, battle, type='victory'):
        super().__init__(battle, type)
        
class GameOverEvent(EncounterEndEvent):
    def __init__(self, battle, type='game over'):
        super().__init__(battle, type)
        
class ShopClosedEvent(EncounterEndEvent):
    def __init__(self, shop, type='shop closed'):
        super().__init__(shop, type)

class LevelUpEvent(StatusEvent):
    def __init__(self, fighter, level, type='level up'):
        super().__init__(fighter, type)
        self.level = level
    def __str__(self):
        return '{} leveled up! {} is now level {}'.format(self.fighter, self.level)
        
class XPEarnedEvent(StatusEvent):
    def __init__(self, fighter, xp, type='xp earned'):
        super().__init__(fighter, type)
        self.xp = xp
    def __str__(self):
        return '{} earned {}XP.'.format(self.fighter, self.xp)
        
class ItemObtainedEvent(StatusEvent):
    def __init__(self, fighter, item, quantity=1, type='item obtained'):
        super().__init__(fighter, type)
        self.item = item
        self.quantity = quantity
    def __str__(self):
        return '{} obtained {}x{}'.format(self.fighter, self.item, self.quantity)
        
class GoldObtainedEvent(StatusEvent):
    def __init__(self, fighter, gold, type='gold obtained'):
        super().__init__(fighter, type)
        self.gold = gold
    def __str__(self):
        return '{} obtained {}G'.format(self.fighter, self.gold)