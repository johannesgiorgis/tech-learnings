"""

Attack of the Orcs v1.0.0
ABC version
-------------------------

While the user wishes to keep playing the game:
    Print the game mission
    Create a huts list
    Randomly place 'enemy' or 'friend' or 'unoccupied' in 5 huts
    Prompt the player to select a hut number
    if enemy :
        while user wishes to continue to attack:
            attack()
            update + show the health
            if enemy health <= 0 -> print "you win"
            if sir foo health <= 0 -> print "you lose"
    else : print "you win"

.. todo ::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.
2. Split the code into smaller modules
3. See the other TODO comments..things you can try fixing as an exercise!
"""

import random
import sys
import textwrap

from abc import ABCMeta, abstractmethod
from typing import List


def weighted_random_selection(obj1, obj2):
    """Randomly select between two objects based on assigned 'weight'

    .. TODO:: How about creating a utility module for common functionality?
    """
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2


def print_bold(msg: str, end: str = "\n"):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


# noinspection DuplicatedCode
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
            self.health_meter += heal_by

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


# noinspection DuplicatedCode
class Knight(AbstractGameUnit):
    """ Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is
    indicated by the attribute `self.unit_type` .
    """

    def __init__(self, name: str = "Sir Foo"):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = "friend"

    def info(self):
        """Print basic information about this character"""
        print("I am a Knight!")

    def acquire_hut(self, hut):
        """Fight the combat (command line) to acquire the hut

        .. TODO::   acquire_hut method can be refactored.
                   Example: Can you use self.enemy instead of calling
                   hut.occupant every time?
        """
        print_bold(f"Entering hut {hut.number}...", end=" ")
        is_enemy = isinstance(hut.occupant, AbstractGameUnit) and hut.occupant.unit_type == "enemy"
        continue_attack = "y"

        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=" ")
            hut.occupant.show_health(bold=True, end=" ")
            while continue_attack:
                continue_attack = input(".......continue attack? (y/n): ")
                if continue_attack == "n":
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break

        else:
            if hut.get_occupant_type() == "unoccupied":
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """Abandon the battle.

        .. seealso:: `self.acquire_hut`
        """
        print_bold("RUNNING AWAY...")
        self.enemy = None


class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider"""

    def __init__(self, name: str = ""):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = "enemy"
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")


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


# noinspection DuplicatedCode
class AttackOfTheOrcs:
    """Main class to play Attack of The Orcs game"""

    def __init__(self):
        self.huts = []
        self.player = None
        self.num_huts = 5  # use this to avoid hard coding

    def get_occupants(self) -> list:
        """Return a list of occupant types for all huts.

        .. TODO::

             Prone to bugs if self.huts is not populated.
             Chapter 2 talks about catching exceptions
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self) -> int:
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        print(f"Current occupants: {self.get_occupants()}")

        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")
            idx = int(user_choice)
            if self.huts[idx - 1].is_acquired:
                print(
                    "You have already acquired this hut. Try again."
                    "<INFO: You can NOT get healed in already acquired hut.>"
                )

            else:
                verifying_choice = False

        return idx

    def _occupy_huts(self):
        """Randomly occupy the huts with one of: friend, enemy or 'None'"""
        for i in range(self.num_huts):
            choice_list = ["enemy", "friend", None]
            computer_choice = random.choice(choice_list)

            if computer_choice == "enemy":
                name = "enemy-" + str(i + 1)
                self.huts.append(Hut(i + 1, OrcRider(name)))

            elif computer_choice == "friend":
                name = "knight-" + str(i + 1)
                self.huts.append(Hut(i + 1, Knight(name)))

            else:
                self.huts.append(Hut(i + 1, computer_choice))

    def play(self):
        """Workhorse method to play the game.

        Controls the high level logic to play the game. This is called from
        the main program to begin the game execution.
        """
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < self.num_huts:
            idx = self._process_user_choice()
            print(f"\tIndex:{idx}")
            self.player.acquire_hut(self.huts[idx - 1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break

            if self.huts[idx - 1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == self.num_huts:
            print_bold("Congratulations! YOU WIN!!!")


if __name__ == "__main__":
    print("Starting game...")
    game = AttackOfTheOrcs()
    game.play()
