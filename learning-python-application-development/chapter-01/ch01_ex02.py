"""
Attack of the Orcs v0.0.5
Using Functions
-------------------------

While the user wishes to keep playing the game:
    Print the game mission
    Create a huts list
    Randomly place 'enemy' or 'friend' or 'unoccupied' in 5 huts
    Prompt the player to select a hut number
    if enemy : print "you lose"
    else : print "you win"
"""

import random
import textwrap

from typing import List


def show_theme_message(width: int):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of the Orcs v0.0.1:")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter.."
    )

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()


def reveal_occupants(idx: int, huts: List[str]):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = f"<{i+1}:{huts[i]}>"
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()


def occupy_huts() -> List[str]:
    """Randomly populate the `huts` list with occupants"""
    huts: List[str] = []
    occupants = ["enemy", "friend", "unoccupied"]
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice() -> int:
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx


def enter_hut(idx: int, huts: List[str]):
    """Enter the hut"""
    print_bold(f"Entering hut {idx}... ", end=" ")

    # Determine and announce the winner
    if huts[idx + 1] == "enemy":
        print_bold("YOU LOSE :( Better luck next time!")
    else:
        print_bold("Congratulations! YOU WIN!!!")
    print_dotted_line()


def print_bold(msg: str, end: str = "\n"):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width: int = 72):
    """Print a dotted (rather 'dashed') line"""
    print("-" * width)


def run_application():
    """Top level control function for running the application."""
    keep_playing = "y"
    width = 72
    # dotted_line = "-" * width

    show_theme_message(width)
    show_game_mission()

    while keep_playing == "y":
        huts = occupy_huts()
        idx = process_user_choice()
        reveal_occupants(idx, huts)

        enter_hut(idx, huts)
        keep_playing = input("Play again? Yes(y)/No(n):")


if __name__ == "__main__":
    run_application()
