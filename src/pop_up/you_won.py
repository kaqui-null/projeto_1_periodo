import curses
from curses import wrapper
import time

def  you_won(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.resize_term(35,135)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)

    youWon = "YOU WON!!"
    y,x = stdscr.getmaxyx()

    y= y//2
    x = x//2-len(youWon)

    while 1:

        stdscr.refresh()

        stdscr.addstr(y,x, youWon)

        stdscr.refresh()
        curses.napms(1000)

        stdscr.attron(GREEN_AND_BLACK)
        stdscr.addstr(y,x, youWon)
        stdscr.attroff(GREEN_AND_BLACK)

        stdscr.refresh()
        curses.napms(1000)

    stdscr.getch()
wrapper(you_won)

