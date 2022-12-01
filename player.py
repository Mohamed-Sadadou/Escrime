class player:
    counter = 0

    # construct
    def __init__(self, posX, posY, movement_speed, attacking_speed, attacking_range, blocking_range, blocking_time, head):
        self.posX = posX
        self.posY = posY
        self.movement_speed = movement_speed
        self.attacking_speed = attacking_speed
        self.attacking_range = attacking_range
        self.blocking_range = blocking_range
        self.blocking_time = blocking_time
        if player.counter == 0:
            self.idle = [['p',head,' '],
                            ['<', 'o', '>'],
                            [' ', '|', '_'],
                            [' ', '|', ' '],
                            [' ', '|', ' '],
                            ['/', '|', ' ']]
            self.weap='g' 
        else:
            self.idle=[['p',head,' '],
                    ['<', 'o', '>'],
                    ['_', '|', ' '],
                    [' ', '|', ' '],
                    [' ', '|', ' '],
                    [' ', '|', '\\']]
            self.weap = 'd'
        player.counter+=1
    def reset(self):
        player.counter= 0
    # getters pour recuperer les données
    def get_idle(self):
        return self.idle
    def get_Pos(self):
        return self.posX, self.posY
    def get_MS(self):
        return self.movement_speed
    def get_Atk_Stats(self):
        return self.attacking_speed, self.attacking_range
    def get_Def_Stats(self):
        return self.blocking_range, self.blocking_time
    def get_weap(self):
        return self.weap
    # Les actions
    def move_left(self):
        self.posX -= 1
    def move_right(self):
        self.posX += 1
    def jump_left(self,curr):
        if curr == 0:
            self.posY += 1
        if curr == 1:
            self.posX -= 2
        if curr == 2:
            self.posY -=1
    def jump_right(self,curr):
        if curr == 0:
            self.posY += 1
        if curr == 1:
            self.posX += 2
        if curr == 2:
            self.posY -=1
    def rest(self):
        return [['/'],[' ']] if self.weap == 'g' else [['\\'],[' ']]
    def attack(self):
        return [['_'],[' ']]
    def block(self):
        return [['|'],[' ']]
