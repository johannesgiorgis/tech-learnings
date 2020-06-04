"""
Attack of the Orcs v2.0.0
"""

import random
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from gameutils import print_bold


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
