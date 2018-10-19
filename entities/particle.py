import numpy as np
import pygame
import math

class Particle:

    def __init__(self,name='',coords=np.array([0,0]),mass=0,density=0):
        self.name = name
        self.coords = coords
        self.mass = mass
        self.density = density
        self.color=(255,255,255)
        self.radius=math.sqrt(self.mass/self.density)
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])

    def move(self):
        self.vel=self.vel+self.acc
        self.coords=self.coords+self.vel

    def draw(self,surface,cpos):
        pygame.draw.circle(surface,
                            self.color,
                            (int(round(self.coords[0]-cpos[0])),int(round(self.coords[1]-cpos[1]))),
                            int(self.radius)
                        )
