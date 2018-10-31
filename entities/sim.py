import pygame
from random import randint,choice
from utils import *
from .particle import *


#TODO move this to some kind of constants file
s_names=[
        'Acamar',\
        'Achernar',\
        'Achird',\
        'Acrab',\
        'Acrux',\
        'Acubens',\
        'Adhafera',\
        'Adhara',\
        'Adhil',\
        'Ain',\
        'Ainalrami',\
        'Aladfar',\
        'Alamak †',\
        'Alathfar †',\
        'Albaldah',\
        'Albali',\
        'Albireo',\
        'Alchiba',\
        'Alcor',\
        'Alcyone',\
        'Aldebaran',\
        'Alderamin',\
        'Aldhanab',\
        'Aldhibah',\
        'Aldulfin',\
        'Alfirk',\
        'Algedi',\
        'Algenib',\
        'Algieba',\
        'Algol',\
        'Algorab',\
        'Alhena',\
        'Alioth',\
        'Aljanah',\
        'Alkaid',\
        'Al Kalb al Rai †',\
        'Alkalurops',\
        'Alkaphrah',\
        'Alkarab',\
        'Alkes',\
        'Almaaz',\
        'Almach',\
        'Al Minliar al Asad †',\
        'Alnair',\
        'Alnasl',\
        'Alnilam',\
        'Alnitak',\
        'Alniyat',\
        'Alphard',\
        'Alphecca',\
        'Alpheratz',\
        'Alpherg',\
        'Alrakis',\
        'Alrescha',\
        'Alruba',\
        'Alsafi',\
        'Alsciaukat',\
        'Alsephina',\
        'Alshain',\
        'Alshat',\
        'Altair',\
        'Altais',\
        'Alterf',\
        'Aludra',\
        'Alula Australis',\
        'Alula Borealis',\
        'Alya',\
        'Alzirr',\
        'Ancha',\
        'Angetenar',\
        'Ankaa',\
        'Anser',\
        'Antares',\
        'Arcturus',\
        'Arkab Posterior',\
        'Arkab Prior',\
        'Arneb',\
        'Ascella',\
        'Asellus Australis',\
        'Asellus Borealis',\
        'Ashlesha',\
        'Asellus Primus †',\
        'Asellus Secundus †',\
        'Asellus Tertius †',\
        'Asmidiske †',\
        'Aspidiske',\
        'Asterope',\
        'Athebyne',\
        'Atik',\
        'Atlas',\
        'Atria',\
        'Avior',\
        'Azelfafage',\
        'Azha',\
        'Azmidi',\
        'Barnard\'s Star',\
        'Baten Kaitos',\
        'Beemim',\
        'Beid',\
        'Bellatrix',\
        'Betelgeuse',\
        'Bharani',\
        'Biham',\
        'Botein',\
        'Brachium',\
        'Bunda',\
        'Canopus',\
        'Capella',\
        'Caph',\
        'Castor',\
        'Castula',\
        'Cebalrai',\
        'Celaeno',\
        'Cervantes',\
        'Chalawan',\
        'Chamukuy',\
        'Chara',\
        'Chertan',\
        'Copernicus',\
        'Cor Caroli',\
        'Cujam',\
        'Cursa',\
        'Dabih',\
        'Dalim',\
        'Deneb',\
        'Deneb Algedi',\
        'Denebola',\
        'Diadem',\
        'Diphda',\
        'Dschubba',\
        'Dubhe',\
        'Dziban',\
        'Edasich',\
        'Electra',\
        'Elgafar',\
        'Elkurud',\
        'Elnath',\
        'Eltanin',\
        'Enif',\
        'Errai',\
        'Fafnir',\
        'Fang',\
        'Fawaris',\
        'Felis',\
        'Fomalhaut',\
        'Fulu',\
        'Fumalsamakah',\
        'Furud',\
        'Fuyue',\
        'Gacrux',\
        'Garnet Star †',\
        'Giausar',\
        'Gienah',\
        'Ginan',\
        'Gomeisa',\
        'Graffias †',\
        'Grumium',\
        'Gudja',\
        'Guniibuu',\
        'Hadar',\
        'Haedus',\
        'Hamal',\
        'Hassaleh',\
        'Hatysa',\
        'Helvetios',\
        'Heze',\
        'Homam',\
        'Iklil',\
        'Imai',\
        'Intercrus',\
        'Izar',\
        'Jabbah',\
        'Jishui',\
        'Kaffaljidhma',\
        'Kang',\
        'Kaus Australis',\
        'Kaus Borealis',\
        'Kaus Media',\
        'Keid',\
        'Khambalia',\
        'Kitalpha',\
        'Kochab',\
        'Kornephoros',\
        'Kraz',\
        'Kuma †',\
        'Kurhah',\
        'La Superba',\
        'Larawag',\
        'Lesath',\
        'Libertas',\
        'Lich',\
        'Lilii Borea',\
        'Maasym',\
        'Mahasim',\
        'Maia',\
        'Marfark †',\
        'Marfik',\
        'Markab',\
        'Markeb',\
        'Marsic',\
        'Matar',\
        'Mebsuta',\
        'Megrez',\
        'Meissa',\
        'Mekbuda',\
        'Meleph',\
        'Menkalinan',\
        'Menkar',\
        'Menkent',\
        'Menkib',\
        'Merak',\
        'Merga',\
        'Meridiana',\
        'Merope',\
        'Mesarthim',\
        'Miaplacidus',\
        'Mimosa',\
        'Minchir',\
        'Minelauva',\
        'Mintaka',\
        'Mira',\
        'Mirach',\
        'Miram',\
        'Mirfak',\
        'Mirzam',\
        'Misam',\
        'Mizar',\
        'Mothallah',\
        'Muliphein',\
        'Muphrid',\
        'Muscida',\
        'Musica',\
        'Nahn',\
        'Naos',\
        'Nashira',\
        'Navi †',\
        'Nekkar',\
        'Nembus',\
        'Nihal',\
        'Nunki',\
        'Nusakan',\
        'Ogma',\
        'Okab',\
        'Paikauhale',\
        'Peacock',\
        'Phact',\
        'Phecda',\
        'Pherkad',\
        'Piautos',\
        'Pipirima',\
        'Pleione',\
        'Polaris',\
        'Polaris Australis',\
        'Polis',\
        'Pollux',\
        'Porrima',\
        'Praecipua',\
        'Prima Hyadum',\
        'Procyon',\
        'Propus',\
        'Proxima Centauri',\
        'Ran',\
        'Rana †',\
        'Rasalas',\
        'Rasalgethi',\
        'Rasalhague',\
        'Rastaban',\
        'Regor †[citation needed]',\
        'Regulus',\
        'Revati',\
        'Rigel',\
        'Rigil Kentaurus',\
        'Rotanev',\
        'Ruchbah',\
        'Rukbat',\
        'Sabik',\
        'Saclateni',\
        'Sadachbia',\
        'Sadalbari',\
        'Sadalmelik',\
        'Sadalsuud',\
        'Sadr',\
        'Saiph',\
        'Salm',\
        'Sargas',\
        'Sarin',\
        'Sarir †',\
        'Sceptrum',\
        'Scheat',\
        'Schedar',\
        'Secunda Hyadum',\
        'Segin',\
        'Seginus',\
        'Sham',\
        'Shaula',\
        'Sheliak',\
        'Sheratan',\
        'Sirius',\
        'Situla',\
        'Skat',\
        'Spica',\
        'Sualocin',\
        'Subra',\
        'Suhail',\
        'Sulafat',\
        'Syrma',\
        'Tabit',\
        'Taiyangshou',\
        'Taiyi',\
        'Talitha',\
        'Tania Australis',\
        'Tania Borealis',\
        'Tarazed',\
        'Tarf',\
        'Taygeta',\
        'Tegmine',\
        'Tejat',\
        'Terebellum',\
        'Thabit †',\
        'Theemin',\
        'Thuban',\
        'Tiaki',\
        'Tianguan',\
        'Tianyi',\
        'Titawin',\
        'Toliman',\
        'Tonatiuh',\
        'Torcular',\
        'Tureis',\
        'Ukdah',\
        'Unukalhai',\
        'Unurgunite',\
        'Vega',\
        'Veritate',\
        'Vindemiatrix',\
        'Wasat',\
        'Wazn',\
        'Wezen',\
        'Wurren',\
        'Xamidimura',\
        'Xuange',\
        'Yed Posterior',\
        'Yed Prior',\
        'Yildun',\
        'Zaniah',\
        'Zaurak',\
        'Zavijava',\
        'Zhang',\
        'Zibal',\
        'Zosma',\
        'Zubenelgenubi',\
        'Zubenelhakrabi',\
        'Zubeneschamali'
    ]

class Sim:

    def __init__(self,N_PARTS=0,SPREAD=0,M_SPREAD=0,D_SPREAD=1,G=0):
        self.G=G#6.674e-11
        self.N_PARTS=N_PARTS
        self.SPREAD=SPREAD
        self.M_SPREAD=M_SPREAD
        self.D_SPREAD=D_SPREAD
        self.star_names=s_names
        self.particles=[Particle('',np.array((float(randint(0,self.SPREAD)),float(randint(0,self.SPREAD)))),
                        min(self.M_SPREAD,round(int(self.M_SPREAD*randint(1,self.M_SPREAD)/randint(1,self.M_SPREAD)**2))+1),
                        randint(1,self.D_SPREAD),self.G) for i in range(self.N_PARTS)]
        self.particles.sort(key=lambda p:p.temperature,reverse=True)
        for i in range(len(self.particles)):
            self.particles[i].name=self.pick_star_name()
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

    def pick_star_name(self):
        '''
            picks a name for a star from the available list, if the list is depleted
            a randomized name is generated and made to look sciency by using the actual
            OBFGKM spectral types
        '''

        #TODO make this function output more realistic names

        try:
            name = choice(self.star_names)
            self.star_names.pop(self.star_names.index(name))
        except:
            name = choice(['O','B','F','G','K','M'])+'-'+str(randint(10000,100000))

        return name

    def time_step(self):
        '''
            Steps the simulation forward by one time_step
        '''

        self.apply_gravity()
