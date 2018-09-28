import os
import json
from random import randint

import numpy as np
import pygame
import math
from numba import jit,njit,cuda
from scipy.spatial.distance import cdist,euclidean


@jit(parallel=True)
def gforce(g,xa,xb,d,m1,m2):

    return g*math.sin((xa-xb)/d)*(m1*m2/(d**2))

@jit(parallel=True)
def g_from_part(g,m,d):
    return g*m/d**2

@jit(parallel=True)
def build_field(g,masses,pixels,coords):
    p=np.zeros(pixels)
    for i in range(pixels[0]):
        for j in range(pixels[1]):
            distances=cdist([(i,j)],np.asarray(coords),'euclidean')
            for k in range(len(distances)):
                p[i,j]=np.int(g_from_part(g,masses[k],distances[k])*10e10)

    return p

@jit(parallel=True)
def compute_gravity(G=0,masses=[],coords='',distances=''):
    accelerations = []
    for i in range(len(masses)):
        fx = 0
        fy = 0
        for j in range(len(masses)):
            if i!=j:
                if coords[i][0] < coords[j][0] and coords[i][1] < coords[j][1]:
                    fx += gforce(G,coords[j][0],coords[i][0],distances[i,j],masses[i],masses[j])
                    fy += gforce(G,coords[j][1],coords[i][1],distances[i,j],masses[i],masses[j])
                if coords[i][0] > coords[j][0] and coords[i][1] < coords[j][1]:
                    fx -= gforce(G,coords[i][0],coords[j][0],distances[i,j],masses[i],masses[j])
                    fy += gforce(G,coords[j][1],coords[i][1],distances[i,j],masses[i],masses[j])
                if coords[i][0] > coords[j][0] and coords[i][1] > coords[j][1]:
                    fx -= gforce(G,coords[i][0],coords[j][0],distances[i,j],masses[i],masses[j])
                    fy -= gforce(G,coords[i][1],coords[j][1],distances[i,j],masses[i],masses[j])
                if coords[i][0] < coords[j][0] and coords[i][1] > coords[j][1]:
                    fx += gforce(G,coords[j][0],coords[i][0],distances[i,j],masses[i],masses[j])
                    fy -= gforce(G,coords[i][1],coords[j][1],distances[i,j],masses[i],masses[j])
        accelerations.append((fx/masses[i],fy/masses[i]))

    return accelerations

# @jit(parallel=True)
# def compute_gravity(G=0,masses=[],coords='',distances='',acc=''):
#     for i in range(len(masses)-2):
#         for j in range(i+1,len(masses)-1):
#             if coords[i][0] < coords[j][0] and coords[i][1] < coords[j][1]:
#                 fx = gforce(G,coords[j][0],coords[i][0],distances[i,j],masses[i],masses[j])
#                 fy = gforce(G,coords[j][1],coords[i][1],distances[i,j],masses[i],masses[j])
#             if coords[i][0] > coords[j][0] and coords[i][1] < coords[j][1]:
#                 fx = -gforce(G,coords[i][0],coords[j][0],distances[i,j],masses[i],masses[j])
#                 fy = gforce(G,coords[j][1],coords[i][1],distances[i,j],masses[i],masses[j])
#             if coords[i][0] > coords[j][0] and coords[i][1] > coords[j][1]:
#                 fx = -gforce(G,coords[i][0],coords[j][0],distances[i,j],masses[i],masses[j])
#                 fy = -gforce(G,coords[i][1],coords[j][1],distances[i,j],masses[i],masses[j])
#             if coords[i][0] < coords[j][0] and coords[i][1] > coords[j][1]:
#                 fx = gforce(G,coords[j][0],coords[i][0],distances[i,j],masses[i],masses[j])
#                 fy = -gforce(G,coords[i][1],coords[j][1],distances[i,j],masses[i],masses[j])
#             acc[i]+=np.array([fx/masses[i],fy/masses[i]])
#             acc[j]-=np.array([fx/masses[j],fy/masses[j]])
#     return acc


class World:

    def __init__(self):
        self.cfg=json.loads(open('settings.cfg','rt').read())

class Sim:

    def __init__(self,N_PARTS=0,SPREAD=0):
        self.N_PARTS=N_PARTS
        self.SPREAD=SPREAD
        self.particles=[Particle(str(i),np.array((float(randint(0,self.SPREAD)),float(randint(0,self.SPREAD)))),
                        randint(1,255),1) for i in range(self.N_PARTS)]
        self.G=1#6.674e-11
        self.flags={
                    'show_field':False,
                    'show_forces':False,
                    'show_grid':False,
                    'camera_lock':False,
                    }

    def apply_gravity(self):
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

    def process_flags(self):
        pass

    def time_step(self):
        self.apply_gravity()
        self.process_flags()

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

    def draw(self,surface):
        pygame.draw.circle(surface,
                            self.color,
                            (int(round(self.coords[0])),int(round(self.coords[1]))),
                            int(self.radius)
                        )
