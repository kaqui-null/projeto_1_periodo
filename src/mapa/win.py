import curses


class Win:

    def __init__(self, stdsrc, y, x):
        self.stdsrc = stdsrc
        self.y = 35
        self.x = 135

    def new_win(self):
        return curses.newwin(self.y, self.x) 