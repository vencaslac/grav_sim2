import classes
import time
import os

S=classes.Sim(5,1500)

print(S.coords)

while True:
    now=time.time()
    S.apply_gravity()
    S.move()
    os.system('cls')
    print(time.time()-now)
    print(S.coords)
