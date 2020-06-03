import unittest
from knight import Knight
from orcrider import OrcRider
from abstractgameunit import AbstractGameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs


class TestWarGame(unittest.TestCase):
    """
    This class contains unit tests for the game Attack of the Orcs.
    """

    def setUp(self):
        """Overrides the setUp fixture of the superclass"""
        self.knight = Knight()
        self.enemy = OrcRider()

    def test_injured_unit_selection(self):
        """Unit test to verify if the injured unit is
        an instance of class AbstractGameUnit"""
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight, self.enemy)

            self.assertIsInstance(
                injured_unit,
                AbstractGameUnit,
                "Injured unit must be an instance of AbstractGameUnit",
            )
        pass  # TODO: To be implemeneted!


if __name__ == "__main__":
    unittest.main()
