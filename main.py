from player import Player
from house import House
from sesame import Sesame
from location import Location

def main():
    player_name = input("Enter your name: ")
    player_inventory = ["light", "map", "note"]
    player_object = Player(player_name, player_inventory)

    current_location = House(
        "Old cottage",
        "an",
        "Before you, an old house plunges into darkness...",
        "find_key",
        "keys and letter"
    )

    visited_locations = set()

    print(f"Welcome {player_name}! Your adventure begins...\n")

    while True:
        if current_location.name not in visited_locations:
            print(f"\nLocation: {current_location.name}")
            print(current_location)
            print(current_location.additional_property_description())
            visited_locations.add(current_location.name)

        user_input = input("\nEnter a command (use ITEM, take ITEM, describe, inventory, help): ").lower()

        if user_input.startswith("use "):
            item = user_input.split(" ", 1)[-1]
            used = player_object.use_item(item)

            # Reakcja gry na konkretne użycie przedmiotu
            if used and item == "key" and current_location.action == "find_key":
                print("\nYou used the key to unlock the door to the vault.")
                current_location = Sesame(
                    "Treasure Vault",
                    "a",
                    "Treasure lies in the murky depths...",
                    "get_treasure",
                    "ancient manuscripts"
                )

            elif used and item == "treasure" and current_location.action == "get_treasure":
                print("\nYou examined the treasure. It's real! You win!")
                break

        elif user_input.startswith("take "):
            item = user_input.split(" ", 1)[-1]
            player_object.take_item(item, current_location)

        elif user_input == "describe":
            print(current_location.additional_property_description())

        elif user_input == "inventory":
            print("Your inventory:", player_object.get_inventory())

        elif user_input == "help":
            print("Available commands:")
            print("- use ITEM")
            print("- take ITEM")
            print("- describe")
            print("- inventory")
            print("- help")

        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
