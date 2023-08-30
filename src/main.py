import curses
from curses import wrapper

from player import Player
from enemy import Enemy
from mapa import win


def main(stdsrc):
    stdsrc.nodelay(True)

    try:
        curses.curs_set(0)
    except:
        pass

    window = win.Win(stdsrc, 35, 135)
    window_src = window.new_win()
    
    player = Player(window_src, [window.y, window.x], [5, 5, "up"], 3, 3)
    enemy = Enemy(window_src, 3, 1,[8, 8, "up"], [player.origin_y, player.origin_x])

    key = 0
    while True:
        curses.resize_term(35,135)
        player.draw_sprite()
        
        
        try:
            key = stdsrc.getkey()
        except:
            key = None

        if key != None:
            if key == "q":
                break
        

            window_src.erase()
            window_src.insch(5,5,curses.ACS_DIAMOND)
            player.walk(key)
            player.draw_sprite()

            if enemy.die() != True:
                enemy.draw_sprite()

                enemy.player_pos = [player.origin_y, player.origin_x]
                if enemy.attack() == True:
                    player.is_hurt(enemy.forca)

            if key == "x":
                if ([enemy.origin_y, enemy.origin_x] == player.attack()):
                    enemy.hp -= player.dmg
                
            if key == "z":
                player.use()
                stdsrc.addstr(0,0, str(player.inventario))

        if player.hp <= 0:
            #game_over()
            break
        
        window_src.refresh()
        window_src.border()
        stdsrc.refresh()


if __name__ == "__main__":
   wrapper(main)
   









