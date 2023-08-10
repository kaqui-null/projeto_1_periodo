import curses


class Player:
    
    def __init__(self, win, window_size, origin, max_hp):
        self.win = win
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
        switcher = {
            "up":"^",
            "down":"v",
            "left": "<",
            "right": ">"
                }
        curr_sprite = switcher.get(self.direction, "invalid direction error")
        self.win.addstr(self.origin_y, self.origin_x, curr_sprite)


    def walk(self, key):
        if key == "KEY_LEFT" and  0 != self.origin_x - 1:
            self.origin_x -= 1
            self.direction = "left"
        elif key == "KEY_RIGHT" and  self.window_x != self.origin_x + 2:
            self.origin_x += 1
            self.direction = "right"
        elif key == "KEY_UP" and  0 != self.origin_y - 1:
            self.origin_y -= 1
            self.direction = "up"
        elif key == "KEY_DOWN" and  self.window_y != self.origin_y + 2:
            self.origin_y += 1
            self.direction = "down"

    def is_hurt(self, dmg):
        self.hp -= 1


    def attack(self):
        pass

    def use(self):
        pass












