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

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            egzit = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                w.cpos = (w.cpos[0],w.cpos[1]-100)

            elif event.key == pygame.K_DOWN:
                w.cpos = (w.cpos[0],w.cpos[1]+100)

            elif event.key == pygame.K_RIGHT:
                w.cpos = (w.cpos[0]+100,w.cpos[1])

            elif event.key == pygame.K_LEFT:
                w.cpos = (w.cpos[0]-100,w.cpos[1])

            elif event.key == pygame.K_m:
                w.focus_particle +=1
                if w.focus_particle > len(w.sim.particles)-1:
                    w.focus_particle=0

            elif event.key == pygame.K_n:
                w.focus_particle -=1
                if w.focus_particle < 0:
                    w.focus_particle = len(w.sim.particles)-1

            elif event.key == pygame.K_SPACE:
                if w.camera_lock:
                    w.camera_lock=False
                else:
                    w.camera_lock=True

            elif event.key == pygame.K_g:
                if w.show_grid:
                    w.show_grid=False
                else:
                    w.show_grid=True

            elif event.key == pygame.K_f:
                if w.show_forces:
                    w.show_forces=False
                else:
                    w.show_forces=True

    os.system('cls')
    testpar=w.sim.particles[w.focus_particle]
    print('Name:{}\n'.format(str(testpar.name)))
    print('Mass:{}\n'.format(str(testpar.mass)))
    print('Density:{}\n'.format(str(testpar.density)))
    print('Radius:{}\n'.format(str(testpar.radius)))
    print('Temperature:{}\n'.format(str(testpar.temperature)))

    w.update()

pygame.quit()
quit()
