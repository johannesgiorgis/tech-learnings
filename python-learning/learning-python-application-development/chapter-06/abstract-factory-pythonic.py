"""
abstract factory pythonic

Example to show a Pythonic way of implementing an abstract factory pattern.

The example shows how to use Python's language feature, (classes are first-class
 objects) to implement an abstract factory. It also shows how to use a
 factory WITHOUT instantiating it (using class method and class variables)
"""

# Some dummy classes to represent factory products (not documented)
from math import factorial


class IronJacket:
    pass


class PowerSuit:
    pass


class MithrilArmor:
    pass


class GoldLocket:
    pass


class SuperLocket:
    pass


class MagicLocket:
    pass


class DwarfIronJacket:
    pass


class DwarfPowerSuit:
    pass


class DwarfMithrilArmor:
    pass


class DwarfGoldLocket:
    pass


class DwarfSuperLocket:
    pass


class DwarfMagicLocket:
    pass


class AccessoryFactory:
    """A factory base class to create various game accessories.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiates factory. See the book
    mentioned at the top of this file for detailed explanation.
    """

    # Subclasses specify their own version of these dictionaries
    armor_dict = {
        "ironjacket": IronJacket,
        "powersuit": PowerSuit,
        "mithril": MithrilArmor,
    }
    locket_dict = {
        "goldlocket": GoldLocket,
        "superlocket": SuperLocket,
        "magiclocket": MagicLocket,
    }

    @classmethod
    def create_armor(cls, armor_type):
        """Return an instance of an armor accessory

        This is a class method and it uses the class variable armor_dict to
        create and return an instance of an armor accessory (e.g. IronJacket(),
        PowerSuit() etc.
        """
        return cls.armor_dict.get(armor_type)()

    @classmethod
    def create_locket(cls, locket_type):
        """Return an instance of a locket accessory

        This is a class method and it uses the class variable locket_dict to
        create and return an instance of an armor accessory (e.g. GoldLocket(),
        DwarfGoldLocket() etc.
        """
        return cls.locket_dict.get(locket_type)()


class DwarfAccessoryFactory(AccessoryFactory):
    """A factory for creating accessories customized for Dwarf game character.

    Redefines the class variables, armor_dict and locket_dict.
    """

    # Redefine the accessory dictionaries
    armor_dict = {
        "ironjacket": DwarfIronJacket,
        "powersuit": DwarfPowerSuit,
        "mithril": DwarfMithrilArmor,
    }
    locket_dict = {
        "goldlocket": DwarfGoldLocket,
        "superlocket": DwarfSuperLocket,
        "magiclocket": DwarfMagicLocket,
    }


class Kingdom:

    # Define which factory class you want to use. (Redefined in subclasses)
    factory = AccessoryFactory

    def buy_accessories(self, armor_type, locket_type):
        """ """
        armor = self.__class__.factory.create_armor(armor_type)
        locket = self.__class__.factory.create_locket(locket_type)
        accessories = [armor, locket]
        self.pay_gold(accessories)
        self.update_records(accessories)
        self.print_info(armor, locket)

    def pay_gold(self, accessories):
        """Pay gold for the new accessories (dummy method)."""
        print("GOLD PAID")

    def update_records(self, accessories):
        """Update some record to reflect new accessories (dummy method)."""
        print("Updated database of accessories")

    def print_info(self, armor, locket):
        """Print some information on the newly created accessories"""
        print("Done with shopping in       :", self.__class__.__name__)
        print("  concrete class for armor  :", armor.__class__.__name__)
        print("  concrete class for locket :", locket.__class__.__name__)


class DwarfKingdom(Kingdom):
    """Class that represents imaginary Kingdom of The Great Dwargs."""

    # Define which factory you want to use for this kingdom.
    factory = DwarfAccessoryFactory


if __name__ == "__main__":
    print("Buying accessories in default Kingdom...")
    k = Kingdom()
    k.buy_accessories("ironjacket", "goldlocket")
    print("-" * 56)
    print("Buying accessories in DwarfKingdom...")
    dwarf_kingdom = DwarfKingdom()
    dwarf_kingdom.buy_accessories("ironjacket", "goldlocket")
