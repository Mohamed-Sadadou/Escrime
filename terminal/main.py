
#importing the necessary modules
import player as create, os , pygame ,numpy as np, keyboard, time, sys
# from matplotlib import pyplot as plt
# from pynput import keyboard

clock=pygame.time.Clock()
pygame.init()

#importing the default scene
def loading(scenes="default.ffscene",scores=0):
    with open(scenes) as f:
        return f.read()

ground = loading()

#loading the scene informations into a matrix
scene = np.zeros((10,len(ground)+4),object)
def make_scene(s1=0,s2=0):
    scene[:9,:]=' '
    scene[9:10,:] = '#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    for i in enumerate(ground):
        if i[1] == '1':
            player1=create.player(i[0], 0, 2, 2, 2, 2, 10,i[1])
            scene[3:9,i[0]:i[0]+3]=player1.get_idle()
            scene[5:7,i[0]+3:i[0]+4]=player1.rest()
        if i[1] == '2':
            player2=create.player(i[0], 0, 2, 2, 2, 2, 2,i[1])
            scene[3:9,i[0]:i[0]+3]=player2.get_idle()
            scene[5:7,i[0]-2:i[0]-1]=player2.rest()
        if i[1] == '#':
            scene[8,i[0]]='#'
    return player1,player2


#create the players
player1,player2 = make_scene()

#updating the scene
def update_scene(s1,s2,stat1=player1.rest(),stat2=player2.rest()):
    scene[:9,:]=' '
    for i in enumerate(ground):
        if i[1] == '#':
            scene[8,i[0]]='#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    scene[3-player1.get_Pos()[1]:9-player1.get_Pos()[1],player1.get_Pos()[0]:player1.get_Pos()[0]+3]=player1.get_idle()
    if player1.get_weap()=='g':
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]+3:player1.get_Pos()[0]+4]=stat1
    else:
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]-1:player1.get_Pos()[0]]=stat1
    scene[3-player2.get_Pos()[1]:9-player2.get_Pos()[1],player2.get_Pos()[0]:player2.get_Pos()[0]+3]=player2.get_idle()
    if player2.get_weap()=='d':
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]-2:player2.get_Pos()[0]-1]=stat2
    else:
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]+3:player2.get_Pos()[0]+4]=stat2

#displaying the scene on terminal
def display():
    for line in scene:
        output = ''
        for colomn in line:
            output+=str(colomn)
        print(output)


p1_move_left=[]
p2_move_left=[]
p1_move_right=[]
p2_move_right=[]
p1_jump_left=[]
p2_jump_left=[]
p1_jump_right=[]
p2_jump_right=[]
p1_attack=[]
p2_attack=[]
p1_block=[]
p2_block=[]
p1_move,p2_move,p1_action,p1scoring,p2scoring,p2_action=False,False,False,False,False,False
p1_jump_count,p2_jump_count=0,0
stat1,stat2=player1.rest(),player2.rest()
#function that hears the keyboard and allows one type of action for each player per frame
def listener(curframe,p1_move,p1_action,p2_move,p2_action):
    global p1_jump_count,p2_jump_count,actif,player1,player2
    distance = abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1))
    #pause
    if keyboard.is_pressed('escape'):
        actif=False
        os.system('cls')
        print('!'*18,'Le jeu est en pause','!'*18)
        print('Guide')
        print('*'*75)
        print('Joueur 1',' '*17,'|',' '*17,'Joueur 2')
        print('d : avancer a droite',' '*5,'|',' '*5,'fleche droite : avancer a droite')
        print('q : avancer a gauche',' '*5,'|',' '*5,'fleche gauche : avancer a gauche')
        print('e : sauter a droite',' '*6,'|',' '*5,'m : sauter a droite')
        print('a : sauter a gauche',' '*6,'|',' '*5,'l : sauter a gauche')
        print('z : attaquer',' '*13,'|',' '*5,'o : attaquer')
        print('s : bloquer',' '*14,'|',' '*5,'p : attaquer')
        print('*'*75)
        print('?-Pour continuer la partie, veilleur appuier sur la touche "C" suivit d"entre')
        print('?-Pour reinitialiser la partie, veilleur appuier sur la touche "R" suivit d"entre')
        print('?-Pour sauvgarder votre partie courante, veilleur appuier sur la touche "S" suivit d"entre')
        print('?-Pour quiter le jeu, veilleur appuier sur la touche "Q" suivit d"entre')

        key = input()
        if key == 'c':
            actif=True
        if key == 'r':
            player1.reset()
            player2.reset()
            player1,player2 = make_scene()
            actif=True
        if key == 's':
            actif=True
        if key == 'q':
            sys.exit()
    #player 1
    if p1_move:    
        #moveleft
        if keyboard.is_pressed('q'):
            #check is the move is possible
            if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-1] != '#':
                    if len(p1_move_right) > 1:
                        del p1_move_right[1:]
                    p1_move_left.append(curframe)
        #moveright
        if keyboard.is_pressed('d'):
            #check is the move is possible
            if distance > 3 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+1] != '#':
                if len(p1_move_left) > 1:
                    del p1_move_left[1:]
                p1_move_right.append(curframe)

        if player1.get_weap() == 'g':
            #jumpleft
            if keyboard.is_pressed('a'):
                #check is the move is possible
                if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
            #jumpright
            if keyboard.is_pressed('e'):
                #check is the move is possible
                if  distance > 3 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+3] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
        else:            
            if keyboard.is_pressed('a'):
                #check is the move is possible
                if distance > 3 and player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
            #jumpright
            if keyboard.is_pressed('e'):
                #check is the move is possible
                if player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+3] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
        p1_move = False
    if p1_action:
        #attack
        if keyboard.is_pressed('z'):
            if len(p1_attack) == 0 and len(p1_block) == 0:
                p1_attack.append(curframe)
        #block
        if keyboard.is_pressed('s'):
            if len(p1_block) == 0 and len(p1_attack) == 0:
                p1_block.append(curframe)
        p1_action =False 
        
    #player 2
    if p2_move:    
        #moveleft
        if keyboard.is_pressed('left'):
            #check is the move is possible
            if distance > 3 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-1] != '#':
                if len(p2_move_right) > 1:
                    del p2_move_right[1:]
                p2_move_left.append(curframe)
        #moveright
        if keyboard.is_pressed('right'):
            #check is the move is possible
            if  player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+1] != '#':
                if len(p2_move_left) > 1:
                    del p2_move_left[1:]
                p2_move_right.append(curframe)

        if player2.get_weap()=='d':
        #jumpleft
            if keyboard.is_pressed('l'):
                #check is the move is possible
                if distance > 3 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
            #jumpright
            if keyboard.is_pressed('m'):
                #check is the move is possible
                if player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
        else :
            if keyboard.is_pressed('l'):
                #check is the move is possible
                if player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
            #jumpright
            if keyboard.is_pressed('m'):
                #check is the move is possible
                if distance > 3 and player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
        p2_move = False
    if p2_action:
        #attack
        if keyboard.is_pressed('o'):
            if len(p2_attack) == 0 and len(p2_block) == 0:
                p2_attack.append(curframe)
        #block
        if keyboard.is_pressed('p'):
            if len(p2_block) == 0 and len(p2_attack) == 0:
                p2_block.append(curframe)
        p2_action =False

# lunch actions regarding the stats
def actioner(curframe):
    global p1_jump_count,p2_jump_count,stat1,stat2,p1scoring,p2scoring
    #player1
    #moves
    if  len(p1_move_left) != 0:
        if curframe%fps == (p1_move_left[0] + player1.get_MS())%fps:
            p1_move_left.pop(0)
            player1.move_left()

    if  len(p1_move_right) != 0:
        if curframe%fps == (p1_move_right[0] + player1.get_MS())%fps:
            p1_move_right.pop(0)
            player1.move_right()
    
    if  len(p1_jump_left) != 0:
        if curframe%fps == (p1_jump_left[0] + player1.get_MS())%fps:
            p1_jump_left[0] = curframe + player1.get_MS() -1
            player1.jump_left(p1_jump_count)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_left.pop(0)
                p1_jump_count=0

    if  len(p1_jump_right) != 0:
        if curframe%fps == (p1_jump_right[0] + player1.get_MS())%fps:
            p1_jump_right[0] = curframe + player1.get_MS() -1
            player1.jump_right(p1_jump_count)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_right.pop(0)
                p1_jump_count=0

    #actions
    if len(p1_attack) != 0:
        if curframe%fps == (p1_attack[0] + player1.get_Atk_Stats()[0])%fps:
            p1_attack.pop(0)
            stat1=player1.attack()
            p1scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player1.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p2_block)

    if len(p1_block) != 0:
        stat1=player1.block()
        if curframe%fps == (p1_block[0] + player1.get_Def_Stats()[1])%fps:
            p1_block.pop(0)


#player2
    if  len(p2_move_left) != 0:
        if curframe%fps == (p2_move_left[0] + player2.get_MS())%fps:
            p2_move_left.pop(0)
            player2.move_left()

    if  len(p2_move_right) != 0:
        if curframe%fps == (p2_move_right[0] + player2.get_MS())%fps:
            p2_move_right.pop(0)
            player2.move_right()
    
    if  len(p2_jump_left) != 0:
        if curframe%fps == (p2_jump_left[0] + player2.get_MS())%fps:
            p2_jump_left[0] = curframe + player2.get_MS() -1
            player2.jump_left(p2_jump_count)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_left.pop(0)
                p2_jump_count=0

    if  len(p2_jump_right) != 0:
        if curframe%fps == (p2_jump_right[0] + player2.get_MS())%fps:
            p2_jump_right[0] = curframe + player2.get_MS() -1
            player2.jump_right(p2_jump_count)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_right.pop(0)
                p2_jump_count=0

    #actions
    if len(p2_attack) != 0:
        if curframe%fps == (p2_attack[0] + player2.get_Atk_Stats()[0])%fps:
            p2_attack.pop(0)
            stat2=player2.attack()
            p2scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player2.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p1_block)

    if len(p2_block) != 0:
        stat2=player2.block()
        if curframe%fps == (p2_block[0] + player2.get_Def_Stats()[1])%fps:
            p2_block.pop(0)


def hitbox(p1x,p2x,atk,blck,blocked):
    dist=abs(p1x-p2x)
    if len(blocked) == 0:
        if dist<=atk:
            return True
    elif dist<=atk-blck+1:
        return True

def referee():
    global p1scoring,p2scoring, score1,score2
    if p1scoring and p2scoring:
        pass
    elif p1scoring :
        score1 +=1
        p1scoring=False
    elif p2scoring:
        score2 +=1
        p2scoring=False

#init scores
score1,score2=0,0
#init fps and ms

ms=120
fps = 12
current_frame=0

def terminal():
    global ms,dps,current_frame,score1,score2,stat1,stat2
    p1_move,p1_action,p2_move,p2_action=True,True,True,True
    #clear the terminal        
    os.system('cls')
    print('FPS ',current_frame)
    #actionners
    listener(current_frame,p1_move,p1_action,p2_move,p2_action)
    actioner(current_frame)    
    #frame counter
    current_frame=(current_frame+1)%fps
    #refresh
    referee()
    update_scene(score1, score2, stat1,stat2)
    display()    
    print(' '*(len(ground)//2 -5) + 'Distance :' , abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1)))
    stat1,stat2=player1.rest(),player2.rest()
    
    #fps
    clock.tick(fps)
    time.sleep(ms/1000)
    # if current_frame == fps:
    #     break


actif = True
while actif:
    terminal()


