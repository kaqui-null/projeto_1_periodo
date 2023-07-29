import curses


class Enemy:

    def __init__(self,stdsrc, hp, forca, origin_y, origin_x, direction, player_pos):
        self.hp = hp
        self.stdsrc = stdsrc
        self.forca = forca
        self.sprite = "@"
        self.origin_y = origin_y
        self.origin_x = origin_x
        self.direction = direction
        self.player_pos = player_pos
        self.player_y = player_pos[0]
        self.player_x = player_pos[1]

    def draw_sprite(self):
        self.stdsrc.addstr(self.origin_y, self.origin_x, self.sprite)

    def attack(self):
        if self.check_surrounding() == True:
            return self.forca
        else:
            #andar()
            return None


    def check_surrounding(self):
        for i in range(self.origin_y - 1, self.origin_y + 2):
            for j in range(self.origin_x - 1, self.origin_y + 2):
                if self.player_pos == [i, j]:
                    return True
                else:
                    continue
        
        





