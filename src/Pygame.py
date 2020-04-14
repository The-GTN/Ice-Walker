#coding:utf-8

################################################# Les Imports #################################################

from pygame import init # désolé, ça affichera forcément ce message...
from pygame import QUIT, MOUSEBUTTONDOWN, KEYDOWN, FULLSCREEN, K_q,K_a, K_b, K_SPACE, K_RETURN, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_BACKSPACE, K_DELETE, K_ESCAPE, quit
from pygame.display import set_caption, set_mode, flip, set_icon
from pygame.mixer import music, pre_init
from pygame.event import get
from pygame.draw import line
from pygame.image import load
from pygame.font import SysFont, get_fonts
from game import *
from grid import *
from cell import *
from queue import change_config
from os import listdir
from os.path import isfile, join
import sys

###############################################################################################################

##### Taille des cellules #####
CELLSIZE = 40
###############################

################################################# Animation du début #################################################

def start():
    """
    Start the Project of Ice Walker
    """
    ## On initialise pygame et on met comme nom de fenêtre le nom du jeu ##
    init()
    set_caption("Ice Walker")
    #######################################################################
    
    ############## On crée la fenêtre pygame avec sa taille ###############
    surface = (500,520)
    window = set_mode(surface,FULLSCREEN)
    #######################################################################
    
    ############## On crée la fenêtre pygame avec sa taille ###############
    icon_32x32 = load("images/Ice/case_final1.png")
    set_icon(icon_32x32)
    #######################################################################
    
    ################# On charge les images de l'animation #################
    image1 = load("images/Menu/ps1_losange.png")
    image2 = load("images/Menu/ps1_ap2.png")
    image3 = load("images/Menu/ps1_P.png")
    image4 = load("images/Menu/ps1_licence.png")
    image5 = load("images/Menu/ps1_proj.png")
    image1.convert_alpha()
    image2.convert_alpha()
    image3.convert_alpha()
    image4.convert_alpha()
    image5.convert_alpha()
    #######################################################################
    
    ######### On insère la 1ere image et on actualise l'affichage #########
    window.blit(image1,[0,0])
    flip()
    #######################################################################
    
    #On préinitialise le son (pour un meilleur rendu), on lance la musique#
    pre_init(44100,-16,2,32)
    music.load("songs/playstation.mp3")
    music.play()
    #######################################################################
    
    ###### Gestionnaire d'événements (tant que ça affiche le pygame) ######
    launched = True
    skip = False
    while launched:
        
        ########## Différentes étape de l'animation ##########
        if 2900 < music.get_pos() < 3200:
            window.blit(image2,[0,0])
            flip()
        elif 7700 < music.get_pos() < 8000:
            window.fill((0,0,0))
            flip()
        elif 8000 < music.get_pos() < 8400:
            window.blit(image3,[0,0])
            flip()
        elif 8600 < music.get_pos() < 8800:
            window.blit(image4,[0,0])
            flip()
        elif 8800 < music.get_pos() < 9000:
            window.blit(image5,[0,0])
            flip()
        ######################################################
            
        ################ Fin de la musique ###################
        elif music.get_pos() == (-1):
            launched = False
        ######################################################
            
        ##################### Evénements #####################
        for event in get():
            if event.type == QUIT:
                #Quand on clique sur la croix de sortie  ## Attention, en plein écran on ne la voit pas, mais la croix est là !
                launched = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # Quand on appuie sur echap, on passe l'animation
                    skip = True
                    launched = False
                elif event.key == K_q:
                    # Quand on appuie sur q, on quitte
                    launched = False
        ######################################################
                
    #######################################################################
                
    ######################### Sortie de boucle ############################
    #### Quand musique finie : on passe au menu grid ####
    if music.get_pos() == -1 or skip:
        music.stop()
        menu_grid()
    #####################################################
    #### On a cliqué sur la croix : on ferme pygame  ####
    else:
        music.stop()
        quit()
    #####################################################
    #######################################################################

######################################################################################################################

################################## Menu sélection de la grille dans laquelle on joue #################################
def menu_grid():
    """
    Show the menu where we can choose the grid of Ice Walker we want to play
    """
    #################### On crée la fenêtre ###############################
    surface = (500,520)
    window = set_mode(surface,FULLSCREEN)
    #######################################################################
    ###### Chargements et conversions (pour utilisation) des images #######
    bouton1 = load("images/Menu/bouton_grid1.png")
    bouton2 = load("images/Menu/bouton_grid2.png")
    bouton3 = load("images/Menu/bouton_grid3.png")
    bouton4 = load("images/Menu/bouton_grid4.png")
    bouton5 = load("images/Menu/bouton_grid5.png")
    bouton6 = load("images/Menu/bouton_grid6.png")
    bouton1.convert_alpha()
    bouton2.convert_alpha()
    bouton3.convert_alpha()
    bouton4.convert_alpha()
    bouton5.convert_alpha()
    bouton6.convert_alpha()
    grid1 = load("images/Menu/grid1.png")
    grid2 = load("images/Menu/grid2.png")
    grid3 = load("images/Menu/grid3.png")
    grid4 = load("images/Menu/grid4.png")
    grid5 = load("images/Menu/grid5.png")
    grid6 = load("images/Menu/grid6.png")
    grid1.convert_alpha()
    grid2.convert_alpha()
    grid3.convert_alpha()
    grid4.convert_alpha()
    grid5.convert_alpha()
    grid6.convert_alpha()
    #######################################################################
    ############ Mise en page du menu de sélection de la grille ###########
    window.fill((0,0,0))
    window.blit(bouton1,(50,50))
    window.blit(bouton2,(190,50))
    window.blit(bouton3,(330,50))
    window.blit(bouton4,(50,270))
    window.blit(bouton5,(190,270))
    window.blit(bouton6,(330,270))
    window.blit(grid1,(70,90))
    window.blit(grid2,(210,90))
    window.blit(grid3,(375,90))
    window.blit(grid4,(70,310))
    window.blit(grid5,(210,310))
    window.blit(grid6,(350,310))
    font = SysFont(get_fonts()[0],30,True)
    text = font.render("Choose your grid", True,(255,255,255))
    window.blit(text,[125,7])
    flip() ## toujours actualiser l'affichage quand on veut afficher
    #######################################################################
    ######################## Gestionnaire d'événements ####################
    launched = True
    back = False
    grid = None
    while launched:

        ################## Evénements ########################
        for event in get():
            if event.type == QUIT:
                ## quand on clique sur la croix de sortie
                launched = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    ## quand on clique sur echap, on retourne à l'animation de début
                    launched = False
                    back = True
                elif event.key == K_q:
                    ## quand on clique sur q, on quitte
                    launched = False
                    
            elif event.type == MOUSEBUTTONDOWN:
                ## quand on clique sur la fenêtre
                
                x, y = event.pos # on récupère l'endroit où on a cliqué
                
                ## Avons nous cliqué sur une grille ? ##
                if (170 >= x >= 50 and 80 >= y >= 50) or (244 >= y >= 90 and 150 >= x >= 70):
                    grid = Grid.from_file("data/grid01.txt")
                    launched = False
                elif (310 >= x >= 190 and 80 >= y >= 50) or (290 >= x >= 210 and 244 >= y >= 90) :
                    grid = Grid.from_file("data/grid02.txt")
                    launched = False
                elif (450 >= x >= 330 and 80 >= y >= 50) or (405>= x >= 375 and 244 >= y >= 90):
                    grid = Grid.from_file("data/grid03.txt")
                    launched = False
                elif (170 >= x >= 50 and 300 >= y >= 270) or (150 >= x >= 70 and 464 >= y >= 310):
                    grid = Grid.from_file("data/grid04.txt")
                    launched = False
                elif (310 >= x >= 190 and 300 >= y >= 270) or (290 >= x >= 210 and 468 >= y >= 310) :
                    grid = Grid.from_file("data/grid05.txt")
                    launched = False
                elif (450 >= x >= 330 and 300 >= y >= 270) or (430>= x >= 350 and 458 >= y >= 310):
                    grid = Grid.from_file("data/grid06.txt")
                    launched = False
        ######################################################
    #######################################################################
    #################### Sortie de boucle #################################
    ### On a choisi une grille : on passe au menu theme ###
    if grid != None:
        menu_theme(grid)
    ### On a cliqué sur echap, on relance l'animation de début ### 
    elif back:
        start()
    ### On a cliqué sur la croix de sortie ###
    else:
        quit()
    #######################################################################
######################################################################################################################
        
################################# Menu sélection du theme de notre partie ############################################
def menu_theme(grid):
    """
    Show the menu where we choose the theme of the game
    :param grid: the grid selected before with menu_grid()
    :type grid: Grid
    """
    ### On initie une nouvelle surface d'une nouvelle taille ###
    surface = (805,580)
    window = set_mode(surface,FULLSCREEN)
    window.fill((0,0,0))
    ############################################################
    # On écrit du texte, donc on initie une police d'écriture ##
    font = SysFont(get_fonts()[0],30,True)
    text = font.render("Choose your theme", True,(255,255,255))
    window.blit(text,[290,7])
    ############################################################
    ############## On initialise les images ####################
    theme1 = load("images/Menu/theme_Ice.jpg")
    theme1.convert()
    theme2 = load("images/Menu/theme_Miraculous.jpg")
    theme2.convert()
    theme3 = load("images/Menu/theme_Initial_D.jpg")
    theme3.convert()
    theme4 = load("images/Menu/theme_Jojo.jpg")
    theme4.convert()
    theme5 = load("images/Menu/theme_Shark.jpg")
    theme5.convert()
    theme6 = load("images/Menu/theme_Minecraft.jpg")
    theme6.convert()
    ############################################################
    ############### On insère les images #######################
    window.blit(theme1,[50,50])
    window.blit(theme2,[315,50])
    window.blit(theme3,[580,50])
    window.blit(theme4,[50,300])
    window.blit(theme5,[315,300])
    window.blit(theme6,[580,300])

    flip() ## et on actualise !
    ############################################################

    ############## Gestionnaire d'événements ###################
    launched = True
    back = False
    theme = None
    while launched:
        ##### Evenements #####
        for event in get():
            if event.type == QUIT:
                ### Clic sur croix de sortie
                launched = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    ## quand on clique sur echap, on retourne au menu grille
                    launched = False
                    back = True
                elif event.key == K_q:
                    ## quand on clique sur q, on quitte
                    launched = False
            elif event.type == MOUSEBUTTONDOWN:
                ### Clic sur la fenêtre
                # on récupère les coordonnées de notre clic
                x, y = event.pos
                # Avons nous cliqué sur un thème ?
                if (50 <= x <= 275 and 50 <= y <= 275):
                    launched = False
                    theme = "Ice"
                elif (315 <= x <= 540 and 50 <= y <= 275):
                    launched = False
                    theme = "Miraculous"
                elif (580 <= x <= 805 and 50 <= y <= 275):
                    launched = False
                    theme = "Initial_D"
                elif (50 <= x <= 275 and 300 <= y <= 525):
                    launched = False
                    theme = "Jojo"
                elif (315 <= x <= 540 and 300 <= y <= 525):
                    launched = False
                    theme = "Shark"
                elif (580 <= x <= 805 and 300 <= y <= 525):
                    launched = False
                    theme = "Minecraft"
    ############################################################
    ################## Sortie de boucle ########################
    ### On a choisi un thème de jeu : on peut jouer
    if theme != None:
        Pygame(grid,theme)
    ### On a appuyé echap, on retourne au menu grille
    elif back:
        menu_grid()
    ### On a clic sur la croix de sortie
    else:
        quit()
######################################################################################################################
        
##########################################       Le jeu         ######################################################
def Pygame(grid,theme = "Ice"):
    """
    Play the Ice Walker grid on pygame with the theme theme
    :param grid: the grid of Ice Walker
    :type grid: Grid
    :param theme:[optionnal] the theme of the game
    :type theme: str
    """
    ### Au cas où on fait un retour en arrière pour changer de thème, il faut garder la version de base lol
    grid_de_base = Grid.from_file(grid.get_name())
    ### On crée une fenêtre de taille dépendante de la taille de la grille
    width = grid.get_width()
    height = grid.get_height()
    surface = (CELLSIZE*width+10,CELLSIZE*height+10)
    window = set_mode(surface,FULLSCREEN)
    ######################################################################
    ### On affiche la grille en pygame ###################################
    # (avec une couleur en plus pour l'esthétique)
    couleur = (230,230,255)
    window.fill(couleur)
    rep_Pygame(grid,window,theme)
    ######################################################################
    ######################## On charge les musiques ######################
    songs = [f for f in listdir('songs') if isfile(join('songs', f))]
    songs = [f for f in songs if theme in f]
    pre_init(44100,-16,2,2048) # préinitialisation pour un meilleur son
    cmpt = 0  ## compteur pour savoir à quelle musique on est
    music.load("songs/"+songs[cmpt])
    music.play()
    ######################################################################
    ######################### Variables ##################################
    player_selected = None         # joueur sélectionné avec le clic
    old_player = list()            # liste des joueurs qu'on a bougé
    old_position = list()          # liste de leurs positions
    pause = False                  # la musique est en pause ?
    restart = False                # on recommence une partie ?
    back = False                   # on retourne au menu theme ?
    width2 = window.get_width()    # largeur fenêtre en pixel
    height2 = window.get_height()  # hauteur fenêtre en pixel
    konami = ""                    # Où en est le konami code ?
    touches = [K_a,K_b,K_UP,K_DOWN,K_RIGHT,K_LEFT,K_RETURN] #touche konami
    ######################################################################
    ################ Gestionnaire d' événements ##########################
    launched = True
    while launched:
        
        #### Quand une musique se finit, on lance la suivante
        if music.get_pos() == (-1) and not(pause):
            if cmpt == len(songs)-1:
                cmpt = 0
            else:
                cmpt += 1
            pre_init(44100,-16,2,2048)
            music.load("songs/"+songs[cmpt])
            music.play()
        #####################################################
        ## Si tu as déjà gagné la partie (en faisant echap, on peut changer le theme d'une partie gagnée)
        if grid.state():
            victory(window)
        ################# Evénements ########################
        for event in get():
            
            if event.type == QUIT:
                # Clic sur croix de sortie 
                launched = False
                
            elif event.type == MOUSEBUTTONDOWN and not(grid.state()):
                # Clic fenêtre pendant la partie
                x, y = event.pos
                x = (x-5)//40     # On récupère la cellule où on a clic
                y = (y-5)//40
                if 0 <= x <= width-1 and 0 <= y <= height-1:
                    cell = grid.get_cell(x,y)
                    if cell.has_player():
                        # Si on a clic sur un joueur, on récupére son num
                        player_selected= cell.get_player().get_num()
                    elif cell.is_win():
                        # Si on clic sur la case finale, on restart la partie
                        while old_player != []:
                            player = grid.get_player(old_player.pop())
                            change_config(grid,player,old_position.pop())
                        window.fill(couleur)
                        rep_Pygame(grid,window,theme)
                    
            elif event.type == KEYDOWN and not(grid.state()):
                # Touche du clavier appuyé pendant la partie
                
                if not(event.key in touches):
                    # Si on clique une touche autre que celle du konami code, konami code réinitialisé
                    konami = ""
                    
                if event.key == K_q:
                    # appuie sur 'q' abandon de la partie
                    launched = False
                
                elif event.key == K_ESCAPE:
                    # on appuie sur echap, on retourne à la sélection de thème
                    launched = False
                    back = True
                    
                elif event.key == K_b:
                    # si le code tapé coorespond à la suite du konami code, on peut poursuivre
                    if konami == "12345678":
                        konami += "9"
                    # sinon le code est réinitialisé
                    else:
                        konami = ""
                        
                elif event.key == K_a:
                    # si le code tapé coorespond à la suite du konami code, on peut poursuivre
                    if konami == "123456789":
                        konami += "10"
                    # sinon le code est réinitialisé
                    else:
                        konami = ""
                
                elif event.key == K_SPACE:
                    # appuie sur "space", pause ou play la musique
                    if pause:
                        music.unpause()
                        pause = False
                    else:
                        music.pause()
                        pause = True
                        
                elif event.key == K_RETURN:
                    #Si le konami code n'est pas tapé, les musiques du theme fonctionne de la même manière
                    # appuie sur "entrée", lance la prochaine musique
                    if cmpt == len(songs)-1 and konami != "12345678910":
                        cmpt = 0
                    elif konami == "12345678910":
                        cmpt = 0
                        songs = ["Rickroll.mp3"]
                        grid.change_state()
                        victory(window)
                    else:
                        cmpt += 1
                    pre_init(44100,-16,2,2048)
                    music.load("songs/"+songs[cmpt])
                    music.play()
                    
                elif event.key == K_DELETE:
                    # appuie sur "suppr", lance la musique précédente
                    if cmpt == 0:
                        cmpt = len(songs)-1
                    else:
                        cmpt -= 1
                    pre_init(44100,-16,2,2048)
                    music.load("songs/"+songs[cmpt])
                    music.play()
                    
                elif event.key == K_BACKSPACE:
                    # appuie sur "backspace", annule le dernier mouvement
                    if old_player != []:
                        player = grid.get_player(old_player.pop())
                        change_config(grid,player,old_position.pop())
                        window.fill(couleur)
                        rep_Pygame(grid,window,theme)
                        
                elif player_selected != None:
                    #Si on a clic sur un joueur
                    
                    if event.key == K_UP:
                        # appuie sur flèche du haut, le joueur va vers le nord
                        old_player += [player_selected]
                        old_position += [(grid.get_player(player_selected).get_x(),grid.get_player(player_selected).get_y())]
                        player_mvt(grid,player_selected,"N")
                        if grid.state():
                            # si mouvement victoire, affiche l'écran de victoire
                            victory(window)
                        else:
                            # sinon affiche le déplacement effectué
                            rep_Pygame(grid,window,theme)
                            # et on voit pour le konami code
                            if konami == "":
                                konami = "1"
                            elif konami == "1":
                                konami += "2"
                            else:
                                konami = ""
                            
                    elif event.key == K_DOWN:
                        # appuie sur flèche du bas, le joueur va vers le sud
                        old_player += [player_selected]
                        old_position += [(grid.get_player(player_selected).get_x(),grid.get_player(player_selected).get_y())]
                        player_mvt(grid,player_selected,"S")
                        if grid.state():
                            # si mouvement victoire, affiche l'écran de victoire
                            victory(window)
                        else:
                            # sinon affiche le déplacement effectué
                            rep_Pygame(grid,window,theme)
                            # et on voit pour le konami code
                            if konami == "12":
                                konami += "3"
                            elif konami == "123":
                                konami += "4"
                            else:
                                konami = ""
                            
                    elif event.key == K_RIGHT:
                        # appuie sur flèche de droite, le joueur va vers l' est
                        old_player += [player_selected]
                        old_position += [(grid.get_player(player_selected).get_x(),grid.get_player(player_selected).get_y())]
                        player_mvt(grid,player_selected,"E")
                        if grid.state():
                            # si mouvement victoire, affiche l'écran de victoire
                            victory(window)
                        else:
                            # sinon affiche le déplacement effectué
                            rep_Pygame(grid,window,theme)
                            # et on voit pour le konami code
                            if konami == "12345":
                                konami += "6"
                            elif konami == "1234567":
                                konami += "8"
                            else:
                                konami = ""
                            
                    elif event.key == K_LEFT:
                        # appuie sur flèche de gauche, le joueur va vers l' ouest
                        old_player += [player_selected]
                        old_position += [(grid.get_player(player_selected).get_x(),grid.get_player(player_selected).get_y())]
                        player_mvt(grid,player_selected,"W")
                        if grid.state():
                            # si mouvement victoire, affiche l'écran de victoire
                            victory(window)
                        else:
                            # sinon affiche le déplacement effectué
                            rep_Pygame(grid,window,theme)
                            # et on voit pour le konami code
                            if konami == "1234":
                                konami += "5"
                            elif konami == "123456":
                                konami += "7"
                            else:
                                konami = ""
                    
                elif event.key == K_UP:
                    # Si aucun personnage n'est sélectionné, les flèches ne servent qu'à faire le konami code
                    if konami == "":
                        konami += "1"
                    elif konami == "1":
                        konami += "2"
                    else:
                        konami = ""
                        
                elif event.key == K_DOWN:
                    # Si aucun personnage n'est sélectionné, les flèches ne servent qu'à faire le konami code
                    if konami == "12":
                        konami += "3"
                    elif konami == "123":
                        konami += "4"
                    else:
                        konami = ""
                    
                elif event.key == K_LEFT:
                    # Si aucun personnage n'est sélectionné, les flèches ne servent qu'à faire le konami code
                    if konami == "1234":
                        konami += "5"
                    elif konami == "123456":
                        konami += "7"
                    else:
                        konami = ""
                    
                elif event.key == K_RIGHT:
                    # Si aucun personnage n'est sélectionné, les flèches ne servent qu'à faire le konami code
                    if konami == "12345":
                        konami += "6"
                    elif konami == "1234567":
                        konami += "8"
                    else:
                        konami = ""
                    
            elif event.type == KEYDOWN:
                # Si touche clavier appuyé et partie gagné
                
                if not(event.key in touches):
                    # Si on clique une touche autre que celle du konami code, konami code réinitialisé
                    konami = ""
                
                if event.key == K_SPACE:
                    # appuie sur "space", pause ou play la musique
                    if pause:
                        music.unpause()
                        pause = False
                    else:
                        music.pause()
                        pause = True
                        
                elif event.key == K_ESCAPE:
                    # echap
                    launched = False
                    back = True
                
                elif event.key == K_UP:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "":
                        konami += "1"
                    elif konami == "1":
                        konami += "2"
                    else:
                        konami = ""
                        
                elif event.key == K_DOWN:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "12":
                        konami += "3"
                    elif konami == "123":
                        konami += "4"
                    else:
                        konami = ""
                    
                elif event.key == K_LEFT:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "1234":
                        konami += "5"
                    elif konami == "123456":
                        konami += "7"
                    else:
                        konami = ""
                    
                elif event.key == K_RIGHT:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "12345":
                        konami += "6"
                    elif konami == "1234567":
                        konami += "8"
                    else:
                        konami = ""
                        
                elif event.key == K_b:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "12345678":
                        konami += "9"
                    else:
                        konami = ""
                        
                elif event.key == K_a:
                    # Même la partie terminée, on peut faire le konami code
                    if konami == "123456789":
                        konami += "10"
                    else:
                        konami = ""
                
                elif event.key == K_RETURN:
                    #Si le konami code n'est pas tapé, les musiques du theme fonctionne de la même manière
                    # appuie sur "entrée", lance la prochaine musique
                    if cmpt == len(songs)-1 and konami != "12345678910":
                        cmpt = 0
                    elif konami == "12345678910":
                        cmpt = 0
                        songs = ["Rickroll.mp3"]
                    else:
                        cmpt += 1
                    pre_init(44100,-16,2,2048)
                    music.load("songs/"+songs[cmpt])
                    music.play()
                    
                elif event.key == K_DELETE:
                    # appuie sur "suppr", lance la musique précédente
                    if cmpt == 0:
                        cmpt = len(songs)-1
                    else:
                        cmpt -= 1
                    pre_init(44100,-16,2,2048)
                    music.load("songs/"+songs[cmpt])
                    music.play()
                    
            elif event.type == MOUSEBUTTONDOWN:
                # Clic sur fenêtre et partie gagné : retour menu grille ou quitter ?
                x, y = event.pos
                
                if width > 15:
                    if (3*width2//8+120 >= x >= 3*width2//8) and (int(height2*(6/8)-25)+30 >= y >= int(height2*(6/8)-25)):
                        launched = False
                    elif (3*width2//8+120 >= x >= 3*width2//8) and (int(height2*(7/8)-15)+30 >= y >= int(height2*(7/8)-15)) :
                        launched = False
                        restart = True
                        
                elif width < 6:
                    if int(width2*(3/16))+120 >= x >= int(width2*(3/16)) and (int(height2*(6/8)-25)+30 >= y >= int(height2*(6/8)-25)):
                        launched = False
                    elif int(width2*(3/16))+120 >= x >= int(width2*(3/16)) and (int(height2*(7/8)-15)+30 >= y >= int(height2*(7/8)-15)) :
                        launched = False
                        restart = True
                        
                elif 15 >= width >= 6:
                    if width2//4+120 >= x >= width2//4 and (int(height2*(6/8)-25)+30 >= y >= int(height2*(6/8)-25)):
                        launched = False
                    elif width2//4+120 >= x >= width2//4 and (int(height2*(7/8)-15)+30 >= y >= int(height2*(7/8)-15)) :
                        launched = False
                        restart = True
        #####################################################
    ######################################################################
    ##################   Sortie de boucle     ############################
    #### On a choisit de retourner au menu grille
    if restart:
        music.stop()
        menu_grid()
    elif back:
        music.stop()
        menu_theme(grid_de_base)
    #### On a cliqué sur la croix sortie, ou on a abandonné, ou on a choisit de quitter à la fin de partie
    else:
        quit()
    ######################################################################
######################################################################################################################


#################################### Affichage d'un mouvement ########################################################
def rep_Pygame(grid,window,theme):
    """
    Represent the grid with pygame on the surface window
    :param grid: Ice Walker grid
    :type grid: Grid
    :param window: the window where we want to represent the grid
    :type window: Surface
    :param theme: the theme of the game
    :type theme: str
    """
    ## On prend les mesures de la grille
    width = grid.get_width()
    height = grid.get_height()
    ## On dessine les contours en conséquence
    line(window,(0,0,0),[0,0],[0,CELLSIZE*height+10],10)
    line(window,(0,0,0),[0,0],[CELLSIZE*width+10,0],10)
    line(window,(0,0,0),[0,CELLSIZE*height+10],[CELLSIZE*width+10,CELLSIZE*height+10],14)
    line(window,(0,0,0),[CELLSIZE*width+10,0],[CELLSIZE*width+10,CELLSIZE*height+10],14)
    ## On charge les images
    image = load("images/"+theme+"/case1.png")
    image.convert_alpha()
    image_final = load("images/"+theme+"/case_final1.png")
    image_final.convert_alpha()
    main = load("images/"+theme+"/main.png")
    main.convert_alpha()
    player = load("images/"+theme+"/player.png")
    player.convert_alpha()
    ## On affiche les images de cellules
    # Avec des traits pour les murs si elles en ont
    # Avec un personnage dessus si il y en a un
    # Avec l'illustration de case finale si elle est en effet finale
    grid1 = grid.get_grid()
    x_final,y_final = grid.get_final()
    grid1[y_final][x_final].set_win()
    for y in range(height):
        for x in range(width):
            if grid1[y][x].is_win():
                window.blit(image_final,[x*CELLSIZE+5,y*CELLSIZE+5])
            if not(grid1[y][x].is_win()):
                window.blit(image,[x*CELLSIZE+5,y*CELLSIZE+5])
            if grid1[y][x].has_player():
                if grid1[y][x].get_player().is_main():
                    window.blit(main,[x*CELLSIZE+5,y*CELLSIZE+5])
                else:
                    window.blit(player,[x*CELLSIZE+5,y*CELLSIZE+5])
            if grid1[y][x].has_east_wall():
                line(window,(0,0,0),[(x+1)*CELLSIZE+5,y*CELLSIZE+5],[(x+1)*CELLSIZE+5,(y+1)*CELLSIZE+5],5)
            if grid1[y][x].has_south_wall():
                line(window,(0,0,0),[x*CELLSIZE+5,(y+1)*CELLSIZE+5],[(x+1)*CELLSIZE+5,(y+1)*CELLSIZE+5],5)
    flip() ## On actualise l'affichage !!
######################################################################################################################

####################################     Affichage Victoire     ######################################################
def victory(window):
    """
    Show a victory message on the surface window
    :param window: the surface we want to show a victory message
    :type window: Surface
    """
    ## On récupère les dimensions en pixel
    width = window.get_width()
    height = window.get_height()
    ## On écrit du texte
    font = SysFont(get_fonts()[0],width//10,True)
    text_victoire = font.render("Congratulation", True,(255,255,255))
    text2 = font.render("You win !", True,(255,255,255))
    ## On charge les images
    bouton1 = load("images/Menu/bouton_quit.png")
    bouton2 = load("images/Menu/bouton_menu.png")
    bouton1.convert_alpha()
    bouton2.convert_alpha()
    ## On affiche l'écran de victoire
    window.fill((0,0,0))
    window.blit(text_victoire,[width//8,height//4])
    window.blit(text2,[width//4,height//2])
    # Selon la taille de la fenêtre
    if 10 >= (width-10)//40 >= 6:
        window.blit(bouton1,([width//4,int(height*(6/8)-25)]))
        window.blit(bouton2,([width//4,int(height*(7/8)-15)]))
    elif (width-10)//40 < 6:
        window.blit(bouton1,([3*width//16,int(height*(6/8)-25)]))
        window.blit(bouton2,([3*width//16,int(height*(7/8)-15)]))
    elif (width-10)//40 > 15:
        window.blit(bouton1,([3*width//8,int(height*(6/8)-25)]))
        window.blit(bouton2,([3*width//8,int(height*(7/8)-15)]))
    flip() ## On actualise l'affichage !!
######################################################################################################################

########################################### Lancement du Ice Walker ##################################################
if __name__ == '__main__':
    start()
######################################################################################################################
    
    
### Codé et commenté par le futur Great Teacher Nollet