import curses

class Menu:
    def __init__(self, win, stdsrc):
        self.win = win
        self.stdsrc = stdsrc

    def print_menu(self, selected_opcoes_idx):
        menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

        self.win.clear()

        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
        MAGENTA_AND_GREEN = curses.color_pair(1)
    
        h, w = self.win.getmaxyx()

        for idx, opcoes in enumerate(menu):
            x = w//2 - len(opcoes)//2
            y = h//2 - len(menu)//2 + idx
            if idx == selected_opcoes_idx:
                self.win.attron(MAGENTA_AND_GREEN)
                self.win.addstr(y, x, opcoes)
                self.win.attroff(MAGENTA_AND_GREEN)
            else: 
                self.win.addstr(y, x, opcoes)

        self.win.refresh()

    def menu(self):
        menu = ['opcao 1', 'opcao 2', 'opcao 3', 'exit']

        opcaoAtual_opcoes_idx = 0
        self.print_menu(opcaoAtual_opcoes_idx)

        while 1: 
            key = self.win.getch()

            self.win.clear()

            if key == curses.KEY_UP and opcaoAtual_opcoes_idx > 0:
                opcaoAtual_opcoes_idx -= 1
            elif key == curses.KEY_DOWN and opcaoAtual_opcoes_idx < len(menu)-1:
                opcaoAtual_opcoes_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.win.addstr(0, 0, "voce selecionou {}".format(menu[opcaoAtual_opcoes_idx]))
                self.win.refresh()
                self.win.getch()
                if opcaoAtual_opcoes_idx == len(menu)-1:
                    break

            self.print_menu(opcaoAtual_opcoes_idx)
            self.win.refresh()
            self.stdsrc.refresh()

