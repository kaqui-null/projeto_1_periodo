import curses


class Player:
    
    def __init__(self, window_size, origin):
        self.window_size = window_size
        self.window_y = window_size[0]
        self.window_x = window_size[1]
        self.origin = origin
        self.origin_y = origin[0]
        self.origin_x = origin[1]
        self.direction = origin[2]

    def draw_sprite(self):
        pass

    def walk(self):
        pass












