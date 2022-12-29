from typing import Dict


class ElfRider:
    pass


class Knight:
    pass


class OrcRider:
    pass


class DwarfFighter:
    pass


class Fairy:
    pass


class Wizard:
    pass


class ElfLord:
    pass


class OrcFighter:
    pass


class UnitFactory:
    """A factory class to create game units.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiates factory.
    """

    units: Dict = {
        "elfrider": ElfRider,
        "knight": Knight,
        "dwarffighter": DwarfFighter,
        "orcrider": OrcRider,
        "fairy": Fairy,
        "wizard": Wizard,
        "elflord": ElfLord,
        "orcfighter": OrcFighter,
    }

    @classmethod
    def create_unit(cls, unit_type: str):
        """Return an instance of a game unit.

        This is a class method and it uses the class variable unit_dict to
        create and return an instance of a game unit class (e.g. ElfRider(),
        Knight(), Dwarf() and so on.
        """
        key = unit_type.lower()
        return cls.units.get(key)()


class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character"""

    def __init__(self, factory) -> None:
        self.factory = factory

    def recruit(self, unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the factory instance, then pays the price and updates some
        record. The pay_gold and update_record methods are dummy, they just
        print some information.
        """
        unit = self.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        print("GOLD PAID")

    def update_records(self, something):
        print("Some logic (not shown) to update the database of units")


if __name__ == "__main__":
    print("Simple factory example")
    print("-" * 25)
    factory = UnitFactory()
    k = Kingdom(factory)
    elf_unit = k.recruit("ElfRider")
    print(f"Created an instace of : {elf_unit.__class__.__name__}")
