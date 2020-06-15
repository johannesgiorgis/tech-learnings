import unittest
from knight import Knight
from hut import Hut


class TestHut(unittest.TestCase):
    """Contains unit tests for the game Attack of the Orcs.

    .. seealso::
       :py:meth: `wargame.hut.Hut.acquire`
    """

    def setUp(self):
        """Overrides the setUp fixture of the superclass.

        This method is called just before the calling each  unit test.
        Here, it creates instances of Knight for use by various unit tests.

        .. seealso:: :py:meth:`TestCase.tearDown`
        """
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
