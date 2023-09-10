import curses
from curses import wrapper

def print_menu(win, selected_opcoes_idx):
    menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

    win.clear()

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    MAGENTA_AND_GREEN = curses.color_pair(1)
   
    h, w = win.getmaxyx()

    for idx, opcoes in enumerate(menu):
        x = w//2 - len(opcoes)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_opcoes_idx:
            win.attron(MAGENTA_AND_GREEN)
            win.addstr(y, x, opcoes)
            win.attroff(MAGENTA_AND_GREEN)
        else: 
            win.addstr(y, x, opcoes)

    win.refresh()

def menu(win):
    menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

    opcaoAtual_opcoes_idx = 0
    print_menu(win, opcaoAtual_opcoes_idx)


    while 1: 
        key = win.getch()

        win.clear()

        if key == curses.KEY_UP and opcaoAtual_opcoes_idx > 0:
            opcaoAtual_opcoes_idx -= 1
        elif key == curses.KEY_DOWN and opcaoAtual_opcoes_idx < len(menu)-1:
            opcaoAtual_opcoes_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            win.addstr(0, 0, "voce selecionou {}".format(menu[opcaoAtual_opcoes_idx]))
            win.refresh()
            win.getch()
            if opcaoAtual_opcoes_idx == len(menu)-1:
                break

        print_menu(win, opcaoAtual_opcoes_idx)

        win.refresh()
wrapper(menu)