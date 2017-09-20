from random import randint, shuffle
from fighter import Fighter
from getch import getch

def printBanner(bannerText, print=print):
    mid = int(len(bannerText) / 2)
    print(''.rjust(48, '-'))
    print(bannerText[:mid].rjust(24, '-') + bannerText[mid:].ljust(24, '-'))
    print(''.rjust(48, '-'))

class Encounter:
    def __init__(self, player, fighters = None, getch=getch, print=print):
        if player is None:
            raise ValueError('player cannot be None')
        self.player = player
        self.fighters = fighters
        self.getch = getch
        self.print = print
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
    def run(self):
        getch = self.getch
        print = self.print
        printBanner('FIGHT!')
        result = True
        while result and not self.player.isdead() and any(not f.isdead() for f in self.fighters):
            print(self.player)
            print(str(self))
            badChoice = False
            while True:
                if not badChoice:
                    print('[a]ttack')
                    print('[q]uit')
                    print('Action: ', end='')
                badChoice = False
                choice = getch('', end='').decode()
                if choice.startswith('q'):
                    print('q')
                    result = False
                    break
                elif choice.startswith('a'):
                    print('a')
                    print('Target ([b]ack)', end='', flush=True)
                    while True:
                        try:
                            choice = getch(end='').decode()
                            if choice.startswith('b'):
                                break
                            index = int(choice) - 1
                            break
                        except ValueError as e:
                            pass
                    print(choice)
                    if choice.startswith('b'):
                        continue
                    target = self.fighters[index]
                    self.player.attack(target)
                    if target.isdead():
                        print('{} is dead!'.format(target.name))
                        self.player.addexp(target.xp)
                        print('{} earned {}XP!'.format(self.player.name, target.xp))
                        self.fighters.remove(target)
                    break
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
        printBanner('Victory!' if result else 'GAME OVER-', print=print)
        return result