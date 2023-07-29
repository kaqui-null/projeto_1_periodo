import curses


class Player:
    
    def __init__(self, stdsrc, window_size, origin, max_hp):
        self.stdsrc = stdsrc
        self.window_size = window_size
        self.window_y = window_size[0]
        self.window_x = window_size[1]
        self.origin_y = origin[0]
        self.origin_x = origin[1]
        self.direction = origin[2]

        self.max_hp = max_hp
        self.hp = max_hp
        self.inventario = []
        self.inventario_max_size = 5

    def draw_sprite(self):
        sprites = ["<", ">", "^", "v"]

        switcher = {
            "up":"^",
            "down":"v",
            "left": "<",
            "right": ">"
                }
        curr_sprite = switcher.get(self.direction, "invalid direction error")
        self.stdsrc.addstr(self.origin_y, self.origin_x, curr_sprite)


    def walk(self, key):
        if key == "KEY_LEFT":
            self.origin_x -= 1 # muda dps quando decidirmos em uma distância percorrida 
            self.direction = "left"
        elif key == "KEY_RIGHT":
            self.origin_x += 1
            self.direction = "right"
        elif key == "KEY_UP":
            self.origin_y -= 1
            self.direction = "up"
        elif key == "KEY_DOWN":
            self.origin_y += 1
            self.direction = "down"

    def is_hurt(self, dmg):
        self.hp -= 1


    def attack(self):
        pass

    def use(self):
        pass












