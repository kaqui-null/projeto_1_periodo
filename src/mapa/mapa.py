import curses
from curses import textpad

class Mapa_test:
    def __init__(self, stdsrc):
        self.stdsrc = stdsrc
        self.y = 20
        self.x = 20
        self.begin_y = int(round((stdsrc.getmaxyx()[0] - self.y)/2))
        self.begin_x = int(round((stdsrc.getmaxyx()[1] - self.x)/2))
    
    def new_win(self):
        window = curses.newwin(self.y, self.x,self.begin_y, self.begin_x)
        window.border()
        return window