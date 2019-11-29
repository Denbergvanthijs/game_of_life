from unittest import TestCase

from World import *


class TestWorld(TestCase):
    """
    Test cases for ``World`` data type.
    """
    def setUp(self):
        """
        Common setup for running tests
        """
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)

    def test_set(self):
        """
        Tests setting value on location (x,y).
        """
        x, y = 4, 6
        self.world.set(x, y)
        self.assertEqual(self.world.world[y][x], 1)
        value = 7
        self.world.set(x, y, 7)
        self.assertEqual(self.world.world[y][x], 7)

    def test_get(self):
        """
        Tests getting value from location (x, y).
        """
        x, y = 3, 5
        value = 3
        self.world.world[y][x] = 3
        self.assertEqual(self.world.get(x, y), value)

    def test_get_neighbours(self):
        """
        Tests getting neighbours from location.
        """
        x, y = 2, 0
        value = 4
        self.world.set(x, self.height-1, value)
        neighbours = self.world.get_neighbours(x, y)
        self.assertEqual(8, len(neighbours))
        self.assertIn(value, neighbours)

    def test_fill_world(self):
        """
        Test of een wereld gevuld met n cells ook n cells bevat.
        Kans op levende cell wordt op 100% gezet, iedere cell zou dus levend moeten zijn.
        `self.height * self.width` staat gelijk aan het aantal cells.
        """
        self.world.fill_world(p=[0.0, 1.0])
        self.assertEqual(np.count_nonzero(self.world.world), self.height * self.width)

        # Geen levende cells
        self.world.fill_world(p=[1.0, 0.0])
        self.assertEqual(np.count_nonzero(self.world.world), 0)
