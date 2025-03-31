"""
Programme réalisé par Roquain Rémy 1G7
"""
import pygame
from pygame import mixer

#variables du niveau
NB_TILES = 33   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=20      #hauteur du niveau
hauteur=20       #largeur du niveau
tiles=[]       #liste d'images tiles

#variables de gestion du pacman
pacX=1          #position x y du pacman dans le niveau
pacY=1
compteurBilles=0
directionPac=14
vie=3

#variables de gestion du fantome
FRAMERATE_FANTOME= 25      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME =28   #le fantome se deplace sur 9 cases
positionFantome=1
frameRateCounterFantome=0
posfX=18     #position initiale du fantome
posfY=2

FRAMERATE_FANTOME2= 25      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME2 =35   #le fantome se deplace sur 9 cases
positionFantome2=1
frameRateCounterFantome2=0
posfX2=18     #position initiale du fantome
posfY2=2

FRAMERATE_FANTOME3= 25      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME3 =31   #le fantome se deplace sur 9 cases
positionFantome3=1
frameRateCounterFantome3=0
posfX3=5     #position initiale du fantome
posfY3=6

# Fluditié : faire une variable stopPacman 0 ou 1 et je peux appuier sur une touche quand stopPacman est égale à 1 et ???

#definition du niveau

niveau=[[1,5,5,5,5,5,5,2,0,0,0,0,1,5,5,5,5,5,5,2],
     [6,0,12,12,12,12,12,3,5,2,1,5,4,12,12,12,12,12,12,6],
     [6,12,12,12,12,12,12,12,12,6,6,12,12,12,12,12,12,12,12,6],
     [3,5,5,5,5,2,12,12,12,6,6,12,12,12,1,5,5,5,5,4],
     [1,5,5,5,5,4,12,12,12,3,4,12,12,12,3,5,5,5,5,2],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,32,6],
     [3,2,12,1,2,12,12,12,12,12,12,12,12,12,12,1,2,12,1,4],
     [0,6,12,6,6,12,1,5,24,12,12,23,5,2,12,6,6,12,6,0],
     [0,6,12,6,6,12,6,12,12,12,12,12,12,6,12,6,6,12,6,0],
     [0,6,32,6,6,12,6,12,12,12,12,12,12,6,12,6,6,12,6,0],
     [0,6,12,6,6,12,6,12,12,12,12,12,12,6,12,6,6,12,6,0],
     [0,6,12,6,6,12,3,5,5,5,5,5,5,4,12,6,6,12,6,0],
     [1,4,12,3,4,12,12,12,12,12,12,12,12,12,12,3,4,12,3,2],
     [6,12,12,12,12,12,1,5,5,5,5,5,5,2,12,12,12,12,12,6],
     [6,12,1,5,2,12,3,5,2,0,0,1,5,4,12,1,5,2,12,6],
     [6,12,6,0,6,12,12,12,6,0,0,6,12,12,12,6,0,6,12,6],
     [6,12,6,0,6,12,12,12,3,5,5,4,12,12,12,6,0,6,12,6],
     [6,12,3,5,4,12,26,12,12,12,12,12,12,26,12,3,5,4,12,6],
     [6,12,12,12,12,12,6,12,12,12,12,12,12,6,12,12,12,12,32,6],
     [3,5,5,5,5,5,8,5,5,5,5,5,5,8,5,5,5,5,5,4]
    ]

fantome=[[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 ,6, 5, 4, 3, 2, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 8, 24,25,26,27,28, 1, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 0,23, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,11, 0,22, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0,14,13, 12, 0,21,20,0,0,0,0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0,15,16,17,18,18,19,0,0,0,0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

fantome2=[[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0],
         [ 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0],
         [ 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0],
         [ 0, 33, 0, 0, 0, 7, 8, 9, 0, 0, 0, 0, 16, 17, 18, 0, 0, 0, 26, 0],
         [ 0, 34, 0, 0, 0, 6, 0, 10, 11, 12, 13, 14, 15, 0, 19, 0, 0, 0, 25, 0],
         [ 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 22, 23, 24, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

fantome3=[[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#la taille de la fenetre dépend de la largeur et de ++9 ,la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
pygame_logo = pygame.image.load('data/14.png')
pygame.display.set_icon(pygame_logo)
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))


def affichePac(numero):
    """
    affiche le pacman en position pacX et pacY
    """
    fenetre.blit(tiles[numero],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render("Score : " + str(score), True, (255, 255, 255))
    fenetre.blit(scoreAafficher,(400,640))

def afficheVie(vie):
    """
    affiche le score
    """
    vieAafficher = font.render("Vie(s) : " + str(vie), True, (255, 255, 255))
    fenetre.blit(vieAafficher,(180,640))

def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coodFantome=x,y
    return coodFantome          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome(fantome):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome
    global positionFantome
    global posfX,posfY
    if frameRateCounterFantome==FRAMERATE_FANTOME:      #ralenti la viteese du fantome
        posfX,posfY=rechercheFantome(fantome,positionFantome)   #deballage du tuple coordonnées du fantome
        positionFantome+=1
        if positionFantome==NB_DEPLACEMENT_FANTOME:     #un tour est fait donc on passe à la 1ere position
            positionFantome=1
        frameRateCounterFantome=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[15],(posfX * TITLE_SIZE,posfY * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome+=1                          #incrémentation du compteur de vitesse

def rechercheFantome2(fantome2,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome2[y][x]==position:
                coodFantome2=x,y
    return coodFantome2          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome2(fantome2):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome2
    global positionFantome2
    global posfX2,posfY2
    if frameRateCounterFantome2==FRAMERATE_FANTOME2:      #ralenti la viteese du fantome
        posfX2,posfY2=rechercheFantome2(fantome2,positionFantome2)   #deballage du tuple coordonnées du fantome
        positionFantome2+=1
        if positionFantome2==NB_DEPLACEMENT_FANTOME2:     #un tour est fait donc on passe à la 1ere position
            positionFantome2=1
        frameRateCounterFantome2=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[30],(posfX2 * TITLE_SIZE,posfY2 * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome2+=1                          #incrémentation du compteur de vitesse

def rechercheFantome3(fantome3,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome3[y][x]==position:
                coodFantome3=x,y
    return coodFantome3          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome3(fantome3):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome3
    global positionFantome3
    global posfX3,posfY3
    if frameRateCounterFantome3==FRAMERATE_FANTOME3:      #ralenti la viteese du fantome
        posfX3,posfY3=rechercheFantome3(fantome3,positionFantome3)   #deballage du tuple coordonnées du fantome
        positionFantome3+=1
        if positionFantome3==NB_DEPLACEMENT_FANTOME3:     #un tour est fait donc on passe à la 1ere position
            positionFantome3=1
        frameRateCounterFantome3=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[31],(posfX3 * TITLE_SIZE,posfY3 * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome3+=1


def suprBilles():
    global niveau
    global compteurBilles
    for y in range(hauteur):
        for x in range(largeur):
            if niveau[y][x]==12:
                if compteurBilles!=0:
                    niveau[y][x]=0
                    compteurBilles+=1
                else:
                    compteurBilles+=1
            if niveau[y][x]==32:
                if compteurBilles!=0:
                    niveau[y][x]=0
    compteurBilles-=1



chargetiles(tiles)  #chargement des images
numeroTile = 0


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:   #est-ce la touche UP
                posY = pacY - 1             #on deplace le pacman vituellement
                posX = pacX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 32):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacY -= 1                         #on monte donc il faut décrémenter pacY
                    directionPac=28
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                print("down",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 32):
                    pacY += 1
                    directionPac=27
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                posY = pacY
                posX = pacX + 1
                numeroTile = niveau[posY][posX]
                print("right",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 32):
                    pacX += 1
                    directionPac=14
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
                #A compléter pour le déplacement à droite

            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                posY = pacY
                posX = pacX - 1
                numeroTile = niveau[posY][posX]
                print("right",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0):
                    pacX -= 1
                    directionPac=29
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            if (numeroTile==12):  #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la bille dans le niveau
                print("nouvelle bille")
            if (numeroTile==32):
                vie+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la vie dans le niveau
                print("nouvelle vie")
            else:
                print("fond noir")
            if compteurBilles==174:
                print("Bien joué vous venez de gagner")
                loop = False
            if event.unicode == 'x':
                suprBilles()




    if(pacX * TITLE_SIZE,pacY * TITLE_SIZE)==(posfX * TITLE_SIZE,posfY * TITLE_SIZE):
        vie=vie-1
        pacX=1
        pacY=1
        fenetre.blit(tiles[14],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))
        print("Vous venez de perdre une vie")
    if(pacX * TITLE_SIZE,pacY * TITLE_SIZE)==(posfX2 * TITLE_SIZE,posfY2 * TITLE_SIZE):
        vie=vie-1
        pacX=1
        pacY=1
        fenetre.blit(tiles[14],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))
        print("Vous venez de perdre une vie")
    if(pacX * TITLE_SIZE,pacY * TITLE_SIZE)==(posfX3 * TITLE_SIZE,posfY3 * TITLE_SIZE):
        vie=vie-1
        pacX=1
        pacY=1
        fenetre.blit(tiles[14],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))
        print("Vous venez de perdre une vie")
    if vie==0:
        print("Vous venez de perdre la partie")
        loop = False

    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    #affichePac(14)          #affiche la pacman et le score
    fenetre.blit(tiles[directionPac],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))
    deplaceFantome(fantome) #mettre un commentaire pour desactiver le déplacement du fantome
    deplaceFantome2(fantome2)
    deplaceFantome3(fantome3)
    afficheScore(compteurBilles)
    afficheVie(vie)
    pygame.display.update() #mets à jour la fentre graphique
pygame.quit()

