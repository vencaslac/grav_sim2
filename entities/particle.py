import numpy as np
import pygame
import math
from utils import *


class Particle:

    def __init__(self,name='',coords=np.array([0,0]),mass=0,density=0,G=0):
        self.name = name
        self.coords = coords
        self.density = min(density,mass)
        self.mass = mass
        self.radius=math.sqrt(self.mass/self.density)
        self.temperature=self.compute_temp(G)
        self.color=self.compute_color()
        self.sprite_it=0
        self.sprites=[self.build_sprite() for i in range(30)]
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])

    def compute_color(self):
        if self.temperature < 255:
            red = int(self.temperature)
            green = 0
            blue = 0
        elif self.temperature >= 255 and self.temperature < 510:
            red = 255
            green = int(self.temperature - 255)
            blue = 0
        elif self.temperature >= 510 and self.temperature < 765:
            red = 255
            green = 255
            blue = int(self.temperature - 510)
        elif self.temperature >= 765 and self.temperature < 1020:
            red = int(255 - (1020 - self.temperature))
            green = 255
            blue = 255
        elif self.temperature >= 1020 and self.temperature < 1275:
            red = 0
            green = int(255 - (1275 - self.temperature))
            blue = 255
        elif self.temperature > 1275:
            red = 0
            green = 0
            blue=255

        color=(red,green,blue,0)
        return color

    def build_sprite(self):
        sp=np.zeros((int(round(self.radius*2)),int(round(self.radius*2)),3))
        srf = pygame.surfarray.make_surface(generate_sprite(0,self.radius,self.radius/2,sp,self.color))
        #srf.flags = pygame.SRCALPHA

        return srf

    def compute_temp(self,G):
        G=G
        M=1
        R=8.314
        r= self.radius
        return (G*M*self.mass)/(R*r)

    def move(self):
        self.vel=self.vel+self.acc
        self.coords=self.coords+self.vel

    def draw(self,surface,cpos):
        # pygame.draw.circle(surface,
        #                     self.color,
        #                     (int(round(self.coords[0]-cpos[0])),int(round(self.coords[1]-cpos[1]))),
        #                     int(self.radius)
        #                 )
        if self.sprite_it>29:
            self.sprite_it=0
        surface.blit(self.sprites[self.sprite_it],(int(round(self.coords[0]-cpos[0]-self.radius)),int(round(self.coords[1]-cpos[1]-self.radius))))
        self.sprite_it+=1

    def draw_forces(self,surface,cpos):
        fx=self.mass*self.acc[0]
        fy=self.mass*self.acc[1]
        pygame.draw.line(surface,(255,0,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]),3)
        pygame.draw.line(surface,(0,255,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0],self.coords[1]-cpos[1]+fy*100),3)
        pygame.draw.line(surface,(0,0,255),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]+fy*100),3)
