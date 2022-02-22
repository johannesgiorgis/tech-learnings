from abc import ABCMeta, abstractmethod


class AbstractGameUnit:
    __metaclass__ = ABCMeta

    def __init__(self, name, jump_object=None) -> None:
        self.jump_strategy = None
        self.name = name
        self.set_jump_strategy(jump_object)

    def set_jump_strategy(self, jump_object=None):
        if isinstance(jump_object, JumpStrategy):
            self.jump_strategy = jump_object
        else:
            self.jump_strategy = JumpStrategy()

    def jump(self):
        try:
            self.jump_strategy.jump()
        except AttributeError as err:
            print(
                f"Error: AbstractGameUnit.jump: self.jump_strategy: {self.jump_strategy} \nError details: {err.args}"
            )

    @abstractmethod
    def info(self):
        pass


class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am a great dwarf of the eastern foo mountain!")


class JumpStrategy:
    """Base Class representing a jump strategy (an algorithm)."""

    def jump(self):
        print("--> JumpStrategy.jump: Default jump")


class CanNotJump(JumpStrategy):
    def jump(self):
        print("--> CanNotJump.jump: I can not jump")


class HorseJump(JumpStrategy):
    def jump(self):
        print("--> HorseJump.jump: Jumping my horse.")


class PowerJump(JumpStrategy):
    def jump(self):
        print("--> PowerJump.jump: I can jump 100 feet from the ground!")


if __name__ == "__main__":
    jump_strategy = CanNotJump()
    dwarf = DwarfFighter("Dwarf", jump_strategy)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-" * 56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.set_jump_strategy(PowerJump())
    dwarf.jump()
    print("-" * 56)
