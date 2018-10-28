import pygame
from random import randint
from utils import *
from .particle import *

class Sim:

    def __init__(self,N_PARTS=0,SPREAD=0,M_SPREAD=0,D_SPREAD=1,G=0):
        self.G=G#6.674e-11
        self.N_PARTS=N_PARTS
        self.SPREAD=SPREAD
        self.M_SPREAD=M_SPREAD
        self.D_SPREAD=D_SPREAD
        self.particles=[Particle(str(i),np.array((float(randint(0,self.SPREAD)),float(randint(0,self.SPREAD)))),
                        min(self.M_SPREAD,round(int(self.M_SPREAD*randint(1,self.M_SPREAD)/randint(1,self.M_SPREAD)**2))+1),
                        randint(1,self.D_SPREAD),self.G) for i in range(self.N_PARTS)]
        self.particles.sort(key=lambda p:p.temperature)
        self.flags={
                    'show_field':False,
                    'show_forces':False,
                    'show_grid':False,
                    'camera_lock':False,
                    }

    def apply_gravity(self):
        '''applies gravity to every particle in the sim class'''

        masses=[]
        coords=[]
        acc=[]
        for p in self.particles:
            masses.append(p.mass)
            coords.append(p.coords)
            acc.append(np.array([0.0,0.0]))
        distances=cdist(coords,coords,'euclidean')
        # for p,a in zip(self.particles,compute_gravity(self.G,masses,coords,distances,acc)):
        #     p.acc=np.array(a)
        for p,a in zip(self.particles,compute_gravity(self.G,masses,coords,distances)):
            p.acc=np.array(a)

        [p.move() for p in self.particles]

    def time_step(self):
        self.apply_gravity()
