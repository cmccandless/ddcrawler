from player import Player
from encounter import Encounter
from getch import getch

class Game:
    def __init__(self, getch=getch, print=print):
        self.player = Player(input('Name: '), print=print)
        self.getch = getch
        self.print = print
    def play(self):
        result = True
        while result:
            encounter = Encounter(self.player, getch=self.getch, print=self.print)
            result = encounter.run()
            self.print('')
        self.print(str(self.player))
        
	
if __name__ == '__main__':
    Game().play()