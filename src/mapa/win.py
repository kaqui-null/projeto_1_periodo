import curses


class Win:

    def __init__(self, stdsrc, y, x):
        self.stdsrc = stdsrc
        self.y = y
        self.x = x

    def new_win(self):
        return curses.newwin(self.y, self.x) 