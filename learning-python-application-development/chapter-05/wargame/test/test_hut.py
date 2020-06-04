import unittest
from knight import Knight
from hut import Hut


class TestHut(unittest.TestCase):
    """Contains unit tests for the game Attack of the Orcs"""

    def setUp(self):
        """Called just before calling each unit test"""
        self.knight = Knight()

    def test_acquire_hut(self):
        """Unit test to verify hut occupant after it is acquired

        Unit test to ensure that when hut is 'acquired', the
        'hut.occupant' is updated to the 'Knight' instance
        """
        print("\nCalling test_hut.test_acquire_hut...")
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)


if __name__ == "__main__":
    unittest.main()
