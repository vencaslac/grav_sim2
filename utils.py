import numpy as np
import math
from numba import jit
import pygame
from scipy.spatial.distance import cdist,euclidean
from random import randint


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
def generate_sprite(taip=0,radius=0,surface_radius=0,sprite=np.array,color=(0,0,0,0)):
    ''' returns a square numpy array of pixel values
        the object is depicted as two noisy grandient filled concentric circles
        the outer most of which is tangent to the square
    '''
    sprite=sprite
    for i in range(sprite.shape[0]):
        for j in range(sprite.shape[1]):
            scale=((i-radius)**2+(j-radius)**2)**0.5/radius
            scale=scale*(randint(-10,10)+100)/100
            if scale >= 1:
                continue
            else:
                for k in range(3):
                    if scale < surface_radius/radius:
                        sprite[i,j,k]=round(int(color[k]-color[k]*scale*randint(40,90)/100))
                    else:
                        sprite[i,j,k]=round(int(color[k]-color[k]*scale))
    return sprite

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
