from player *
from encounter import Encounter
from getch import getch
from event import *

class Game:
    def __init__(self, enable_console=True):
        self.player = Player(Console.inst.input('Name: '))
        self.enable_console(enable_console)
        
        ## Test Code
        # from consumeable import Consumeable
        # for _ in range(3):
            # self.player.inventory.add(Consumeable.preset('Minor Health Potion'))
            # self.player.inventory.add(Consumeable.preset('Cherry Bomb'))
        # from spell import Spell
        # self.player.spells['Fireball'] = Spell.preset(self, 'Fireball')
    def enable_console(enable=True):
        eventhandler.enable_console = enable
        
    def play(self):
        result = True
        while result:
            encounter = Encounter.random(self.player)
            result = encounter.run()
            eventhandler(InfoEvent(''))
        eventhandler(InfoEvent(self.player.stats(True) + '\n'))
        
        # Score = Gold + (sum-value of Inventory / 10) + (XP Earned)
        score = self.player.gold
        score += sum(i.value for i in self.player.inventory)
        score += int((self.player.level - 1) * 1.1 * BASE_XP_NEEDED / 10) + self.player.xp
        eventhandler(InfoEvent('Score: {}'.format(score)))
        
	
if __name__ == '__main__':
    Game().play()