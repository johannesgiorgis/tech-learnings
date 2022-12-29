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
    """A simple factory to create and return instances of game units"""

    def create_unit(self, unit_type):
        """The work horse method to create and return instances of a game unit"""
        unit = None

        if unit_type == "ElfRider":
            unit = ElfRider()
        elif unit_type == "Knight":
            unit = Knight()
        elif unit_type == "DwarfFighter":
            unit = DwarfFighter()
        elif unit_type == "OrcRider":
            unit = OrcRider()
        elif unit_type == "Fairy":
            unit = Fairy()
        elif unit_type == "Wizard":
            unit = Wizard()
        elif unit_type == "ElfLord":
            unit = ElfLord()
        elif unit_type == "OrcFighter":
            unit = OrcFighter()

        return unit


class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character"""

    factory = UnitFactory

    def recruit(self, unit_type: str):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the 'factory' which is a 'class variable'. Then pays the
        price and updates some record. The pay_gold and update_record methods
        are dummy, they just print some information.
        """
        unit = self.__class__.factory.create_unit(unit_type)
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
    k = Kingdom()
    elf_unit = k.recruit("ElfRider")
    print(f"Created an instace of : {elf_unit.__class__.__name__}")
