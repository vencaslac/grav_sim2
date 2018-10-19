import pygame

from utils import *


class World:

    def __init__(self):
        self.cfg=json.load(open('settings.cfg'))
        self.sim=self.configure_sim()
        self.display=self.init_display()

    def configure_sim(self):
        return Sim(int(self.cfg['Sim']['Particles']['N_PARTS']),\
                    int(self.cfg['Sim']['Particles']['SPREAD']),\
                    float(self.cfg['Sim']['Physics']['G']))

    def init_display(self):
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
        self.sim.time_step()
        self.display.fill((0,0,0))
        for p in self.sim.particles:
            try:
                p.draw(self.display)
            except:
                pass
        pygame.display.update()

class Sim:

    def __init__(self,N_PARTS=0,SPREAD=0,G=0):
        self.N_PARTS=N_PARTS
        self.SPREAD=SPREAD
        self.particles=[Particle(str(i),np.array((float(randint(0,self.SPREAD)),float(randint(0,self.SPREAD)))),
                        randint(1,255),1) for i in range(self.N_PARTS)]
        self.G=G#6.674e-11
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
