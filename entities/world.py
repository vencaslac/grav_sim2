import pygame
import json
from .sim import *
from .particle import *

class World:

    def __init__(self):
        self.cfg=json.load(open('settings.cfg'))
        self.win_size=[int(item) for item in self.cfg['Graphics']['window_size'].split(',')]
        self.sim=self.configure_sim()
        self.display=self.init_display()
        self.cpos=(0,0)
        self.focus_particle=-1
        self.camera_lock=False

    def configure_sim(self):
        ''' instantiates the simulation based on parameters given in
            the settings.cfg file which is a simple json
        '''

        return Sim(int(self.cfg['Sim']['Particles']['N_PARTS']),\
                    int(self.cfg['Sim']['Particles']['SPREAD']),\
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
        for p in self.sim.particles:
            try:
                p.draw(self.display,self.cpos)
            except:
                pass
        pygame.display.update()
