import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((840, 680))
fenetre.fill([10,186,171])

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()

fenetre.blit(perso, position_perso)

pygame.display.flip()

pygame.time.delay(1000)

while True :
  pass
