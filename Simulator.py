from World import *
import copy

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, rule_str, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.rule_str = rule_str
        self.generation = 0

        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        world_new = copy.deepcopy(self.world)
        birth, surv = self.get_rules(self.rule_str)

        for i, row in enumerate(self.world.world):
            for j, _ in enumerate(row):
                neigh = np.sum(self.world.get_neighbours(i, j))
                
                if world_new.get(j, i):  # If levend
                    if not (neigh == any(surv)):  # If niet overleven
                        world_new.set(j, i, value=0)
                else:  # If dood
                    if neigh == any(birth):  # If n neigbours in surv
                        world_new.set(j, i, value=1)

        
        self.set_world(world_new)
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

    def get_rules(self, rule):
        """
        Zet een string om naar twee lijsten met het aantal mogelijke buren voor resp. de birth en de survival
        """
        birth, surv = rule.split("/")
        
        birth = [int(x) for x in birth if x.isdigit()]
        surv = [int(x) for x in surv if x.isdigit()]

        return birth, surv