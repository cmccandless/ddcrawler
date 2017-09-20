from player import Player
from encounter import Encounter
from getch import getch

class Game:
    def __init__(self, getch=getch, print=print):
        self.player = Player(input('Name: '), print=print)
        from consumable import HealthPotion
        for _ in range(3):
            self.player.inventory.add(HealthPotion())
        self.getch = getch
        self.print = print
    def play(self):
        result = True
        while result:
            encounter = Encounter.random(self.player, getch, print)
            result = encounter.run()
            self.print('')
        self.print(str(self.player))
        
	
if __name__ == '__main__':
    Game().play()