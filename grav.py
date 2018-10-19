import entities.world as world
import time
import os
import pygame

w=world.World()
egzit=False
while not egzit:
    now=time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            egzit = True
        elif event.type == pygame.KEYDOWN:
            pressed = False
            if event.key == pygame.K_UP and pressed == False:
                w.cpos = (w.cpos[0],w.cpos[1]-100)
                pressed = True
            elif event.key == pygame.K_DOWN and pressed == False:
                w.cpos = (w.cpos[0],w.cpos[1]+100)
                pressed = True
            elif event.key == pygame.K_RIGHT and pressed == False:
                w.cpos = (w.cpos[0]+100,w.cpos[1])
                pressed = True
            elif event.key == pygame.K_LEFT and pressed == False:
                w.cpos = (w.cpos[0]-100,w.cpos[1])
                pressed = True

    w.update()

pygame.quit()
quit()
