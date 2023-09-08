import curses


class Mapa1:
    def __init__(self, win):
        self.win = win
#
    def desenhando_salas(self, altura, comprimento, y, x):
        for i in range(y, y + altura):
            self.win.addstr(i, x, '.' * comprimento)

#
    def imprimindo_salas(self):
        numero_salas = 7

        dimensoes_salas = [
            [8,16], #[y,x]
            [9,13],
            [10,15], 
            [6,30],
            [15,15],
            [8,23],
            [8,24] 
        ]

        coordenadas_salas = [
            [3,5], 
            [22,35],
            [19,5], 
            [3,65],
            [13,110],
            [9,30],
            [18,68] 
        ]

        for i in range(numero_salas):

            altura = dimensoes_salas[i][0]
            comprimento = dimensoes_salas[i][1]
            y = coordenadas_salas[i][0]
            x = coordenadas_salas[i][1]

        
            self.desenhando_salas(altura, comprimento, y, x) 
            
            window = self.win.subwin(altura+2, comprimento+2, y-1, x-1)
            window.border()
            
#
    def desenhando_corredor_vertical(self, y, x, vertical):
        for i in range(y, y + vertical):
            self.win.addstr(i,x, ".")

#
    def desenhando_corredor_horizontal(self, y, x, horizontal):
        for i in range(x, x+horizontal):
            self.win.addstr(y,i, ".")

#
    def imprimindo_corredores(self):

        dimensoes_vertical = [
            (6), 
            (2), 
            (3), 
            (9),
            (2), 
            (2), 
            (3),
            (2),
            (5), 
            (2), 
        ]

        coordenadas_vertical = [
            [11,6],
            [17,18],
            [29,6],
            [23,27],
            [29,78],
            [28,124],
            [10,111],
            [8,105],
            [4,30],
            [16,69]
        ]

        dimensoes_horizontal = [
            (12),
            (20),
            (8), 
            (30), 
            (45),
            (6),
            (10), 
            (35), 
            (16), 
        ]

        coordenadas_horizontal = [
            [16,7],
            [31,7],
            [22,27],
            [30,48],
            [29,79],
            [10,105],
            [8,95],
            [3,30],
            [16,53]
        ]
        
        for j in range(len(coordenadas_vertical)):

            vertical = dimensoes_vertical[j]
            y_vertical = coordenadas_vertical[j][0]
            x_vertical = coordenadas_vertical[j][1]

            self.desenhando_corredor_vertical(y_vertical, x_vertical, vertical)
            
            
        for k in range(len(coordenadas_horizontal)):
    
            horizontal = dimensoes_horizontal[k]
            y_horizontal = coordenadas_horizontal[k][0]
            x_horizontal = coordenadas_horizontal[k][1]

            #imprimindo corredor horizontal
            self.desenhando_corredor_horizontal( y_horizontal, x_horizontal, horizontal)

    def draw(self):
        self.imprimindo_salas()#
        self.imprimindo_corredores()
        
