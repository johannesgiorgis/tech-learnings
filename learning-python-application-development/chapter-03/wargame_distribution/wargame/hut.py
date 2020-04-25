"""
Hut Class
"""

from gameutils import print_bold


class Hut:
    """Class to create hut object(s) in the game Attack of the Orcs"""

    def __init__(self, number: int, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """Update the occupant of this hut"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold(f"GOOD JOB! Hut {self.number} acquired")

    def get_occupant_type(self) -> str:
        """Return a string giving info on the hut occupant"""
        if self.is_acquired:
            occupant_type = "ACQUIRED"
        elif self.occupant is None:
            occupant_type = "unoccupied"
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type
