#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame import key
from classes.SpeechGoogle import *
from classes.staticLists import *
from classes.PlaySil import *

pygame.init()
pygame.mixer.quit()

#speech = SpeechPlay

screen = pygame.display.set_mode((1024,768),0,32)
pygame.display.set_caption("PyMumu v0.1a")

#pleyarLetras = QualLetra()
#pleyarLetras.selectLetra()
#imgLetra = pygame.image.load("images/alfabeto/"+pleyarLetras.selectedLetra.lower()+".png").convert()

#img_x_position_initial = (1024/100)*30
#img_y_position_initial = (768/100)*8

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

#        screen.blit(imgLetra, (img_x_position_initial,img_y_position_initial))

        if event.type == KEYDOWN:
            if event.key:
                pass
#                if pleyarLetras.checkResult(key.name(event.key)):
#                    imgLetra = pygame.image.load(
#                        "images/alfabeto/" + pleyarLetras.selectedLetra.lower() + ".png").convert()

        pygame.display.update()



