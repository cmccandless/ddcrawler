from random import randint, random, shuffle
from fighter import Fighter
from getch import getch

def printBanner(bannerText, print=print):
    mid = int(len(bannerText) / 2)
    print(''.rjust(48, '-'))
    print(bannerText[:mid].rjust(24, '-') + bannerText[mid:].ljust(24, '-'))
    print(''.rjust(48, '-'))


def selectFromList(choices, prompt='>', getch=getch, print=print, formatter=lambda x: x or 'Cancel'):
    def smartGetch():
        choice = getch(end='').decode()
        try:
            return int(choice)
        except ValueError:
            return choice
    print('\n'.join(sorted('{} - {}'.format(k, 'Cancel' if v is None else formatter(v)) for k, v in choices.items())))
    print(prompt, end='', flush=True)
    choice = None
    while choice not in choices:
        choice = smartGetch()
    print(choice)
    return choices[choice]
    
    
class Encounter:
    types = [ ('battle', .8), ('shop', 1) ]
    def __init__(self, player, getch=getch, print=print):
        if player is None:
            raise ValueError('player cannot be None')
        self.player = player
        self.getch = getch
        self.print = print
    def run(self):
        raise NotImplementedError()
    @staticmethod
    def random(player, getch=getch, print=print):
        r = random()
        type = None
        for t, weight in Encounter.types:
            if r < weight:
                type = t
                break
        if type == 'battle':
            return Battle(player, getch=getch, print=print)
        elif type == 'shop':
            return Shop(player, getch=getch, print=print)
    

class Battle(Encounter):
    def __init__(self, player, fighters=None, getch=getch, print=print):
        super().__init__(player, getch, print)
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
        getch = self.getch
        print = self.print
        choices = dict((i+1,f) for i, f in enumerate(self.fighters))
        choices['b'] = None
        print(choices)
        target = selectFromList(choices, '>', getch, print)
        if target is None:
            return False
        self.player.attack(target)
        if target.isdead():
            print('{} is dead!'.format(target.name))
            self.player.addexp(target.xp)
            self.player.gold += target.gold
            print('{} earned {}XP and {}G!'.format(self.player.name, target.xp, target.gold))
            self.fighters.remove(target)
        return True
    def useitem(self):
        getch = self.getch
        print = self.print
        def handler(consumables):
            if len(consumables) == 0:
                print('No usable items.')
                return []
            # items = list(enumerate(consumables.items()))
            # for i, entry in items:
                # name, items = entry
                # quantityStr = '' if len(items) == 1 else '[x{}]'.format(len(items))
                # print('{}. {}{}'.format(i + 1, name, quantityStr))
            choices = dict((i + 1, ch) for i, ch in enumerate(consumables.keys()))
            choices['b'] = None
            def formatter(choice):
                items = consumables[choice]
                quantityStr = '' if len(items) == 1 else '[x{}]'.format(len(items))
                return '{}{}'.format(choice, quantityStr)
            choice = selectFromList(choices, getch=getch, print=print)
            if choice is None:
                return False
            return [consumables[choice][0]]
        items = self.player.inventory.use(handler)
        for item in items:
            item.use(self.player)
        return len(items) > 0
    def run(self):
        printBanner('FIGHT!')
        result = True
        while result and not self.player.isdead() and any(not f.isdead() for f in self.fighters):
            print(self.player)
            print(str(self))
            badChoice = False
            while True:
                if not badChoice:
                    print('Choose:')
                    print('[a]ttack')
                    print('[i]nventory')
                    print('[q]uit')
                    print('>', end='')
                badChoice = False
                choice = getch('', end='').decode()
                if choice.startswith('q'):
                    print('q')
                    result = False
                    break
                elif choice.startswith('a'):
                    print('a')
                    if self.attack():
                        break
                    else:
                        continue
                elif choice.startswith('i'):
                    print('i')
                    if self.useitem():
                        break
                    else:
                        continue
                else:
                    badChoice = True
            if not result:
                break
            for fighter in self.fighters:
                fighter.attack(self.player)
                if self.player.isdead():
                    break
            print('')
        result = result and not self.player.isdead()
        if result:
            printBanner('Victory!', print=print)
            #handle reward
        else:
            printBanner('GAME OVER-', print=print)
        return result


class Shop(Encounter):
    def __init__(self, player, gold=100, items=None, getch=getch, print=print):
        super().__init__(player, getch=getch, print=print)
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
        self.print('Shops coming soon!!!')
        return True