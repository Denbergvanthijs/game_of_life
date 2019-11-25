import time

from Simulator import *
from Visualisation import *

# Configuratie
VISUALISATION=False

if __name__ == "__main__":
    w = World(10, 4)
    sim = Simulator(w)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)
