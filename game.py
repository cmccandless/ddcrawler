from player import Player
from encounter import Encounter
from getch import getch
from console import Console
from event import *

class Game:
    def __init__(self):
        self.player = Player(Console.inst.input('Name: '))
        
        from consumeable import Consumeable
        for _ in range(3):
            self.player.inventory.add(Consumeable.preset('Minor Health Potion'))
        from spell import Spell
        self.player.spells['Fireball'] = Spell.preset(self, 'Fireball')
    def enable_console(enable=True):
        eventhandler.enable_console = enable
        
    def play(self):
        result = True
        while result:
            encounter = Encounter.random(self.player)
            result = encounter.run()
            eventhandler(InfoEvent(''))
        eventhandler(InfoEvent(self.player.stats(True)))
        
class TestConsole(Console):
    def input(self, prompt=''):
        return super().input('TEST' + prompt)
    def smart_getch(self, prompt='', echo=False, end='\n', choices=None):
        return super().smart_getch(prompt='TEST'+prompt, echo=echo, end=end, choices=choices)
    def print(self, *objects, sep=' ', end='\n', flush=True):
        objects = tuple(['TEST'] + list(objects))
        return print(*objects, sep, end, flush)
        
        
	
if __name__ == '__main__':
    Game().play()