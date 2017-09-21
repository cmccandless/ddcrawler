from random import randint, random, shuffle
from fighter import Fighter
from getch import getch
from console import console

def printBanner(bannerText):
    mid = int(len(bannerText) / 2)
    console.print(''.rjust(48, '-'))
    console.print(bannerText[:mid].rjust(24, '-') + bannerText[mid:].ljust(24, '-'))
    console.print(''.rjust(48, '-'))


def selectFromList(choices, prompt='>', formatter=lambda x: x or 'Cancel'):
    console.print('\n'.join(sorted('{} - {}'.format(k, 'Cancel' if v is None else formatter(v)) for k, v in choices.items())))
    console.print(prompt, end='', flush=True)
    choice = None
    while choice not in choices:
        choice = console.smart_getch()
    console.print(choice)
    return choices[choice]
    
    
class Encounter:
    types = [ ('battle', .8), ('shop', 1) ]
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
                fighterClasses = list(Fighter.presets)
                shuffle(fighterClasses)
                for fighterClass in fighterClasses:
                    if len(self.fighters) == player.level:
                        break
                    for _ in range(0, player.level - len(self.fighters)):
                        self.fighters.append(Fighter.preset(fighterClass))
    def __str__(self):
        return '\n'.join('{}. {}'.format(i+1,f) for i,f in enumerate(self.fighters))
    def attack(self):
        choices = dict((i+1,f) for i, f in enumerate(self.fighters))
        if len(choices) > 1:
            choices['b'] = None
            target = console.menu(choices)
            if target is None:
                return False
        else:
            target = self.fighters[0]
        self.player.attack(target)
        if target.isdead():
            console.print('{} is dead!'.format(target.name))
            self.player.addexp(target.xp)
            self.player.gold += target.gold
            console.print('{} earned {}XP and {}G!'.format(self.player.name, target.xp, target.gold))
            self.fighters.remove(target)
        return True
    def useitem(self):
        def handler(consumables):
            if len(consumables) == 0:
                console.print('No usable items.')
                return []
            choices = dict((i + 1, ch) for i, ch in enumerate(consumables.keys()))
            choices['b'] = None
            def formatter(choice):
                items = consumables[choice]
                quantityStr = '' if len(items) == 1 else '[x{}]'.format(len(items))
                return '{}{}'.format(choice, quantityStr)
            choice = console.menu(choices, formatter=formatter)
            if choice is None:
                return []
            return [consumables[choice][0]]
        while True:
            items = self.player.inventory.use(handler)
            if len(items) == 0:
                return False
            item = items[0]
            targets = [self.player]
            targets.extend(self.fighters)
            choices = dict((i + 1, t) for i, t in enumerate(targets))
            choices['b'] = None
            choice = console.menu(choices, 'Use on whom?')
            if item is None or not item.use(choice):
                continue
            break
        return True
    def run(self):
        console.printBanner('FIGHT!')
        result = True
        while result and not self.player.isdead() and any(not f.isdead() for f in self.fighters):
            console.print(self.player)
            console.print(str(self))
            while True:
                choices = {
                    'a':'Attack', 
                    'i':'Inventory',
                    'q':'Quit'
                }
                console.print('Choose:')
                choice = console.menu(choices).lower()
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
            for fighter in self.fighters:
                fighter.attack(self.player)
                if self.player.isdead():
                    break
            console.print('')
        result = result and not self.player.isdead()
        if result:
            printBanner('Victory!')
            #handle reward
        else:
            printBanner('GAME OVER-')
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
        console.print('Shops coming soon!!!')
        return True