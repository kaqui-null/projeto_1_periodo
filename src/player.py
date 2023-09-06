import curses

#### DEPRECATED ####
class Player:
    
    def __init__(self, win, window_size, origin, max_hp, dmg):
        self.win = win
        self.window_size = window_size
        self.window_y = window_size[0]
        self.window_x = window_size[1]
        self.origin_y = origin[0] 
        self.origin_x = origin[1]
        self.direction = origin[2]
        self.dmg = dmg

        self.max_hp = max_hp
        self.hp = max_hp
        self.inventario = []

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
        self.hp -= dmg


    def attack(self):
        switcher = {
            "up":[self.origin_y - 1, self.origin_x],
            "down":[self.origin_y + 1, self.origin_x],
            "left": [self.origin_y, self.origin_x - 1],
            "right": [self.origin_y, self.origin_x + 1]
                }
        return switcher.get(self.direction, "invalid direction")

    def use(self):
        switcher_ver = {
            "up": int(self.origin_y - 1),
            "down": int(self.origin_y + 1)
                }
        switcher_hor = {
            "left": int(self.origin_x - 1),
            "right": int(self.origin_x + 1)
        }
        coord_y = switcher_ver.get(self.direction, - 1)
        coord_x = switcher_hor.get(self.direction, - 1)

        visualized_vertical = self.win.inch(coord_y, int(self.origin_x))
        visualized_horizontal = self.win.inch(int(self.origin_y) ,coord_x)

        if (visualized_horizontal == curses.ACS_DIAMOND) or (visualized_vertical == curses.ACS_DIAMOND):
            self.inventario.append(self.win.inch(coord_y, int(self.origin_x)))
        else:
            return False












