import numpy as np
import pygame
from utils import *


class Particle:

    def __init__(self,name='',coords=np.array([0,0]),mass=0,density=0,G=0):
        self.name = name
        self.coords = coords
        self.density = min(density,mass)
        self.mass = mass
        self.radius=(self.mass/self.density)**0.5
        self.temperature=self.compute_temp(G)
        self.color=self.compute_color()
        self.sprite_it=0
        self.sprites=[self.build_sprite() for i in range(3)]
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])

    def compute_color(self):
        '''
            Computes the color of a particle based on it's temperature in a manner
            analogous to real life stars. Cooler particles are redder, hotter ones are bluer"
        '''

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
        '''
            Returns a pygame surface from the np array generated by the utils.generate_sprite() function.
            This is necessary because @jitted functions do not play nicely with classes and so they have to
            be wrapped.
        '''

        sp=np.zeros((int(round(self.radius*2)),int(round(self.radius*2)),3))
        srf = pygame.surfarray.make_surface(generate_sprite(0,self.radius,self.radius/2,sp,self.color))
        srf.set_colorkey((0,0,0))
        return srf

    def compute_temp(self,G):
        '''
            Computes the temperature* of a particle based on the ideal gas law.
            Note that volume was replaced with surface area owing to the 2d nature of this simulation
        '''

        G=G
        M=1
        R=8.314
        r= self.radius
        return (G*M*self.mass)/(R*r)

    def move(self):
        '''
            changes the particles coordinates according it its' velocity
        '''
        self.vel=self.vel+self.acc
        self.coords=self.coords+self.vel

    def draw(self,surface,cpos):
        '''
            draws the particle on a surface relative to the observer's point of view
        '''
        if self.sprite_it>2:
            self.sprite_it=0
        surface.blit(self.sprites[self.sprite_it],(int(round(self.coords[0]-cpos[0]-self.radius)),int(round(self.coords[1]-cpos[1]-self.radius))))
        self.sprite_it+=1

    def draw_forces(self,surface,cpos):
        '''
            draw's the verticle component of the total forces acting on the particle in green
            the horizontal component in red and the total forces in blue
        '''

        fx=self.mass*self.acc[0]
        fy=self.mass*self.acc[1]
        pygame.draw.line(surface,(255,0,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]),3)
        pygame.draw.line(surface,(0,255,0),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0],self.coords[1]-cpos[1]+fy*100),3)
        pygame.draw.line(surface,(0,0,255),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),\
                        (self.coords[0]-cpos[0]+fx*100,self.coords[1]-cpos[1]+fy*100),3)

    def build_tooltip(self,screen_size):

        tooltip = pygame.Surface((screen_size[0]//5,screen_size[1]//3),pygame.SRCALPHA | pygame.HWSURFACE | pygame.HWACCEL)
        tooltip.fill((0,0,0,200))
        pygame.draw.rect(tooltip,(255,255,255,128),pygame.Rect(0,0,screen_size[0]//5,screen_size[1]//3),3)

        return tooltip

    def draw_tooltip(self,surface,cpos):
        t=self.build_tooltip(surface.get_size())
        pygame.draw.line(surface,(255,255,255,128),(self.coords[0]-cpos[0],self.coords[1]-cpos[1]),(surface.get_size()[0]*4//5,surface.get_size()[1]//3),2)
        surface.blit(t,(surface.get_size()[0]*4//5,surface.get_size()[1]//9))
