
import player as Player
import os , pygame ,numpy as np, keyboard, time, sys

LOAD_Music = pygame.mixer.music.load
Play_music = pygame.mixer.music.play

clock=pygame.time.Clock()
pygame.init()


#import de la scene 
def loading(scenes,scores=0):
    with open(scenes) as f:
        return f.read()

#reconsititution de la scene
def make_scene(s1=0,s2=0):
    scene[:9,:]=' '
    scene[9:10,:] = '#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    for i in enumerate(ground):
        if i[1] == '1':
            player1=Player.player(i[0], 0, 2, 2, 2, 2, 10,i[1])
            scene[3:9,i[0]:i[0]+3]=player1.get_idle()
            scene[5:7,i[0]+3:i[0]+4]=player1.rest()
        if i[1] == '2':
            player2=Player.player(i[0], 0, 2, 2, 2, 2, 2,i[1])
            scene[3:9,i[0]:i[0]+3]=player2.get_idle()
            scene[5:7,i[0]-2:i[0]-1]=player2.rest()
        if i[1] == '#':
            scene[8,i[0]]='#'
    return player1,player2

for i in range (4):
 print(" ","*"*5," ","Pour la scene "+loading("scene/scene"+str(i)+".ffscene")+" appuyez "+str(i)+" puis entrer "," "*4,"*"*6," ")

key = input()


#verification de l'existance d'une ancienne sauvegarde        
if os.path.exists('terminalSave.txt'):
    print("ya une sauvegarde")
    #on recupere la scene comme elle a été laisser
    ground = loading("terminalSave.ffscene")
    #on recupere les scores de la partie
    file1 = open('terminalSave.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
                        data = line.split()
    score1,score2=int(data[0]),int(data[1])
else:
    #sans sauvegarde on initialise nos score a 0
    score1,score2=0,0
    if key == '0' or key == '1' or key == '2' or key == '3':
        ground = loading("scene/scene"+key+".ffscene")
    else :
        ground = loading("default.ffscene")
   
    #on recupere la scene par defaut
    
taille = len(ground) 
#son de debut de combat
pygame.mixer.music.load('audio/start.mp3')
pygame.mixer.music.play(1)
#recuperation de la scene en cours et reconstitution de la chaine de caractere
def save_scene():
    s=''
    for i in range(np.shape(scene)[1]):
                            if scene[8,i] == '#':
                                s+='#'
                            if i == player1.get_Pos()[0]:
                                s+='1'
                                i+=2
                            if i == player2.get_Pos()[0]:
                                s+='2'
                                i+=2
                            if scene[8,i] == ' ':
                                s+='_'
    with open("terminalSave.ffscene", "w") as fichier:
        #on sauvegarde la nouvelle scene qui est une sauvegarde
        fichier.write(s)

#fonction de sauvegarde de nos scores
def sauvegarder(s1, s2):
    save_scene()
    with open("terminalSave.txt", "w") as fichier:
        print ("on va sauvegarder")
        fichier.write(str(s1)+' '+str(s2))

#initialisation de la matrice representant la scene
scene = np.zeros((10,len(ground)+4),object)


#positionnement de nos joeurs et leurs instanciation
player1,player2 = make_scene()

#mise a jour de la scene affiché
def update_scene(s1,s2,stat1=player1.rest(),stat2=player2.rest()):
    scene[:9,:]=' '
    for i in enumerate(ground):
        if i[1] == '#':
            scene[8,i[0]]='#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    scene[3-player1.get_Pos()[1]:9-player1.get_Pos()[1],player1.get_Pos()[0]:player1.get_Pos()[0]+3]=player1.get_idle()
    #position de garde
    if player1.get_weap()=='g':
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]+3:player1.get_Pos()[0]+4]=stat1
    else:
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]-1:player1.get_Pos()[0]]=stat1
    scene[3-player2.get_Pos()[1]:9-player2.get_Pos()[1],player2.get_Pos()[0]:player2.get_Pos()[0]+3]=player2.get_idle()
    #position de defense
    if player2.get_weap()=='d':
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]-2:player2.get_Pos()[0]-1]=stat2
    else:
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]+3:player2.get_Pos()[0]+4]=stat2

#display de la scene dans le terminal ( son affichage )
def display():
    for line in scene:
        output = ''
        for colomn in line:
            output+=str(colomn)
        print(output)

#instanciation de nos listes de mouvement 
p1_move_left, p1_move_right, p1_jump_left, p1_jump_right, p1_attack, p1_block = ([] for i in range(6))
p2_move_left, p2_move_right, p2_jump_left, p2_jump_right, p2_attack, p2_block = ([] for i in range(6))
#instanciation de nos etats
p1_move,p2_move,p1_action,p1scoring,p2scoring,p2_action=(False for i in range(6))
#instanciation de nos conteur de saut
p1_jump_count,p2_jump_count=0,0
#affichage du guide du jeu
def guide():
        print('\n','#'*18,'Le jeu est en pause','#'*35,'\n')
        print(' '*28,'Guide\n')
        print('#'*75,'\n')
        print('Joueur 1',' '*29)
        print('d : bouger a droite',' '*18,'#')
        print('q : bouger a gauche',' '*18,'#')
        print('e : sauter a droite',' '*18,'#')
        print('a : sauter a gauche',' '*18,'#')
        print('z : attaquer',' '*25,'#')
        print('s : bloquer',' '*26,'#\n')
        print('#'*75,'\n')
        print('Joueur 2',' '*29)
        print('fleche droite : bouger a droite',' '*6,'#')
        print('fleche gauche : bouger a gauche',' '*6,'#')
        print('m : sauter a droite',' '*18,'#')
        print('l : sauter a gauche',' '*18,'#')
        print('o : attaquer',' '*25,'#')
        print('p : bloquer',' '*26,'#\n')
        print('#'*75,'\n')
        print(" ","*"*5," ","Pour continuer la partie, appuyez sur la touche 'r' puis d'entre"," "*27,"*"*6," ")
        print(" ","*"*5," ","Pour relancer une nouvelle partie, appuyez sur la touche 'n' puis d'entre"," "*18,"*"*6," ")
        print(" ","*"*5," ","Pour quiter la version terminal et revenir au menu, appuyez sur la touche 'q' puis d'entre"," ","*"*6," ")
#retour a la position naturel
stat1,stat2=player1.rest(),player2.rest()
    
#ecoute et attente de la touche suivante
def Recup_mouvement(curframe,p1_move,p1_action,p2_move,p2_action):
    global p1_jump_count,p2_jump_count,actif,player1,player2
    distance = abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1))
    #pause et mise en suspension avec affichage du guide
    if keyboard.is_pressed('escape'):
        #sauvegarde
        sauvegarder(score1,score2)
        #on laisse les frames actives
        actif=False
        #on vide le terminal pour afficher le guide
        os.system('cls')
        guide()
        #attente de la decision du joueur
        key = input()
        if key == 'r':
            actif=True
        if key == 'n':
            player1.reset()
            player2.reset()
            player1,player2 = make_scene()
            actif=True
        if key == 'q':
            sys.exit()
    #mouvements du joueur 1
    if p1_move:    
        #se deplacer a gauche
        if keyboard.is_pressed('q'):
            #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
            if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-1] != '#':
                    if len(p1_move_right) > 1:
                        del p1_move_right[1:]
                    p1_move_left.append(curframe)
        #se deplacer a droite
        if keyboard.is_pressed('d'):
            #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
            if distance > 3 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+1] != '#':
                if len(p1_move_left) > 1:
                    del p1_move_left[1:]
                p1_move_right.append(curframe)

        if player1.get_weap() == 'g':
            #sauter a gauche
            if keyboard.is_pressed('a'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
            #sauter a droite
            if keyboard.is_pressed('e'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if  distance > 3 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+3] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
        else:  
            #sauter a gauche          
            if keyboard.is_pressed('a'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if distance > 3 and player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
            #sauter a droite
            if keyboard.is_pressed('e'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+3] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
        #on met l'etat de mouvement a faux pour pouvoir continuer
        p1_move = False
    if p1_action:
        #attaquer
        if keyboard.is_pressed('z'):
            if len(p1_attack) == 0 and len(p1_block) == 0:
                p1_attack.append(curframe)
        #Bloquer
        if keyboard.is_pressed('s'):
            if len(p1_block) == 0 and len(p1_attack) == 0:
                p1_block.append(curframe)
        p1_action =False 
        
    #mouvements du joueur 2
    if p2_move:    
        #se deplacer a gauche
        if keyboard.is_pressed('left'):
            #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
            if distance > 3 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-1] != '#':
                if len(p2_move_right) > 1:
                    del p2_move_right[1:]
                p2_move_left.append(curframe)
        #se deplacer a droite
        if keyboard.is_pressed('right'):
            #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
            if  player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+1] != '#':
                if len(p2_move_left) > 1:
                    del p2_move_left[1:]
                p2_move_right.append(curframe)

        if player2.get_weap()=='d':
        #sauter a gauche
            if keyboard.is_pressed('l'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if distance > 3 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
            #sauter a droite
            if keyboard.is_pressed('m'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
        else :
            #sauter a gauche
            if keyboard.is_pressed('l'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
            #sauter a droite
            if keyboard.is_pressed('m'):
                #on verifi que le mouvement est faisable et que ca respecte les lois du jeu
                if distance > 3 and player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
        p2_move = False
    if p2_action:
        #attaquer
        if keyboard.is_pressed('o'):
            if len(p2_attack) == 0 and len(p2_block) == 0:
                p2_attack.append(curframe)
        #Bloquer
        if keyboard.is_pressed('p'):
            if len(p2_block) == 0 and len(p2_attack) == 0:
                p2_block.append(curframe)
        p2_action =False

# lancer les actions 
def Execution(curframe):
    global p1_jump_count,p2_jump_count,stat1,stat2,p1scoring,p2scoring
    #joueur 1
    #on verfi si il a effectuer des mouvements 
    if  len(p1_move_left) != 0:
        if curframe%fps == (p1_move_left[0] + player1.get_MS())%fps:
            p1_move_left.pop(0)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            player1.move_left()

    if  len(p1_move_right) != 0:
        if curframe%fps == (p1_move_right[0] + player1.get_MS())%fps:
            p1_move_right.pop(0)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            player1.move_right()
    
    if  len(p1_jump_left) != 0:
        if curframe%fps == (p1_jump_left[0] + player1.get_MS())%fps:
            p1_jump_left[0] = curframe + player1.get_MS() -1
            player1.jump_left(p1_jump_count)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_left.pop(0)
                p1_jump_count=0

    if  len(p1_jump_right) != 0:
        if curframe%fps == (p1_jump_right[0] + player1.get_MS())%fps:
            p1_jump_right[0] = curframe + player1.get_MS() -1
            player1.jump_right(p1_jump_count)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_right.pop(0)
                p1_jump_count=0

    if len(p1_attack) != 0:
        if curframe%fps == (p1_attack[0] + player1.get_Atk_Stats()[0])%fps:
            p1_attack.pop(0)
            LOAD_Music('audio/Coup.mp3')
            Play_music(1)
            stat1=player1.attack()
            p1scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player1.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p2_block)

    if len(p1_block) != 0:
        stat1=player1.block()
        LOAD_Music('audio/bloc.mp3')
        Play_music(1)
        if curframe%fps == (p1_block[0] + player1.get_Def_Stats()[1])%fps:
            p1_block.pop(0)

    #joueur 2
    #on verfi si il a effectuer des mouvements 
    if  len(p2_move_left) != 0:
        if curframe%fps == (p2_move_left[0] + player2.get_MS())%fps:
            p2_move_left.pop(0)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            player2.move_left()

    if  len(p2_move_right) != 0:
        if curframe%fps == (p2_move_right[0] + player2.get_MS())%fps:
            p2_move_right.pop(0)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            player2.move_right()
    
    if  len(p2_jump_left) != 0:
        if curframe%fps == (p2_jump_left[0] + player2.get_MS())%fps:
            p2_jump_left[0] = curframe + player2.get_MS() -1
            player2.jump_left(p2_jump_count)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_left.pop(0)
                p2_jump_count=0

    if  len(p2_jump_right) != 0:
        if curframe%fps == (p2_jump_right[0] + player2.get_MS())%fps:
            p2_jump_right[0] = curframe + player2.get_MS() -1
            player2.jump_right(p2_jump_count)
            LOAD_Music('audio/move.mp3')
            Play_music(1)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_right.pop(0)
                p2_jump_count=0

    if len(p2_attack) != 0:
        if curframe%fps == (p2_attack[0] + player2.get_Atk_Stats()[0])%fps:
            p2_attack.pop(0)
            LOAD_Music('audio/Coup.mp3')
            Play_music(1)
            stat2=player2.attack()
            p2scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player2.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p1_block)

    if len(p2_block) != 0:
        LOAD_Music('audio/bloc.mp3')
        Play_music(1)
        stat2=player2.block()
        if curframe%fps == (p2_block[0] + player2.get_Def_Stats()[1])%fps:
            p2_block.pop(0)
#verification du blocage
def hitbox(p1x,p2x,atk,blck,blocked):
    dist=abs(p1x-p2x)
    if len(blocked) == 0:
        if dist<=atk:
            return True
    elif dist<=atk-blck+1:
        return True

def Score_Suivi():
    global p1scoring,p2scoring, score1,score2
    if p1scoring and p2scoring:
        pass
    elif p1scoring :
        score1 +=1
        p1scoring=False
    elif p2scoring:
        score2 +=1
        p2scoring=False





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
    Recup_mouvement(current_frame,p1_move,p1_action,p2_move,p2_action)
    Execution(current_frame)    
    #frame counter
    current_frame=(current_frame+1)%fps
    #refresh
    Score_Suivi()
    update_scene(score1, score2, stat1,stat2)
    display()    
    #print(' '*(len(ground)//2 -5) + 'Distance :' , abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1)))
    stat1,stat2=player1.rest(),player2.rest()
    
    #fps
    clock.tick(fps)
    time.sleep(ms/1000)


actif = True
while actif:
    terminal()


