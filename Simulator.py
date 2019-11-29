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

        for y, row in enumerate(self.world.world):
            for x, _ in enumerate(row):
                world_new.set(x, y, value=self.update_cell(x, y))
        
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
        if "A" in rule:
            birth, surv, age = rule.split("/")        
            ageMax = [int(x) for x in age if x.isdigit()][0]
        else:
            birth, surv = rule.split("/")
            ageMax = 1
    
        birth = [int(x) for x in birth if x.isdigit()]
        surv = [int(x) for x in surv if x.isdigit()]

        return birth, surv, ageMax

    def update_cell(self, x, y):
        neigh_arr = self.world.get_neighbours(x, y)
        cell_val = self.world.get(x, y)
        birth, surv, ageMax = self.get_rules(self.rule_str)

        if self.world.startAge > 1:
            neigh_fertile = len([1 for x in neigh_arr if 2 <= x <= ageMax - 2])
        else:
            neigh_fertile = np.count_nonzero(neigh_arr)        

        if self.world.get(y, x):  # If levend
            if neigh_fertile in surv:  # If overleven
                return min(cell_val + 1, ageMax)
        else:  # If dood
            if neigh_fertile in birth:  # If n neigbours in surv
                return ageMax
        return max(cell_val - 1, 0)