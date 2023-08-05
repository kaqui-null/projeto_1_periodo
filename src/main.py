import curses
from curses import wrapper

from player import Player
from enemy import Enemy

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
    enemy = Enemy(stdsrc, 3, 1, WINDOW_SIZE[0] + 3, WINDOW_SIZE[1] + 1, DIRECTION, [player.origin_y, player.origin_x])

    game_running = True
    key = 0
    while game_running:
        player.draw_sprite()
        enemy.draw_sprite()
        
        try:
            key = stdsrc.getkey()
        except:
            key = None

        if key != None:
            if key == "q":
                break
        
            stdsrc.erase()
            player.walk(key)
            player.draw_sprite()
            enemy.draw_sprite()

            enemy.player_pos = [player.origin_y, player.origin_x]
            if enemy.attack() == True:
                player.is_hurt(enemy.forca)
        
        stdsrc.refresh()
    
     


if __name__ == "__main__":
   wrapper(main)
   









