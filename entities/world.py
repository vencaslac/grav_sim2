import pygame
import json
from .sim import *
from .particle import *

class World:

    def __init__(self):
        self.cfg = json.load(open('settings.cfg'))
        self.win_size = [int(item) for item in self.cfg['Graphics']['window_size'].split(',')]
        self.sim = self.configure_sim()
        self.display = self.init_display()
        self.cpos = (0,0)
        self.focus_particle = -1
        self.camera_lock = False
        self.show_grid = self.cfg['App']['show_grid']=='True'
        self.show_forces = self.cfg['App']['show_forces']=='True'

    def configure_sim(self):
        ''' instantiates the simulation based on parameters given in
            the settings.cfg file which is a simple json
        '''

        return Sim(int(self.cfg['Sim']['Particles']['N_PARTS']),\
                    int(self.cfg['Sim']['Particles']['SPREAD']),\
                    int(self.cfg['Sim']['Particles']['M_SPREAD']),\
                    int(self.cfg['Sim']['Particles']['D_SPREAD']),\
                    float(self.cfg['Sim']['Physics']['G']))

    def init_display(self):
        ''' instantiaties a pygame surface display given the configuration in
            the settings.cfg file which is a simple json
        '''

        pygame.init()
        modes = pygame.HWSURFACE | pygame.HWACCEL
        if self.cfg['Graphics']['full_screen'] == 'Yes':
            modes = modes | pygame.FULLSCREEN
        if self.cfg['Graphics']['borderless'] == 'Yes':
            modes = modes | pygame.NOFRAME

        #self.win_size=self.cfg['Graphics']['window_size'].split(',')
        #self.win_size=[int(item) for item in self.win_size]

        return pygame.display.set_mode(self.win_size,modes)

    def update(self):
        '''updates the display'''
        self.sim.time_step()
        self.display.fill((0,0,0))

        if self.camera_lock:
            self.cpos = (int(round(self.sim.particles[self.focus_particle].coords[0]-self.win_size[0]//2)),\
                         int(round(self.sim.particles[self.focus_particle].coords[1]-self.win_size[1]//2)))

        if self.show_grid:
            wx=self.win_size[0]
            wy=self.win_size[1]
            for i in range(int(self.cpos[0]),int(self.cpos[0])+wx):
                if i%500 == 0:
                    pygame.draw.line(self.display,(105,105,125),(i-self.cpos[0],0),(i-self.cpos[0],wx*2),3)
            for i in range(int(self.cpos[1]),int(self.cpos[1])+wy):
                if i%500 == 0:
                    pygame.draw.line(self.display,(105,105,125),(0,i-self.cpos[1]),(wy*2,i-self.cpos[1]),3)

        on_screen=[]
        for p in self.sim.particles:
            if p.coords[0]<self.cpos[0]+self.win_size[0] and p.coords[1]<self.cpos[1]+self.win_size[1]:
                on_screen.append(self.sim.particles.index(p))

        [self.sim.particles[p].draw(self.display,self.cpos) for p in on_screen.__iter__()]
        if self.show_forces:
            [self.sim.particles[p].draw_forces(self.display,self.cpos) for p in on_screen.__iter__()]

        pygame.display.update()
