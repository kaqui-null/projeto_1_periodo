import curses
from curses import wrapper


def main(stdsrc):
    WIN_Y = 35
    WIN_X = 135

    PLAYER_X = 5
    PLAYER_Y = 5
    PLAYER_DIRECTION = "up"
    PLAYER_DMG = 1
    PLAYER_HP = [10, 10]
    PLAYER_INVENTORY = []

    ENEMY_HP = 3
    ENEMY_DMG = 1
    ENEMY_Y = 8
    ENEMY_X = 8
    ENEMY_DIRECTION = "up"

    stdsrc.nodelay(True)

    try:
        curses.curs_set(0)
    except:
        pass

    window = curses.newwin(WIN_Y, WIN_X)
    
    key = 0
    while True:
        curses.resize_term(35,135)
        draw_map1(window)
        player_draw_sprite(window, PLAYER_DIRECTION, PLAYER_Y, PLAYER_X)
        
        
        try:
            key = stdsrc.getkey()
        except:
            key = None

        if key != None:
            if key == "q":
                print("you quit") # change to a centered message
                curses.napms(1000) 
                break
        

            window.erase()
            window.insch(5,5,curses.ACS_DIAMOND)
            player_origin = player_walk(WIN_X, WIN_Y, key, PLAYER_X, PLAYER_Y, PLAYER_DIRECTION)
            PLAYER_Y = player_origin[0]
            PLAYER_X = player_origin[1]
            PLAYER_DIRECTION = player_origin[2]
            player_draw_sprite(window, PLAYER_DIRECTION, PLAYER_Y, PLAYER_X)

            if ENEMY_HP > 0:
                window.addstr(ENEMY_Y, ENEMY_X, "@")
                if enemy_attack(ENEMY_Y, ENEMY_X, PLAYER_Y, PLAYER_X) == True:
                    PLAYER_HP[0] -= ENEMY_DMG

            if key == "x":
                if ([ENEMY_Y, ENEMY_X] == player_attack(PLAYER_Y, PLAYER_X, PLAYER_DIRECTION)):
                    ENEMY_HP -= PLAYER_DMG
                
            if key == "z":
                player_use(window, PLAYER_Y, PLAYER_X, PLAYER_DIRECTION, PLAYER_INVENTORY)
                stdsrc.addstr(0,0, str(PLAYER_INVENTORY))

        if PLAYER_HP[0] <= 0:
            #game_over()
            break
        
        print(ENEMY_HP, " ", PLAYER_HP)

        window.refresh()
        window.border()
        stdsrc.refresh()

## PLAYER ###
def player_draw_sprite(win, player_direction, player_y, player_x):
    switcher = {
        "up":"^",
        "down":"v",
        "left": "<",
        "right": ">"
            }
    curr_sprite = switcher.get(player_direction, "invalid direction error")
    win.addstr(player_y, player_x, curr_sprite)


def player_walk(window_x, window_y, key, player_x, player_y, player_direction):
    if key == "KEY_LEFT" and  0 != player_x - 1:
        player_x -= 1
        player_direction = "left"
        return [player_y, player_x, player_direction]
    elif key == "KEY_RIGHT" and  window_x != player_x + 2:
        player_x += 1
        player_direction = "right"
        return [player_y, player_x, player_direction]
    elif key == "KEY_UP" and  0 != player_y - 1:
        player_y -= 1
        player_direction = "up"
        return [player_y, player_x, player_direction]
    elif key == "KEY_DOWN" and  window_y != player_y + 2:
        player_y += 1
        player_direction = "down"
        return [player_y, player_x, player_direction]
    else:
        return [player_y, player_x, player_direction]


def player_attack(player_y, player_x, player_direction):
    switcher = {
        "up":[player_y - 1, player_x],
        "down":[player_y + 1, player_x],
        "left": [player_y, player_x - 1],
        "right": [player_y, player_x + 1]
            }
    return switcher.get(player_direction, "invalid direction")


def player_use(win, player_y, player_x, player_direction, player_inventory):
    switcher_ver = {
        "up": int(player_y - 1),
        "down": int(player_y + 1)
            }
    switcher_hor = {
        "left": int(player_x - 1),
        "right": int(player_x + 1)
    }
    coord_y = switcher_ver.get(player_direction, - 1)
    coord_x = switcher_hor.get(player_direction, - 1)

    visualized_vertical = win.inch(coord_y, int(player_x))
    visualized_horizontal = win.inch(int(player_y) ,coord_x)

    if (visualized_horizontal == curses.ACS_DIAMOND) or (visualized_vertical == curses.ACS_DIAMOND):
        player_inventory.append(win.inch(coord_y, int(player_x)))
    else:
        return False
##############

#### ENEMY ####
def enemy_draw(win, y, x, sprite):
    win.addstr(y, x, sprite)


def enemy_attack(enemy_y, enemy_x, player_y, player_x):
    for i in range(enemy_y - 1, enemy_y + 2):
            for j in range(enemy_x - 1, enemy_y + 2):
                if [player_y, player_x] == [i, j]:
                    return True
                else:
                    continue
###############

#### MAPA1 ####
def draw_map1(win):
    draw_room_map1(win)
    draw_corr_map1(win)


def draw_room_map1(win):
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

    
        for i in range(y, y + altura):
            win.addstr(i, x, '.' * comprimento) 
        
        window = win.subwin(altura+2, comprimento+2, y-1, x-1)
        window.border()


def draw_corr_map1(win):
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

        for i in range(y_vertical, y_vertical + vertical):
            win.addstr(i,x_vertical, ".")
        
    for k in range(len(coordenadas_horizontal)):

        horizontal = dimensoes_horizontal[k]
        y_horizontal = coordenadas_horizontal[k][0]
        x_horizontal = coordenadas_horizontal[k][1]

        #imprimindo corredor horizontal
        for i in range(x_horizontal, x_horizontal+horizontal):
            win.addstr(y_horizontal,i, ".")
###############










if __name__ == "__main__":
   wrapper(main)
   









