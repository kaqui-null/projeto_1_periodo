import curses
from curses import textpad
from curses import wrapper

class Mapa:

    def mapa(stdscr):

        curses.curs_set(False)
        y, x = stdscr.getmaxyx()
        
        textpad.rectangle(stdscr, 5, 30, y-5, x-30)

        stdscr.getch()
        stdscr.refresh()
        
    wrapper(mapa)
