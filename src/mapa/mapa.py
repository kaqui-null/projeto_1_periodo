'''
AINDA VOU ORGANIZAR MELHOR O CODIGO DOS CORREDORES.
AINDA ESTA FALTANDO COLOCAR OS CORREDORES.

salas -> "."
corredores -> "#"

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
        
        #criando as subjanelas e adicionando as bordas
        window = stdscr.subwin(altura, comprimento, y, x)
        window.border()

############################### CORREDORES #########################################

#funcao para desenhar corredor vertical
def desenhando_corredor_vertical(stdscr, y, x, vertical):
    for i in range(y, y+vertical):
        stdscr.addstr(i,x, "#")

#funcao para desenhar corredor horizontal
def desenhando_corredor_horizontal(stdscr, y, x, horizontal):
    for i in range(x, x+horizontal):
        stdscr.addstr(y,i, "#")

#funcao para imprimir os corredores na tela
def imprimindo_corredores(stdscr):
    #corredor vertical
    dimensoes_vertical = [
        (10),
        (3),
    ]

    dimensoes_horizontal = [

    ]

    #coordenadas corredor, sempre (y,x)
    coordenadas_vertical = [
        [11,7],
        [29,17],
    ]

    coordenadas_horizontal = [

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

#funcao principal do mapa
def mapa(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    imprimindo_salas(stdscr)
    imprimindo_corredores(stdscr)


    stdscr.refresh()
    stdscr.getch()
curses.wrapper(mapa)
