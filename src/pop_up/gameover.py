import curses

def game_over(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.resize_term(35,135)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)

    gameOver = "GAME OVER!!"
    y,x = stdscr.getmaxyx()

    y= y//2
    x = x//2-len(gameOver)

    while 1:

        stdscr.refresh()

        stdscr.addstr(y,x, gameOver)

        stdscr.refresh()
        curses.napms(1000)

        stdscr.attron(RED_AND_BLACK)
        stdscr.addstr(y,x, gameOver)
        stdscr.attroff(RED_AND_BLACK)

        stdscr.refresh()
        curses.napms(1000)

    stdscr.getch()

