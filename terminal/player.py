class player:
    counter = 0

    # construct
    def __init__(self, posX, posY, movement_speed, attacking_speed, attacking_range, blocking_range, blocking_time, head):
        self.__posX = posX
        self.__posY = posY
        self.__movement_speed = movement_speed
        self.__attacking_speed = attacking_speed
        self.__attacking_range = attacking_range
        self.__blocking_range = blocking_range
        self.__blocking_time = blocking_time

        if player.counter == 0:
            self.__idle = [['p',head,' '],
                            ['<', 'o', '>'],
                            [' ', '|', '_'],
                            [' ', '|', ' '],
                            [' ', '|', ' '],
                            ['/', '|', ' ']]
            self.__weap='g' 
        else:
            self.__idle=[['p',head,' '],
                    ['<', 'o', '>'],
                    ['_', '|', ' '],
                    [' ', '|', ' '],
                    [' ', '|', ' '],
                    [' ', '|', '\\']]
            self.__weap = 'd'
        player.counter+=1


    def reset(self):
        player.counter= 0
    # getters
    def get_idle(self):
        return self.__idle

    def get_Pos(self):
        return self.__posX, self.__posY

    def get_MS(self):
        return self.__movement_speed

    def get_Atk_Stats(self):
        return self.__attacking_speed, self.__attacking_range

    def get_Def_Stats(self):
        return self.__blocking_range, self.__blocking_time
    
    def get_weap(self):
        return self.__weap

    # actions
    def move_left(self):
        self.__posX -= 1
        

    def move_right(self):
        self.__posX += 1
        

    def jump_left(self,curr):
        if curr == 0:
            self.__posY += 1
        if curr == 1:
            self.__posX -= 2
        if curr == 2:
            self.__posY -=1

    def jump_right(self,curr):
        if curr == 0:
            self.__posY += 1
        if curr == 1:
            self.__posX += 2
        if curr == 2:
            self.__posY -=1
    
    def rest(self):
        return [['/'],[' ']] if self.__weap == 'g' else [['\\'],[' ']]

    def attack(self):
        return [['_'],[' ']]

    def block(self):
        return [['|'],[' ']]
