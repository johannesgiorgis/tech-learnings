"""
Abstract Game Unit
"""

import random
from abc import ABCMeta, abstractmethod

from gameutils import print_bold, weighted_random_selection
from gameuniterror import GameUnitError


class AbstractGameUnit(metaclass=ABCMeta):
    """An Abstract base for creating various game characters"""

    def __init__(self, name: str = ""):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Information on the unit (MUST be overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of injury

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end="")
        self.show_health(end="  ")
        enemy.show_health(end="  ")

    def heal(self, heal_by: int = 2, full_healing: bool = True):
        """Heal the unit replenishing all the hit points"""
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
        """Show the remaining hit points of the player and the enemy"""
        # TODO: what if there is no enemy?
        msg = f"Health: {self.name}: {self.health_meter}"

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
