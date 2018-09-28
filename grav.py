import classes
import time
import os
import pygame
import numpy as np

pygame.init()

clock = pygame.time.Clock()
wx = 1500
wy = 1100
window_size = (wx,wy)
interface = pygame.display.set_mode(window_size)
pygame.display.set_caption('MZ gravity sim')
S=classes.Sim(700,1500)


egzit=False
while not egzit:
    now=time.time()
    pixels = pygame.PixelArray(interface)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            egzit = True

    S.time_step()
    interface.fill((0,0,0))
    #interface=S.draw_field((wx,wy))
    for p in S.particles:
        try:
            p.draw(interface)
        except:
            pass
    pygame.display.update()
    os.system('cls')
    print(1/(time.time()-now))
pygame.quit()
quit()
