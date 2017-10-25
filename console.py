from getch import getch
from math import floor, ceil


class Console:
    instance = None

    def __init__(self, getch=getch, print=print, input=input):
        self.__getch__ = getch
        self.__print__ = print
        self.__input__ = input
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
        while choice is None or (choices is not None and
                                 choice not in choices):
            try:
                choice = self.getch(end='').decode()
            except UnicodeDecodeError:
                continue
            try:
                f_choice = float(choice)
                try:
                    choice = int(choice)
                except ValueError:
                    choice = f_choice
            except ValueError:
                pass
        return choice

    def createBanner(self, bannerText, width=48):
        mid = int(len(bannerText) / 2)
        return '\n'.join([
            ''.rjust(width, '-'),
            (bannerText[:mid].rjust(int(floor(width / 2)), '-') +
             bannerText[mid:].ljust(int(ceil(width / 2)), '-')),
            ''.rjust(width, '-')
        ])

    def printBanner(self, bannerText, width=48):
        self.print(self.createBanner(bannerText, width))

    def default_menu_formatter(self, choice):
        return 'Cancel' if choice is None else str(choice)

    def menu(self, choices, title=None, prompt='>', formatter=None, echo=True):
        if formatter is None:
            formatter = self.menu_formatter
        if title is not None:
            self.print(title)
        s_choices = ['[{}] {}'.format(k,
                                      '[Cancel]' if v is None
                                      else formatter(v))
                     for k, v in choices.items()]
        self.print('\n'.join(sorted(s_choices)))
        if echo:
            self.print(prompt, end='', flush=True)
        choice = None
        while choice not in choices:
            choice = self.smart_getch()
        if echo:
            self.print(choice)
        return choices[choice]


Console.inst = Console()
