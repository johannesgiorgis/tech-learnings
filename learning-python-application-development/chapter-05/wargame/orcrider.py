"""
OrcRider Class
"""

from abstractgameunit import AbstractGameUnit


class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider

    .. seealso:: The class `Knight` and the superclass `AbstractGameUnit`
    """

    def __init__(self, name: str = ""):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = "enemy"
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrrr..I am an Orc Rider. Don't mess with me.")
