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

    
    player = Player(stdsrc, WINDOW_SIZE, MAP_ORIGIN, 3)

    game_running = True
    while game_running:
        try:
            key = stdsrc.getkey()
        except:
            key = None

        if key == "q":
            break

        stdsrc.erase()
        player.walk(key)
        player.draw_sprite()
        stdsrc.refresh()
     

if __name__ == "__main__":
   wrapper(main) 









