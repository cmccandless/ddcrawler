from player import Player
from fighter import Fighter
from getch import getch
from encounter import Encounter

def inputch(prompt):
    print(prompt, end='', flush=True)
    ch = getch()
    print('')
    return ch

def run():
    player = Player(input('Name: '))
    result = True
    while result:
        encounter = Encounter(player.level)
        result = encounter.run(player, inputch)
    print('GAME OVER!')
    print(str(player))
        
	
if __name__ == '__main__':
    run()