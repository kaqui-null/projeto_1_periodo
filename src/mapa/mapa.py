'''
AINDA VOU ORGANIZAR MELHOR O CODIGO DOS CORREDORES.
AINDA ESTA FALTANDO COLOCAR OS CORREDORES.

salas -> "."
corredores -> "."

'''

import curses
from curses import wrapper

############################### SALAS ##########################################

#funcao para desenhar as salas
def desenhando_salas(stdscr, altura, comprimento, y, x):
    for i in range(y, y + altura):
        stdscr.addstr(i, x, '.' * comprimento)

#funcao para imprimir as salas na tela
def imprimindo_salas(stdscr):
     #coloca a quantidade de salas que o mapa tera
    numero_salas = 7

    # coloca as dimensoes da sala, sempre (altura, comprimento)
    dimensoes_salas = [
        [8,16], 
        [10,13],
        [10,15], 
        [6,30],
        [15,15],
        [6,22],
        [6,15] 
    ]

    #coloca as coordenadas da sala, sempre (y,x)
    coordenadas_salas = [
        [4,5], 
        [23,35],
        [20,5], 
        [4,65],
        [14,110],
        [13,30],
        [21,70] 
    ]

    #loop para imprimir as salas
    for i in range(numero_salas):

        #passando pelos vetores das salas
        altura = dimensoes_salas[i][0]
        comprimento = dimensoes_salas[i][1]
        y = coordenadas_salas[i][0]
        x = coordenadas_salas[i][1]

       
        #imprimindo as salas
        desenhando_salas(stdscr, altura, comprimento, y, x)
        
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
        WHITE_AND_WHITE = curses.color_pair(1)

        #criando as subjanelas e adicionando as bordas
        stdscr.attron(WHITE_AND_WHITE)
        window = stdscr.subwin(altura, comprimento, y, x)
        window.border()
        stdscr.attroff(WHITE_AND_WHITE)

############################### CORREDORES #########################################

#funcao para desenhar corredor vertical
def desenhando_corredor_vertical(stdscr, y, x, vertical):
    for i in range(y, y+vertical):
        stdscr.addstr(i,x, ".")

#funcao para desenhar corredor horizontal
def desenhando_corredor_horizontal(stdscr, y, x, horizontal):
    for i in range(x, x+horizontal):
        stdscr.addstr(y,i, ".")

#funcao para imprimir os corredores na tela
def imprimindo_corredores(stdscr):

    #corredor vertical
    dimensoes_vertical = [
        (8),
        (3)
    ]

    #coordenadas corredor, sempre (y,x)
    coordenadas_vertical = [
        [11,7],
        [18,17]
    ]

    dimensoes_horizontal = [
        (10)
    ]

    coordenadas_horizontal = [
        [18,8]
    ]
    
    #loop para imprimir os corredores verticais
    for j in range(len(coordenadas_vertical)):

        #passando pelos vetores dos corredores verticais
        vertical = dimensoes_vertical[j]
        y_vertical = coordenadas_vertical[j][0]
        x_vertical = coordenadas_vertical[j][1]

        
        #imprimindo corredor vertical
        desenhando_corredor_vertical(stdscr, y_vertical, x_vertical, vertical)
        


    #loop para imprimir os corredores horizontais
    for k in range(len(coordenadas_horizontal)):

        #passando pelos vetores dos corredores horizontais 
        horizontal = dimensoes_horizontal[k]
        y_horizontal = coordenadas_horizontal[k][0]
        x_horizontal = coordenadas_horizontal[k][1]

        #imprimindo corredor horizontal
        desenhando_corredor_horizontal(stdscr, y_horizontal, x_horizontal, horizontal)

def portas(stdscr):
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    BLACK = curses.color_pair(2)

    #coordenadas das portas (y,x)
    porta = [
        [11,7]
    ]
    for i in range(len(porta)):
        y = porta[i][0]
        x = porta[i][1]
        stdscr.attron(BLACK)
        stdscr.addch(y,x, curses.ACS_BLOCK)
        stdscr.attroff(BLACK)

#funcao principal do mapa
def mapa(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    WHITE_AND_WHITE = curses.color_pair(1)

    imprimindo_salas(stdscr)
    
    stdscr.attron(curses.A_BOLD)
    stdscr.attron(WHITE_AND_WHITE)
    imprimindo_corredores(stdscr)
    stdscr.attroff(WHITE_AND_WHITE)
    stdscr.attroff(curses.A_BOLD)

    #portas(stdscr)

    stdscr.refresh()
    stdscr.getch()
curses.wrapper(mapa)
