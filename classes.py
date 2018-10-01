from utils import *

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
