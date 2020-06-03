"""
Game Utils
"""

import random


def weighted_random_selection(obj1, obj2):
    """Randomly select between two objects based on assigned 'weight'

    .. TODO:: How about creating a utility module for common functionality?
    """
    # weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)] # original
    weighted_list = 3 * [id(obj1)] + 6 * [id(obj2)] + 1 * [None]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1
    elif selection == id(obj2):
        return obj2
    else:
        return None


def print_bold(msg: str, end: str = "\n"):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)
