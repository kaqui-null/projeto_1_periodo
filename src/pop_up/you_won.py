import curses

def  you_won(win):
    win.clear()
    curses.curs_set(0)
    curses.resize_term(35,135)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)

    youWon = "YOU WON!!"
    y,x = win.getmaxyx()

    y= y//2
    x = x//2-len(youWon)

    while 1:

        win.refresh()

        win.addstr(y,x, youWon)

        win.refresh()
        curses.napms(1000)

        win.attron(GREEN_AND_BLACK)
        win.addstr(y,x, youWon)
        win.attroff(GREEN_AND_BLACK)

        win.refresh()
        curses.napms(1000)

    win.getch()

