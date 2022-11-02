import pygame
import random
import time

###INITIALISATION
pygame.init()

ecran=pygame.display.set_mode((1000,800))

image=pygame.image.load("D:\...\sprites\personnage\gnu.png").convert_alpha()    #choisir le chemin de l'emplacement de l'image pour le personnage en png

alien=image.get_rect()
alien.x=400
alien.y=300

start_time=pygame.time.get_ticks()

k=2000  #)compteurs deg pour slow la tp
b=1000  #)

###FONCTION
def deplacement_droite(touches,bonhomme):
    if touches[pygame.K_RIGHT]==1:
        bonhomme.x+=1

def deplacement_gauche(touches,bonhomme):
    if touches[pygame.K_LEFT]==1:
        bonhomme.x+=-1

def deplacement_haut(touches,bonhomme):
    if touches[pygame.K_UP]==1:
        bonhomme.y+=-1

def deplacement_bas(touches,bonhomme):
    if touches[pygame.K_DOWN]==1:
        bonhomme.y+=1


def limite():
    if alien.x==-1:
        alien.x=0
    if alien.y==-1:
        alien.y=0
    if alien.x==936:
        alien.x=935
    if alien.y==711:
        alien.y=710


def objectif():
    objectif_x=random.randint(0,950)
    objectif_y=random.randint(0,750)
    objectif = pygame.Rect(objectif_x,objectif_y,20,20)
    return objectif


objecti=objectif()
mechan=objectif()
bonu=objectif()
points=0
score_fin=0


###ACTION
while True:


#obligatoire mais sert a rien (obligé de mettre une action (variable a))
    for evenement in pygame.event.get():
        a=0


#afficher l'image de l'alien tout le temps
    ecran.blit(image, alien)


#bord
    limite()


#score
    police=pygame.font.Font(None,60)
    texte=police.render(str(points),True,pygame.Color('white'))
    score=texte.get_rect()
    ecran.blit(texte, score)


#timer
    if (pygame.time.get_ticks()-start_time)/1000 > 40:
        pygame.quit()
#ecran de fin quand t'es arrivé à la fin du timer
        pygame.init()
        ecran = pygame.display.set_mode((400, 300))


        bruh=pygame.font.Font(None,50)
        text_fin=bruh.render(str(score_fin)+"       Game Over",True,pygame.Color('red'))
        impec=text_fin.get_rect()
        impec.y=135
        ecran.blit(text_fin,impec)


        pygame.display.update()
        time.sleep(5)
        pygame.quit()


#points/boules
    pygame.display.update()
    ecran.fill(pygame.Color('pink'))
    pygame.draw.rect(ecran, pygame.Color('red'),objecti)
    pygame.draw.rect(ecran, pygame.Color('dark blue'),mechan)
    pygame.draw.rect(ecran, pygame.Color('gold'),bonu)


#collision alien et point rouge
    collision = alien.colliderect(objecti)
    if collision:
        objecti=objectif()
        points+=1
        score_fin=points


#collision alien et point bleu
    coco = alien.colliderect(mechan)
    if not coco:
        k-=1     #k=2000 a l'init pour tempo et pas qu'il se tp instant (moyen un peu moche)
        if k==0:
            mechan=objectif()
            k=2000
    else:
        pygame.quit()
#ecran de fin quand tu tapes l'ennemi
        pygame.init()
        ecran = pygame.display.set_mode((400, 300))


        bruh=pygame.font.Font(None,50)
        text_fin=bruh.render(str(score_fin)+"       Game Over",True,pygame.Color('red'))
        impec=text_fin.get_rect()
        impec.y=135
        ecran.blit(text_fin,impec)


        pygame.display.update()
        time.sleep(5)
        pygame.quit()


#collision alien et point jaune
    impact_divin = alien.colliderect(bonu)
    if not impact_divin:
        b-=1
        if b==0:
            bonu=objectif()
            b=1000
    else:
        points+=10
        bonu=objectif()



#déplacements
    touches=pygame.key.get_pressed()
    deplacement_droite(touches,alien)
    deplacement_gauche(touches,alien)
    deplacement_haut(touches,alien)
    deplacement_bas(touches,alien)
