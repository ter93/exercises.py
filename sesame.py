from location import Location

class Sesame(Location):
    def __init__(self, name, article, description, action, additional_property):
        super().__init__(name, article, description, action, available_items=["treasure", "manuscript"])
        self.additional_property = additional_property
        
    def __str__(self):
        return ("Treasure lies in the murky depths, hidden beneath the layers of time. Glowing jewels spread a glow on walls steeped in mysterious heritage. It's a place where stories from bygone eras circulate. Find your way through the hidden treasures and discover the prize that lies at the heart of this mysterious vault.")
    
    def additional_property_description(self):
        return "This place hides many ancient manuscripts. You see: " + ", ".join(self.available_items)