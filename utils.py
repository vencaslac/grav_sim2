import os
import json
from random import randint

import numpy as np
import pygame
import math
from numba import jit,njit,cuda
from scipy.spatial.distance import cdist,euclidean


@jit(parallel=True)
def gforce(g,x1,x2,d,m1,m2):
    '''computes gforce between two particles on one axis using numba parellelization'''

    return g*math.sin((x1-x2)/d)*(m1*m2/(d**2))

@jit(parallel=True)
def g_from_part(g,m,d):
    '''computes the field strength value of a particle of mass m at a distance d
        given gravitational constant g
    '''
    return g*m/d**2

@jit(parallel=True)
def build_field(g,masses,pixels,coords):
    '''computes 2d gravitational field plot on a pixel array defined by the pixels
        parameter given a list of masses, their coordinates and gravitational
        constant g
    '''
    #TODO: FIX THIS FUNCTIOn

    p=np.zeros(pixels)
    for i in range(pixels[0]):
        for j in range(pixels[1]):
            distances=cdist([(i,j)],np.asarray(coords),'euclidean')
            for k in range(len(distances)):
                p[i,j]=np.int(g_from_part(g,masses[k],distances[k])*10e10)

    return p

@jit(parallel=True)
def compute_gravity(G=0,masses=[],coords='',distances=''):
    '''computes accelerations for each particle in the masses list via brute force
        using numba to parellize nested loops
    '''

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
