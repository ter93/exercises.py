from location import Player
import location
import house
import sesame

def main():
    #Player
    player_name = input("Enter your name: ")
    player_inventory = ["light"]
    player_object = player.Player(player_name, player_inventory)
    current_location = house.House("Old cottage", "Before you, an old house...", "find key", "keys and letter")
    #Pierwsza lokalizacja
    print("Welcome {}! Your adventure begins in an old house.".format(player_name))
    
    #Opis aktualnej lokalizacji
    while True:
        print(str(current_location))
        
        
    #Komendy gracza
        user_input = input("Enter a command (use item, take item, help, describe): ").lower()
        
        if "use" in user_input:
            item = user_input.split(" ",1)[-1]
            player_object.use_item(item)
        elif "take" in user_input:
            item = user_input.split(" ", 1)[-1]
            player_object.take_item(item)
        elif user_input == "help":
            print("Available commands: use item, take item, help, describe")
        elif user_input == "describe":
            print(current_location.additional_property_description())
        else:
            print("Invalid command. Type 'help' for available commands.")
        
        
        
        if current_location.action == "find_key" and "key" in player_object.get_inventory():
            print("Congratulations! You found the key. Now you can unlock the door.")
            current_location = sesame.Sesame("Treasure Vault", "a", "Treasure lies in the murky depths...", "get_treasure", "ancient manuscripts")
        elif current_location.action == "get_treasure" and "treasure" in player_object.get_inventory():
            print("Congratulations! You succesfully retrieved the treasure. You won the game!")
            break

    
if __name__ == "__main__":
    main()