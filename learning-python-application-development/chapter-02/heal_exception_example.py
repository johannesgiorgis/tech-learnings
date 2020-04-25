from attackoftheorcs_v1_1 import Knight
from gameuniterror import GameUnitError


if __name__ == "__main__":
    print("Creating a Knight...")
    knight = Knight("Sir Bar")
    # Assume the knight has sustained injuries in the combat
    knight.health_meter = 10
    knight.show_health()
    try:
        # Heal the knight by 100 hit points. This is the `artificial bug'!
        # The Knight can have a maximum of 40 hit points
        knight.heal(heal_by=100, full_healing=False)
        knight.show_health()
    except GameUnitError as e:
        print(e)
        print(e.error_message)

    knight.show_health()
