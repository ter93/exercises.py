class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        
    def get_inventory(self):
        return self.inventory
    
    def use_item(self, item):
        if item in self.inventory:
            print(f"You used {item}.")
            self.inventory.remove(item)
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
        
    def take_item(self, item):
        print(f"You took {item}.")
        self.inventory.append(item)
        return True