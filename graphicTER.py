import pygame, numpy

from threading import Timer

LOAD_Music = pygame.mixer.music.load
Play_music = pygame.mixer.music.play
WIDTH = 650
HEIGHT = 550
BACKGROUND = pygame.image.load("assets/bd.png")
TICK=10
class Sprite1(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [startx, starty]
    def get_position(self):
        return (self.rect.x,self.rect.y)
    def update(self):
        pass
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player1(Sprite1):
    def __init__(self,num, startx, starty,step,health,movement_speed,attacking_speed,attacking_range,defending_range,blocking_time,points):
        super().__init__("assets/OLD/p"+str(num)+"_front.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = pygame.image.load("assets/OLD/p"+str(num)+"_jump.png")
        self.jump_image = pygame.image.load("assets/OLD/p"+str(num)+"_jump.png")
        self.jump_imageD = pygame.image.load("assets/OLD/p"+str(num)+"_jump.png")
        self.jump_imageG = pygame.image.load("assets/OLD/p"+str(num)+"_jump.png")
        self.attack_image = pygame.image.load("assets/OLD/p"+str(num)+"_attack.png")
        self.bloc_image = pygame.image.load("assets/OLD/p"+str(num)+"_block.png")
        self.num = num
        self.walk_cycle = [pygame.image.load(f"assets/OLD/p"+str(num)+"_walk01.png") for i in range(1,12)]
        self.animation_index = 0
        self.facing_left = False
        self.startx = startx
        self.starty = starty
        self.step = step
        self.movement_speed = movement_speed
        self.jumpspeed = movement_speed
        self.on_def=False
        self.on_att=False
        self.attacking_speed = attacking_speed
        self.attacking_range = attacking_range*60
        self.defending_range = defending_range
        self.blocking_time = TICK/blocking_time
        self.points=points
        self.health=health
        self.vsp = 0
        self.gravity = 100
        self.min_jumpspeed = 4
        self.prev_key = pygame.key.get_pressed()
    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        LOAD_Music('audio/move.mp3')
        Play_music(1)
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0
    def update(self, sol,player2,clock,count):
        hsp = 0
        onground = self.check_collision(0, 1, sol)
        # on recupere la touche pressé
        key = pygame.key.get_pressed()
        # Mouvement a gauche 
        if key[pygame.K_q] and self.num==1:
            self.walk_animation()
            hsp = -self.step
        # Mouvement a droit
        elif key[pygame.K_d] and self.num==1:
            self.walk_animation()
            hsp = self.step
        # Mouvement attack
        elif key[pygame.K_z] and self.num==1:
            self.image = self.attack_image
            self.on_att=True
            #print(str(Sprite1.get_position(player2)[0])+" -z- "+str(Sprite1.get_position(self)[0])+" -z- "+str(self.attacking_range) +" -z- "+ str(player2.on_def)+" -z- "+ str(player2.on_att))
            if(Sprite1.get_position(player2)[0]-self.attacking_range <= Sprite1.get_position(self)[0] and not player2.on_def and not player2.on_att):  
                LOAD_Music('audio/Coup.mp3')
                Play_music(1)  
                self.points+=1
                player2.health-=10
                self.rect.center = [self.startx, self.starty]
                player2.rect.center = [player2.startx, player2.starty]
            elif Sprite1.get_position(player2)[0]-self.attacking_range <= Sprite1.get_position(self)[0] and player2.on_def and not player2.on_att :  
                LOAD_Music('audio/bloc.mp3')
                Play_music(1)
            else:
                LOAD_Music('audio/CoupVide.mp3')
                Play_music(1)      
                 
        elif not self.on_def :
            self.image = self.stand_image
            self.on_att=False
        # fonction pour desactiver la defense    
        def descative():
                self.on_def=False
                self.image = self.stand_image
        # Mouvement block joueur 1
        if key[pygame.K_s] and self.num==1:
            self.image = self.bloc_image
            #activer la defense 
            self.on_def=True
            #timer pour la desactiver
            t = Timer(self.blocking_time,descative)
            t.start() 
        if key[pygame.K_a] and onground and self.num==1:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageG
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            hsp = -self.step
            self.vsp = -self.step*10
        if key[pygame.K_e] and onground and self.num==1:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageD
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            hsp = self.step
            self.vsp = -self.step*10      
        # Mouvement block joueur 2
        if key[pygame.K_p] and self.num==2:
            self.image = self.bloc_image
            #activer la defense 
            self.on_def=True
            t = Timer(self.blocking_time,descative)
            t.start()
        if key[pygame.K_l] and onground and self.num==2:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageG
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            hsp = -self.step
            self.vsp = -self.step*10
        if key[pygame.K_m] and onground and self.num==2:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageD
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            hsp = self.step
            self.vsp = -self.step*10
        if key[pygame.K_LEFT] and self.num==2:
            self.walk_animation()
            hsp = -self.step
        # Mouvement a droit
        if key[pygame.K_RIGHT]and self.num==2:
            self.walk_animation()
            hsp = self.step
        # Mouvement attack
        if key[pygame.K_o]and self.num==2:
            self.image = self.attack_image
            self.on_att=True
            #print(str(Sprite1.get_position(player2)[0])+" -o- "+str(Sprite1.get_position(self)[0])+" -o- "+str(self.attacking_range) +" -o- "+ str(player2.on_def)+" -o- "+ str(player2.on_att))
            if(Sprite1.get_position(self)[0]-self.attacking_range <= Sprite1.get_position(player2)[0]  and not player2.on_def and not player2.on_att):
                
                LOAD_Music('audio/Coup.mp3')
                Play_music(1)
                self.points+=1
                player2.health-=10
                self.rect.center = [self.startx, self.starty]
                player2.rect.center = [player2.startx, player2.starty]
            elif Sprite1.get_position(self)[0]-self.attacking_range <= Sprite1.get_position(player2)[0]  and player2.on_def and not player2.on_att :  
                LOAD_Music('audio/bloc.mp3')
                Play_music(1)
            else:
                LOAD_Music('audio/CoupVide.mp3')
                Play_music(1)        
        self.prev_key = key
        # vitesse de chute / effet gravité
        if self.vsp < 10 and not onground :
            self.vsp += self.gravity
        # si la chute ne le remet pas a terre visuellement on le met a 0    
        if onground and self.vsp > 0:
            self.vsp = 0       
        self.move(hsp, self.vsp, sol,player2,key)
    def move(self, x, y, sol,player2,key):
        dx = x # distance a parcourir sur x
        dy = y # distance a parcourir sur y
        #on peux modifier la positon vertical a condition de pas avoir de collision si non on tombe plus
        while self.check_collision(0, dy, sol):
            dy -= numpy.sign(dy)
        #on peux modifier la positon a condition de pas avoir de collision si non on avance plus
        while ( self.check_collision(dx, dy, sol)):    
            dx -= numpy.sign(dx)
        while (self.check_collision2(dx, dy,player2)):    
            dx -= numpy.sign(dx)  
        self.rect.move_ip([dx, dy]) 
    #verification qu'on traverse pas le sol
    def check_collision(self, x, y, grounds):
        self.rect.move_ip([x, y])
         #on detecte la colision avec un autre element qui est le bloc de scene
        collide = pygame.sprite.spritecollideany(self, grounds) 
        self.rect.move_ip([-x, -y])
        return collide
    #verification qu'on traverse pas le deuxieme joueur
    def check_collision2(self, x, y,player2):
        self.rect.move_ip([x, y])
        #on detecte la colision avec un autre element qui est player 2
        collide = pygame.sprite.collide_rect(self, player2)
        self.rect.move_ip([-x, -y])
        return collide
class Bloc1(Sprite1):
    def __init__(self, startx, starty):
        super().__init__("assets/OLD/Bloc.png", startx, starty)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



