"""
Attack of the Orcs v0.0.5
Using Functions
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
            if sir foo helath <= 0 -> print "you lose"
    else : print "you win"
"""

import random
import textwrap

from typing import List


def show_theme_message(width: int):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of The Orcs v0.0.5:")
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


def show_health(health_meter: dict, bold: bool = False):
    """Show the remaining hit points of the player and the enemy"""
    msg = f"Health: Sir Foo: {health_meter['player']}, Enemy: {health_meter['enemy']}"

    if bold:
        print_bold(msg)
    else:
        print(msg)


def reset_health_meter(health_meter: dict):
    """Reset the values of health_meter dict to the original ones"""
    health_meter["player"] = 40
    health_meter["enemy"] = 30


def print_bold(msg: str, end: str = "\n"):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width: int = 72):
    """Print a dotted (rather 'dashed') line"""
    print("-" * width)


def attack(health_meter: dict):
    """The main logic to determine injured unit and amount of injury"""
    hit_list = 4 * ["player"] + 6 * ["enemy"]
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end="")
    show_health(health_meter)


def play_game(health_meter: dict):
    """The main control function for playing the game"""
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx - 1] != "enemy":
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold("ENEMY SIGHTED! ", end="")
        show_health(health_meter, bold=True)
        continue_attack = True

        # Loop that actually runs the combat if user wants to attack
        while continue_attack:
            continue_attack = input(".......continue attack? (y/n): ")
            if continue_attack == "n":
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)

            # Check if either one of the opponents is defeated
            if health_meter["enemy"] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter["player"] <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break


def run_application():
    """Top level control function for running the application."""
    keep_playing = "y"
    width = 72
    health_meter = {}

    show_theme_message(width)
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == "y":
        reset_health_meter(health_meter)
        play_game(health_meter)

        keep_playing = input("\nPlay again? Yes(y)/No(n):")


if __name__ == "__main__":
    run_application()
