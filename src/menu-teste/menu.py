import curses
from curses import wrapper

def print_menu(stdscr, selected_opcoes_idx):
    menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

    stdscr.clear()

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    MAGENTA_AND_GREEN = curses.color_pair(1)
   
    h, w = stdscr.getmaxyx()

    for idx, opcoes in enumerate(menu):
        x = w//2 - len(opcoes)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_opcoes_idx:
            stdscr.attron(MAGENTA_AND_GREEN)
            stdscr.addstr(y, x, opcoes)
            stdscr.attroff(MAGENTA_AND_GREEN)
        else: 
            stdscr.addstr(y, x, opcoes)

    stdscr.refresh()

def menu(stdscr):
    menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

    opcaoAtual_opcoes_idx = 0
    print_menu(stdscr, opcaoAtual_opcoes_idx)


    while 1: 
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and opcaoAtual_opcoes_idx > 0:
            opcaoAtual_opcoes_idx -= 1
        elif key == curses.KEY_DOWN and opcaoAtual_opcoes_idx < len(menu)-1:
            opcaoAtual_opcoes_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "voce selecionou {}".format(menu[opcaoAtual_opcoes_idx]))
            stdscr.refresh()
            stdscr.getch()
            if opcaoAtual_opcoes_idx == len(menu)-1:
                break

        print_menu(stdscr, opcaoAtual_opcoes_idx)

        stdscr.refresh()
wrapper(menu)