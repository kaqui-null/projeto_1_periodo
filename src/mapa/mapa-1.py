import curses
from curses import wrapper
from curses import textpad


def criando_sala(stdscr, y, x, height, width):
    textpad.rectangle(stdscr, y, x, y + height, x + width)
    return (y, x, height, width)

def mapa_1(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    #salas | ainda vou alterar os tamanhos das salas
    salas = [
        criando_sala(stdscr, 2, 5, 5, 10),
        criando_sala(stdscr, 8, 20, 6, 8),
        criando_sala(stdscr, 15, 5, 8, 12),
        criando_sala(stdscr, 2, 40, 4, 10),
        criando_sala(stdscr, 12, 35, 5, 15),
        criando_sala(stdscr, 5, 65, 7, 10),
        criando_sala(stdscr, 15, 60, 6, 12),
    ]

    for i in range(len(salas) - 1):
        y1, x1, _, _ = salas[i]
        y2, x2, _, _ = salas[i + 1]
    
    stdscr.refresh()
    stdscr.getch()

wrapper(mapa_1)



