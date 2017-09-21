from getch import getch
from math import floor, ceil

class Console:
    def __init__(self, getch=getch, print=print, input=input, data_handler=None):
        self.__getch__ = getch
        self.__print__ = print
        self.__input__ = input
        self.data_handler = data_handler
        self.menu_formatter = self.default_menu_formatter
    def print(self, *objects, sep=' ', end='\n', flush=True):
        self.__print__(*objects, sep=sep, end=end, flush=flush)
    def getch(self, prompt='', echo=False, end='\n'): 
        return self.__getch__(prompt, echo, end)
    def input(self, prompt=''):
        return self.__input__(prompt)
    def smart_getch(self, prompt='', echo=False, end='\n', choices=None):
        choice = None
        if choices is not None and None in choices:
            raise ValueError('None is not a valid choice.')
        while choice is None or (choices is not None and choice not in choices):
            choice = self.getch(end='').decode()
            try:
                choice = float(choice)
            except ValueError:
                try:
                    choice = int(choice)
                except ValueError:
                    pass
        return choice
    def printBanner(self, bannerText, width=48):
        mid = int(len(bannerText) / 2)
        self.print(''.rjust(width, '-'))
        self.print(bannerText[:mid].rjust(int(floor(width / 2)), '-'), end='')
        self.print(bannerText[mid:].ljust(int(ceil(width / 2)), '-'))
        self.print(''.rjust(width, '-'), flush=True)
    def default_menu_formatter(self, choice):
        return 'Cancel' if choice is None else str(choice)
    def menu(self, choices, title=None, prompt='>', formatter=None, echo=True):
        if formatter is None:
            formatter = self.menu_formatter
        if title is not None:
            console.print(title)
        s_choices = ['[{}] {}'.format(k,
                                      'Cancel' if v is None else formatter(v))
                     for k, v in choices.items()]
        console.print('\n'.join(sorted(s_choices)))
        if echo:
            console.print(prompt, end='', flush=True)
        choice = None
        while choice not in choices:
            choice = console.smart_getch()
        if echo:
            console.print(choice)
        return choices[choice]

        
console = Console()