import pygame, sys, time, os
from button import Button
from graphicA import Sprite,Player,Bloc,draw_text
from graphicTER import Sprite1,Player1,Bloc1
import subprocess
pygame.init()

MWIDTH = 1280
MHEIGHT = 720

WIDTH = 650
HEIGHT = 550
BACKGROUND = pygame.image.load("assets/bd.png")
TICK=60

pygame.mixer.music.load('audio/KOF.mp3')
        #play the music infinite
pygame.mixer.music.play(-1)

SCREEN = pygame.display.set_mode((MWIDTH, MHEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def TERMINAL():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN = pygame.display.set_mode((MWIDTH, MHEIGHT))
        SCREEN.fill("black")
        pygame.display.set_caption("TERMINAL")
        PLAY_TEXT = get_font(35).render("This is the TERMINAL screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(MWIDTH/2, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(15).render("Go to terminal to play the game", True, "green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(MWIDTH/2, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_Last = Button(image=None, pos=(MWIDTH/2, 300), 
                            text_input="PLAY LAST", font=get_font(50), base_color="White", hovering_color="Green")
        PLAY_NEW = Button(image=None, pos=(MWIDTH/2, 400), 
                            text_input="PLAY NEW", font=get_font(50), base_color="White", hovering_color="Green")                    
        PLAY_BACK = Button(image=None, pos=(MWIDTH/2, 500), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        for button in [PLAY_Last, PLAY_NEW, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                    #on lance une nouvelle partie
                    print("play new")
                    if os.path.exists('terminalSave.txt'):
                     os.remove("terminalSave.txt")
                    subprocess.run([sys.executable, "-c", 'exec(open("./terminal.py").read())'])   
                elif PLAY_Last.checkForInput(PLAY_MOUSE_POS):
                    #il suffit de ne pas supprimer le fichier et le code detecte la sauvegarde
                    print("play Last")
                    subprocess.run([sys.executable, "-c", 'exec(open("./terminal.py").read())'])  
        pygame.display.update()
def GRAPHIC_TER():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN = pygame.display.set_mode((MWIDTH, MHEIGHT))
        SCREEN.fill("black")

        PLAY_TEXT = get_font(35).render("This is the GRAPHIC screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(MWIDTH/2, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        
        PLAY_Last = Button(image=None, pos=(MWIDTH/2, 300), 
                            text_input="PLAY LAST", font=get_font(50), base_color="White", hovering_color="Green")
        PLAY_NEW = Button(image=None, pos=(MWIDTH/2, 400), 
                            text_input="PLAY NEW", font=get_font(50), base_color="White", hovering_color="Green")
                                           
        PLAY_BACK = Button(image=None, pos=(MWIDTH/2, 500), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        for button in [PLAY_Last, PLAY_NEW, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                    #on lance une nouvelle partie
                    print("play new")
                    graphi(2,100,400,420,5,1000,1000,1,4,2,4,4,1,4,2,4,4,0,0)
                elif PLAY_Last.checkForInput(PLAY_MOUSE_POS):
                    #on recupere les données puis on lance
                    print("play Last")
                    file1 = open('data.txt', 'r')
                    Lines = file1.readlines()
  
                    count = 0
                    players =[]
                    # Strips the newline character
                    for line in Lines:
                        count += 1
                        data = line.split()
                        players.append(data)
                        print(data)
                    print(players)
                    graphi(2,float(players[0][0]),float(players[1][0]),float(players[0][1]),5,int(players[0][2]),int(players[1][2]),int(players[0][3]),int(players[0][4]),float(players[0][5])/60,int(players[0][6]),float(players[0][7]),int(players[1][3]),int(players[1][4]),float(players[1][5])/60,int(players[1][6]),float(players[1][7]),int(players[0][8]),int(players[1][8]))

        pygame.display.update()    
    
def GRAPHIC():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN = pygame.display.set_mode((MWIDTH, MHEIGHT))
        SCREEN.fill("black")
        pygame.display.set_caption("GRAPHIC")
        PLAY_TEXT = get_font(35).render("This is the GRAPHIC screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(MWIDTH/2, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        
        PLAY_Last = Button(image=None, pos=(MWIDTH/2, 300), 
                            text_input="PLAY LAST", font=get_font(50), base_color="White", hovering_color="Green")
        PLAY_NEW = Button(image=None, pos=(MWIDTH/2, 400), 
                            text_input="PLAY NEW", font=get_font(50), base_color="White", hovering_color="Green")
                                           
        PLAY_BACK = Button(image=None, pos=(MWIDTH/2, 500), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        for button in [PLAY_Last, PLAY_NEW, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                    #on lance une nouvelle partie
                    print("play new")
                    graphi(1,100,400,420,5,1000,1000,6,4,2,4,4,6,4,2,4,4,0,0)
                elif PLAY_Last.checkForInput(PLAY_MOUSE_POS):
                    #on recupere les données puis on lance
                    print("play Last")
                    file1 = open('data.txt', 'r')
                    Lines = file1.readlines()
                    count = 0
                    players =[]
                    # Strips the newline character
                    for line in Lines:
                        count += 1
                        data = line.split()
                        players.append(data)
                        print(data)
                    print(players)
                    graphi(1,float(players[0][0]),float(players[1][0]),float(players[0][1]),5,int(players[0][2]),int(players[1][2]),int(players[0][3]),int(players[0][4]),float(players[0][5])/60,int(players[0][6]),float(players[0][7]),int(players[1][3]),int(players[1][4]),float(players[1][5])/60,int(players[1][6]),float(players[1][7]),int(players[0][8]),int(players[1][8]))

        pygame.display.update()

def sauvegarder(player1, player2):
    with open("data.txt", "w") as fichier:
        print ("on va sauvegarder")
        arguments = (str(Sprite.get_position(player1)[0]),str(Sprite.get_position(player1)[1]),str(player1.health),str(player1.movement_speed),str(player1.attacking_speed),str(player1.attacking_range),str(player1.defending_range),str(player1.blocking_time),str(player1.points), "\n")
        fichier.write(" ".join(arguments))
        arguments2 = (str(Sprite.get_position(player2)[0]),str(Sprite.get_position(player2)[1]),str(player2.health),str(player2.movement_speed),str(player2.attacking_speed),str(player2.attacking_range),str(player2.defending_range),str(player2.blocking_time),str(player2.points),)
        fichier.write(" ".join(arguments2))
       
def graphi(af,startx1,startx2, starty,step,health,health2,movement_speed,attacking_speed,attacking_range,defending_range,blocking_time,movement_speed2,attacking_speed2,attacking_range2,defending_range2,blocking_time2,points,points2):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load('audio/start.mp3')
    pygame.mixer.music.play(1)
    
    if (af == 1 ):
        player = Player(1,startx1,starty,step,health,movement_speed,attacking_speed,attacking_range,defending_range,blocking_time,points)
        player2 = Player(2,startx2,starty,step,health2,movement_speed2,attacking_speed2,attacking_range2,defending_range2,blocking_time2,points2)

     #delimiter la zone de combat avec le sol et les murs non visible a l'ecran
        sol = pygame.sprite.Group()
        for bx in range(0, 650, 70):
            sol.add(Bloc(bx, 500))
        for by in range(0, 500, 70):
            sol.add(Bloc(-35, by))
            sol.add(Bloc(685, by))    
        font = get_font(15)
    else:
        print("deuxieme cas")
        player = Player1(1,startx1,starty,step,health,movement_speed,attacking_speed,attacking_range,defending_range,blocking_time,points)
        player2 = Player1(2,startx2,starty,step,health2,movement_speed2,attacking_speed2,attacking_range2,defending_range2,blocking_time2,points2)

     #delimiter la zone de combat avec le sol et les murs non visible a l'ecran
        sol = pygame.sprite.Group()
        for bx in range(0, 650, 70):
            sol.add(Bloc1(bx, 500))
        for by in range(0, 500, 70):
            sol.add(Bloc1(-35, by))
            sol.add(Bloc1(685, by))    
        font = get_font(15)

    
    loop = 1
    count = 0
    while loop:
        pygame.event.pump()
        GRAPH_MOUSE_POS = pygame.mouse.get_pos()
        # compteur de la frame
        if count !=TICK:
            count+=1
        else :
            count=0
        player.update(sol,player2,clock,count)
        player2.update(sol,player,clock,count)
         
        if( af == 1): 
            screen.blit(BACKGROUND, (0, 0))
        else:
            screen.fill((255, 255, 255))
        player.draw(screen)
        player2.draw(screen)
        sol.draw(screen)

        POINT_TEXT = get_font(15).render(str(player.health)+" / "+str(player.points)+"   -----    "+str(player2.points)+" / "+str(player2.health), True, "black")
        POINT_RECT = POINT_TEXT.get_rect(center=(WIDTH/2, 100))
        screen.blit(POINT_TEXT, POINT_RECT)


        draw_text("clock"+str(TICK), font, (0, 0, 0), screen, 500, 50)
        PAUSE = Button(image=None, pos=(100, 50), 
                            text_input="PAUSE", font=get_font(16), base_color="black", hovering_color="Green")
        PAUSE.changeColor(GRAPH_MOUSE_POS)
        PAUSE.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sauvegarder(player,player2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(GRAPH_MOUSE_POS):
                    #sauvegarder
                   sauvegarder(player,player2)
                   if ( af == 1):
                    GRAPHIC()
                   else:
                    GRAPHIC_TER()
        pygame.display.flip()
        
        if(player.health<0 or player2.health<0):
            draw_text("Game over", get_font(55), (0, 0, 0), screen, 100, 100)
            time.sleep(10)
            loop = 0
        clock.tick(TICK)
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(85).render("MAIN MENU", True, "Green")
        MENU_RECT = MENU_TEXT.get_rect(center=(MWIDTH/2, 75))

        TERMINAL_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(MWIDTH/2, 200), 
                            text_input="TERMINAL", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        GRAPHIC_TER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(MWIDTH/2, 350), 
                            text_input="GRAPHIC TER", font=get_font(50), base_color="#d7fcd4", hovering_color="White")                    
        GRAPHIC_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(MWIDTH/2, 500), 
                            text_input="GRAPHIC", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(MWIDTH/2, 650), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [TERMINAL_BUTTON, GRAPHIC_TER_BUTTON, GRAPHIC_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TERMINAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    TERMINAL()
                if GRAPHIC_TER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    GRAPHIC_TER()    
                if GRAPHIC_BUTTON.checkForInput(MENU_MOUSE_POS):
                    GRAPHIC()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()