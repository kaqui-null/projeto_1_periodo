import curses
from curses import wrapper

from player import Player
from enemy import Enemy
from mapa import mapa


def main(stdsrc):
    stdsrc.nodelay(True)

    try:
        curses.curs_set(0)
    except:
        pass

    mapa_test = mapa.Mapa_test(stdsrc)
    mapa_test_window = mapa_test.new_win()
    
    player = Player(mapa_test_window, [mapa_test.y, mapa_test.x], [5, 5, "up"], 3)
    enemy = Enemy(mapa_test_window, 3, 1,[8, 8, "up"], [player.origin_y, player.origin_x])

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
        
            mapa_test_window.erase()
            player.walk(key)
            player.draw_sprite()
            enemy.draw_sprite()

            enemy.player_pos = [player.origin_y, player.origin_x]
            if enemy.attack() == True:
                player.is_hurt(enemy.forca)
        
        mapa_test_window.refresh()
        mapa_test_window.border()
        stdsrc.refresh()
    

if __name__ == "__main__":
   wrapper(main)
   









