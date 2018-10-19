import pygame
import json
from .sim import *
from .particle import *

class World:

    def __init__(self):
        self.cfg=json.load(open('settings.cfg'))
        self.sim=self.configure_sim()
        self.display=self.init_display()

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

        win_size=self.cfg['Graphics']['window_size'].split(',')
        win_size=[int(item) for item in win_size]

        return pygame.display.set_mode(win_size,modes)

    def update(self):
        '''updates the display'''
        self.sim.time_step()
        self.display.fill((0,0,0))
        for p in self.sim.particles:
            try:
                p.draw(self.display)
            except:
                pass
        pygame.display.update()
