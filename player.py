class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        
    def get_inventory(self):
        return self.inventory
    
    def use_item(self, item):
        if item in self.inventory:
            if item == "map":
                print("You look at the map. A hidden room is marked behind the bookshelf.")
            elif item == "note":
                print("The note says: 'The key lies beneath the mat by the door.'")
            elif item == "key":
                print("You try the key on the old lock... it clicks open.")
            elif item == "light":
                print("You turn on the light. Shadows flee from the corners.")
            else:
                print(f"You used {item}.")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
        
    def take_item(self, item, current_location):
        if item in current_location.available_items:
            print(f"You took {item}.")
            self.inventory.append(item)
            current_location.available_items.remove(item)
            return True
        else:
            print(f"There is no {item} here.")
            return False
