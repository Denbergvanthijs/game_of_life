import time

from Simulator import *
from Visualisation import *

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(100, p=[0.5, 0.5])
    sim = Simulator("B358/S237", world=w)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)
