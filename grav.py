import entities.world as world
import time
import os
import pygame

w=world.World()
egzit=False
testpar=-1

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
            elif event.key == pygame.K_m and pressed == False:
                w.focus_particle +=1
                if w.focus_particle > len(w.sim.particles)-1:
                    w.focus_particle=0
                pressed = True
            elif event.key == pygame.K_n and pressed == False:
                w.focus_particle -=1
                if w.focus_particle < 0:
                    w.focus_particle = len(w.sim.particles)-1
                pressed = True
            elif event.key == pygame.K_SPACE and pressed == False:
                if w.camera_lock:
                    w.camera_lock=False
                else:
                    w.camera_lock=True
                pressed = True



    print('{}|{}|{}'.format(str(w.cpos),str(w.sim.particles[testpar].coords),str(w.win_size)))

    w.update()

pygame.quit()
quit()
