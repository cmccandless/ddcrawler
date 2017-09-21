from player import Player
from encounter import Encounter
from getch import getch
from console import console

class Game:
    def __init__(self):
        self.player = Player(input('Name: '))
        from consumable import HealthPotion
        for _ in range(3):
            self.player.inventory.add(HealthPotion())
    def play(self):
        result = True
        while result:
            encounter = Encounter.random(self.player)
            result = encounter.run()
            console.print('')
        console.print(self.player.stats(True))
        
	
if __name__ == '__main__':
    Game().play()