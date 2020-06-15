"""
Abstract Game Unit
"""

import random
from abc import ABCMeta, abstractmethod

from gameutils import print_bold, weighted_random_selection
from gameuniterror import GameUnitError


class AbstractGameUnit(metaclass=ABCMeta):
    """Abstract class to represent a game character (or a 'unit')

    :ivar max_hp: Maximum 'hit points' or 'health points' for the unit
                 This is set by the subclasses.
    :ivar health_meter: Keeps track of the current health of the unit
    :ivar name: Name of the character (set by subclasses)
    :ivar enemy: Present enemy of this unit, At any time, it can have only
                one enemy.
    :ivar unit_type: Tells if this is a 'friend' or an 'enemy'

    :param name: Accept the name of this game character

    .. seealso:: Classes :py:class:`Knight` and :py:class:`OrcRider`
    """

    def __init__(self, name: str = ""):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Print information about this game unit.

        Abstract method. See subclasses for implementation.
        """
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of injury

        This method handles combat between the player (Knight instance) and
        the given enemy (at the moment OrcRider instance). In the combat,
        one of the units could get injured or both will escape unhurt. The
        method reduces the 'health' of the injured unit by a randomly selected
        amount.

        :param enemy: The enemy to be attacked (instance of subclass of
                      AbstractGameUnit

        .. seealso:: :py:meth:`Knight.acquire_hut`

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end="")
        self.show_health(end="  ")
        enemy.show_health(end="  ")

    def heal(self, heal_by: int = 2, full_healing: bool = True):
        """Heal the unit replenishing all the hit points

        This method is called when you (the player) enters a friendly hut.

        :param heal_by: `health_meter` will be updated by this amount if
                        full healing is not requested/
        :param full_healing: Fully heal this unit by resetting the `heal_meter`
                        to the maximum limit.

        .. seealso:: :py:meth:`Knight.acquire_hut`

        .. todo:: Add exception handling code , assert heal_by amount is within
                  limits! (exercise)
        """
        # Do not continue if the game unit already has full health
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            # TODO: Do you see a bug here? it can exceed max hit points!
            # assert (self.health_meter + heal_by <= self.max_hp)
            self.health_meter += heal_by

        # raise a custom exception
        if self.health_meter > self.max_hp:
            raise GameUnitError("health_meter > max_hp!", 101)

        print_bold("You are HEALED!", end=" ")
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold: bool = False, end: str = "\n"):
        """Show the remaining hit points of the player and the enemy

        The arguments to this method are mainly to customize the message display
        style.

        :param bold: Flag to indicate whether information should be printed in
                     bold style or normal style.
        :param end: Specify how the message should end i.e whether a new line
                    character should be appended in the end or you just want to
                    add a space or a tab (for message continuation)
        """
        # TODO: what if there is no enemy?
        msg = f"Health: {self.name}: {self.health_meter}"

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
