import curses
from curses import wrapper


from player import Player

# coloquem o tamanho do mapa aqui ou mudem a variável na inicialização tbm
Y = 0
X = 0
WINDOW_SIZE = (Y, X)

# A origem do player
DIRECTION = "up"
MAP_ORIGIN = (Y, X, DIRECTION)

def main(stdsrc):
    stdsrc.nodelay(True)

    try:
        curses.curs_set(0)
    except:
        pass

    
    player = Player(WINDOW_SIZE, MAP_ORIGIN)

    game_running = True
    while game_running:
        try:
            key = stdsrc.getch()
        except:
            key = None

        if key == 27:
            break
        else:
            continue


# inicialização na função main em main.py
if __name__ == "__main__":
   wrapper(main) 









