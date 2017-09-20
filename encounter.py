from random import randint, shuffle
from fighter import Fighter

class Encounter:
    def __init__(self, level = 1, fighters = None):
        self.level = level
        self.fighters = fighters
        if fighters is None:
            self.fighters = []
            while len(self.fighters) == 0:
                fighterClasses = list(Fighter.presets)
                shuffle(fighterClasses)
                for fighterClass in fighterClasses:
                    if len(self.fighters) == level:
                        break
                    for _ in range(0, level - len(self.fighters)):
                        self.fighters.append(Fighter.preset(fighterClass))
    def __str__(self):
        return '\n'.join('{}. {}'.format(i+1,f) for i,f in enumerate(self.fighters))
    def run(self, player, input=input):
        print('NEW ENCOUNTER!')
        while not player.isdead() and any(not f.isdead() for f in self.fighters):
            print(player)
            print(str(self))
            index = int(input('Target: ')) - 1
            target = self.fighters[index]
            player.attack(target)
            if target.isdead():
                print('{} is dead!'.format(target.name))
                player.addexp(target.xp)
                print('{} earned {}XP!'.format(player.name, target.xp))
                self.fighters.remove(target)
            for fighter in self.fighters:
                fighter.attack(player)
                if player.isdead():
                    break
            print('')
        return not player.isdead()