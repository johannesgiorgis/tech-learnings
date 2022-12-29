"""
adapter pattern

Example to show a Pythonic way of implementing an adapter pattern.

The example shows how to use Python's language feature, first-class
functions, to implement adapter pattern.
"""


class ElfRider:
    """Class which confirms to our existing interface that client expects.

    The ElfRider represents a game character. It already has defined the methods
    that the client code expects. In this trivial example, it has the 'jump'
    """

    def jump(self):
        """Tell how the unit jumps (dummy method)"""
        print("Inside ElfRider.jump")


class WoodElf:
    """An imaginary third-party class that has an incompatible interface.

    WoodElf represents a game character class that is provided by an imaginary
    'third party' developer. It does not have the 'jump' method that the client
    code expects (incompatible interface). This is used to illustrate how to
    implement adapter pattern.
    """

    def leap(self):
        """leap method is equivalent to the 'jump' method client expects

        The adapter should have a jump method which in turn calls this method.
        """
        print("Inside WoodElf.leap")

    def climb(self):
        """Some other (dummy) method of the class.

        Adapter shouldn't do anything with this method. It should just delegate
        the call from the client to this method.
        """
        print("Inside WoodElf.climb")


class MountainElf:
    """Example class with an incompatible interface than what we expect

    Similar to WoodElf, this is yet another class which has a "spring" method
    which is equivalent to `jump` method of the client interface.
    """

    def spring(self):
        """spring method is equivalent to the 'jump' method client expects"""
        print("Inside MountainElf.spring")


class ForeignUnitAdapter:
    """Generalized adapter class for 'fixing' incompatible interfaces."""

    def __init__(self, adaptee, adaptee_method) -> None:
        self.foreign_unit = adaptee
        self.jump = adaptee_method

    def __getattr__(self, item: str):
        """Handle all the undefined attributes the client code expects."""
        return getattr(self.foreign_unit, item)


if __name__ == "__main__":
    elf = ElfRider()
    elf.jump()

    wood_elf = WoodElf()
    wood_elf_adapter = ForeignUnitAdapter(wood_elf, wood_elf.leap)
    # # Internally the following calls wood_elf.leap()
    wood_elf_adapter.jump()

    # # Internally the following calls __get_attr__
    # # which in turn calls wood_elf.climb()
    wood_elf_adapter.climb()

    mountain_elf = MountainElf()
    mountain_elf_adapter = ForeignUnitAdapter(mountain_elf, mountain_elf.spring)
    mountain_elf_adapter.jump()
