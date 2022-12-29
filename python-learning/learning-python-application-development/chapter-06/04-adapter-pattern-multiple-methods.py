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


class FooElf:
    """An imaginary third-party class that has an incompatible interface.

     FooElf represents a game character class that is provided by an imaginary
     'third party' developer. It does not have the 'jump' and 'attack' methods
     that the client code expects (incompatible interface).

     This is used to illustrate one way of implementing the adapter pattern
     when you have multiple methods that have incompatible names

    .. seealso:: `ForeignUnitAdapter`
    """

    def leap(self):
        """leap method is equivalent to the 'jump' method client expects

        The adapter should have a jump method which in turn calls this.
        """
        print("FooElf.leap")

    def hit(self):
        """hit method is equivalent to the 'attack' method client expects

        The adapter should have an attack method which in turn calls this.
        """
        print("FooElf.hit")


class ForeignUnitAdapter:
    """Generalized adapter class for 'fixing' incompatible interfaces."""

    def __init__(self, adaptee) -> None:
        self.foreign_unit = adaptee

    def __getattr__(self, item: str):
        """Handle all the undefined attributes the client code expects."""
        return getattr(self.foreign_unit, item)

    def set_adapter(self, name, adaptee_method):
        """Convenience method to set a new attribute to this class
        Example: setattr(self, 'jump', foo_elf.leap) is equivalent to
        saying:
            self.jump = foo_elf.jump
        """
        setattr(self, name, adaptee_method)


if __name__ == "__main__":
    foo_elf = FooElf()
    foo_elf_adapter = ForeignUnitAdapter(foo_elf)

    foo_elf_adapter.set_adapter("jump", foo_elf.leap)
    foo_elf_adapter.set_adapter("attack", foo_elf.hit)

    foo_elf_adapter.jump()
    foo_elf_adapter.attack()
