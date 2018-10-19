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

    w.update()

pygame.quit()
quit()
