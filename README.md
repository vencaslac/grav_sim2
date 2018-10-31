## GRAV SIM 2

### What is it?

This is my personal attempt at an n body gravity simulation.

### What's it for?
The intent is to make good on a promiss to my highschool physics teacher and build a tool that is
intuitive for her to use in teaching kids about Newtonian Mechanics.

### How do I install it?
This is a python project, so you will need to install python 3.x You can clone
the project and use pip to install its' dependencies. Just open a command window
in the repo root and type:

> pip install -r requirements.txt

### What am I looking at?

The screen displays a two dimensional space with particles that have mass and are influenced by gravity
Particles are characterized by mass and density which in turn are used to compute the radius and temperature.
Temperature is the measure by which color is computed based on the ideal gas law.
For aesthetic reasons I have chosen to display the Particles as though they were stars and are named as such in the
console window.

### How do I use it?

- You can modify the _settings.cfg_ file to alter the initial state of the simulation, though
  as this is a work in progress some of the toggles may not currently work
- To start the simulation type the following in a command window in the root directory
  > python grav.py
- Key Bindings:
  - Arrow keys to move the camera around
  - Spacebar to lock the camera to a particle
  - Lowercase 'm' and 'n' cycle between particles from hottest to coolest
  - Lowercase 'f' toggles the display of force vectors on top of the particles
  - Lowercase 'g' toggles the display of the cartesian grid giving a better understanding of the relative motion of particles
