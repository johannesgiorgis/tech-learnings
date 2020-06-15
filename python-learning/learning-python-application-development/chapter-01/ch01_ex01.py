"""
Attack of the Orcs v0.0.1
Simple Script
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

if __name__ == "__main__":
    keep_playing = "y"
    occupants = ["enemy", "friend", "unoccupied"]
    width = 72
    dotted_line = "-" * width
    print(dotted_line)
    print("\033[1m" + "Attack of the Orcs v0.0.1:" + "\033[0m")
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
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0m")
    print("Be careful as there are enemies lurking around!")
    print(dotted_line)
    # print("\033[1m" + " " + "\033[0m")
    # print("\033[1m" + " " + "\033[0m")

    while keep_playing == "y":
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the huts list
        while len(huts) < 5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user to select a hut
        msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
        user_choice = input("\n" + msg)
        idx = int(user_choice)

        # Print the occupant info
        print("Revealing the occupants...")
        msg = ""
        for i in range(len(huts)):
            occupant_info = f"<{i+1}:{huts[i]}>"
            if i + 1 == idx:
                occupant_info = "\033[1m" + occupant_info + "\033[0m"
            msg += occupant_info + " "
        print("\t" + msg)
        print(dotted_line)
        print("\033[1m" + f"Entering hut {idx}... " + "\033[0m", end=" ")

        # Determine and announce the winner
        if huts[idx + 1] == "enemy":
            print("\033[1m" + "YOU LOSE :( Better luck next time!" + "\033[0m")
        else:
            print("\033[1m" + "Congratulations! YOU WIN!!!" + "\033[0m")
        print(dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n):")

