from __future__ import print_function
from random import random, shuffle
import fighter
from console import Console
from event import (eventhandler,
                   BattleEvent,
                   DeathEvent,
                   GameOverEvent,
                   GoldObtainedEvent,
                   InfoEvent,
                   ItemUsedEvent,
                   ShopClosedEvent,
                   ShopEvent,
                   VictoryEvent,
                   XPEarnedEvent)


class Encounter:
    types = [('battle', .8), ('shop', 1)]

    def __init__(self, player):
        if player is None:
            raise ValueError('player cannot be None')
        self.player = player

    def run(self):
        raise NotImplementedError()

    @staticmethod
    def random(player):
        r = random()
        type = None
        for t, weight in Encounter.types:
            if r < weight:
                type = t
                break
        if type == 'battle':
            return Battle(player)
        elif type == 'shop':
            return Shop(player)


class Battle(Encounter):
    def __init__(self, player, fighters=None):
        super().__init__(player)
        self.fighters = fighters
        if fighters is None:
            self.fighters = []
            while len(self.fighters) == 0:
                fighterClasses = list(fighter.presets.keys())
                shuffle(fighterClasses)
                for fighterClass in fighterClasses:
                    if len(self.fighters) == player.level:
                        break
                    for _ in range(0, player.level - len(self.fighters)):
                        newFighter = fighter.Fighter.preset(fighterClass)
                        self.fighters.append(newFighter)

    def __str__(self):
        return '\n'.join('{}. {}'.format(i + 1, f.stats())
                         for i, f in enumerate(self.fighters))

    def select_target(self):
        choices = dict((i + 1, f) for i, f in enumerate(self.fighters))
        if len(choices) == 1:
            return self.fighters[0]
        choices['q'] = None
        return Console.inst.menu(choices, 'Choose a target:')

    def attack(self):
        while True:
            spell_name = self.player.select_spell()
            if spell_name is None:
                return False
            spell = self.player.spells[spell_name]
            targets = []
            for _ in range(spell.ntargets):
                target = self.select_target()
                if target is None:
                    break
                targets.append(target)
            if len(targets) < spell.ntargets:
                continue
            for target in targets:
                self.player.attack(target, spell_name)
                return True

    def useitem(self):
        def handler(consumeables):
            if len(consumeables) == 0:
                eventhandler(InfoEvent('No usable items.'))
                return []
            choices = dict((i + 1, ch) for i, ch in
                           enumerate(consumeables.keys()))
            choices['q'] = None

            def formatter(choice):
                items = consumeables[choice]
                quantityStr = ('' if len(items) == 1
                               else '[x{}]'.format(len(items)))
                return '{}{}'.format(choice, quantityStr)
            choice = Console.inst.menu(choices, formatter=formatter)
            if choice is None:
                return []
            return [consumeables[choice][0]]
        while True:
            items = self.player.inventory.use(handler)
            if len(items) == 0:
                return False
            item = items[0]
            targets = [self.player]
            targets.extend(self.fighters)
            choices = dict((i + 1, t) for i, t in enumerate(targets))
            choices['b'] = None
            choice = Console.inst.menu(choices, 'Use on whom?')
            eventhandler(ItemUsedEvent(self.player, choice, item))
            if choice is None or not item.use(choice):
                continue
            break
        return True

    def run(self):
        eventhandler(BattleEvent(self))
        result = True
        while (result and
               not self.player.isdead() and
               any(not f.isdead() for f in self.fighters)):
            eventhandler(InfoEvent(self.player.stats()))
            eventhandler(InfoEvent(str(self)))
            while True:
                choices = {
                    'a': 'Attack',
                    'i': 'Inventory',
                    'q': 'Quit'
                }
                choice = Console.inst.menu(choices, 'Choose:').lower()
                if choice.startswith('q'):
                    result = False
                    break
                elif choice.startswith('a'):
                    if self.attack():
                        break
                    else:
                        continue
                elif choice.startswith('i'):
                    if self.useitem():
                        break
                    else:
                        continue
            if not result:
                break
            for _fighter in self.fighters:
                if _fighter.isdead():
                    eventhandler(DeathEvent(_fighter.name))
                    self.player.addexp(_fighter.xp)
                    self.player.gold += _fighter.gold
                    eventhandler(XPEarnedEvent(self.player, _fighter.xp))
                    eventhandler(GoldObtainedEvent(self.player, _fighter.gold))
                    self.fighters.remove(_fighter)
                else:
                    fighter.attack(self.player)
                    if self.player.isdead():
                        break
            Console.inst.print('')
        if self.player.isdead():
            eventhandler(DeathEvent(self.player))
            result = False
        if result:
            eventhandler(VictoryEvent(self))
            # handle reward
        else:
            eventhandler(GameOverEvent(self))
        return result


class Shop(Encounter):
    def __init__(self, player, gold=100, items=None):
        super().__init__(player)
        self.gold = gold
        self.items = items
        if items is None:
            # generate items
            pass

    def sell(self, player, item):
        pass

    def buy(self, player, item):
        pass

    def run(self):
        eventhandler(ShopEvent(self))
        eventhandler(InfoEvent('Shops coming soon!!!'))
        eventhandler(ShopClosedEvent(self))
        return True
