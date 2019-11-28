from unittest import TestCase

from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator("B358/S237")

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_get_rules(self):
        """
        Test of een string correct wordt omgezet naar een regelset.
        """
        input = "B358/S237"
        self.assertEqual(self.sim.get_rules(input), ([3, 5, 8], [2, 3, 7]))

    def test_update_cell(self):
        """
        Test of een cell correct wordt geupdatet.
        Rules: "B358/S237"
        """
        world = World(3, 3)
        self.sim.set_world(world)


        ### VOLLEDIGE WORLD
        self.sim.world.fill_world(p=[0, 1])  # Vult de wereld volledig, cell zelf leeft ook
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(0, cell)  # Test of cell dood gaat aangezien alles leeft

        self.sim.world.fill_world(p=[1, 0]); self.sim.world.set(1,1)  # Leegt de wereld volledig, cell zelf leeft
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(0, cell)  # Test of cell dood gaat aangezien geen neighbour leeft


        ### BIRTH TESTS
        self.sim.world.fill_world(p=[1, 0])  # Leegt de wereld volledig
        self.sim.world.set(0,0); self.sim.world.set(0,1); self.sim.world.set(0,2)
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell tot leven is gekomen bij drie neighbours

        self.sim.world.set(1,0)  # Vierde neighbour
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell tot leven is gekomen bij vier neighbours

        self.sim.world.fill_world(p=[0, 1])  # Vult de wereld volledig
        self.sim.world.set(1, 1, value=0)  # Alle neighbours leven, cell zelf niet
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell tot leven is gekomen bij acht neigbours


        ### SURVIVAL TESTS
        self.sim.world.fill_world(p=[1, 0])  # Leegt de wereld volledig
        self.sim.world.set(0, 0); self.sim.world.set(0, 1); self.sim.world.set(1, 1)  # Twee neighbours en de cell zelf leven
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell overleeft bij twee neigbours

        self.sim.world.set(0, 2)  # Derde neighbour
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell overleeft bij drie neigbours

        self.sim.world.fill_world(p=[0, 1])  # Vult de wereld volledig
        self.sim.world.set(0, 0, value=0); self.sim.world.set(1, 1, value=0)  # Zeven neighbours leven, cell zelf niet
        cell = self.sim.update_cell(1, 1)
        self.assertEqual(1, cell)  # Test of de cell overleeft bij zeven neigbours