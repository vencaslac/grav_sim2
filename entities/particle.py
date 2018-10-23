import numpy as np
import pygame
import math

class Particle:

    def __init__(self,name='',coords=np.array([0,0]),mass=0,density=0,G=0):
        self.name = name
        self.coords = coords
        self.density = min(density,mass)
        self.mass = mass
        self.radius=math.sqrt(self.mass/self.density)
        self.temperature=min(765,self.compute_temp(G))
        self.color=self.compute_color()
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])

    def compute_color(self):
        red = max(0,int(255-self.temperature))

        blue = min(255,int(self.temperature))

        green = 0#(red+blue)//2

        color=(red,green,blue)
        return color

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
        pygame.draw.circle(surface,
                            self.color,
                            (int(round(self.coords[0]-cpos[0])),int(round(self.coords[1]-cpos[1]))),
                            int(self.radius)
                        )
    def draw_forces(self,surface,cpos):
        fx=self.mass*self.acc[0]
        fy=self.mass*self.acc[1]
        pygame.draw.line(surface,(255,0,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]),3)
        pygame.draw.line(surface,(0,255,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0],self.coords[1]-cpos[1]+fy*100),3)
        pygame.draw.line(surface,(0,0,255),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]+fy*100),3)
