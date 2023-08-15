import curses
from curses import wrapper
from curses import textpad

def criando_sala(stdscr, y_sala, x_sala, height, width):
    textpad.rectangle(stdscr, y_sala, x_sala, y_sala + height, x_sala + width)
    return (y_sala, x_sala, height, width)

def mapa_1(stdscr):

    stdscr = stdscr
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    #salas | tamanhos ajustados
    salas = [ 
        criando_sala(stdscr, 4, 5, 8, 16),
        criando_sala(stdscr, 23, 35, 10, 13),
        criando_sala(stdscr, 20, 5, 10, 15),
        criando_sala(stdscr, 4, 65, 6, 30),
        criando_sala(stdscr, 14, 110, 15, 15),
        criando_sala(stdscr, 13, 30, 6, 22),
        criando_sala(stdscr, 21, 70, 8, 15),
    ]

    corredor = [
        criando_corredor(stdscr, 20,20)
    ]

    stdscr.getch()

wrapper(mapa_1)

