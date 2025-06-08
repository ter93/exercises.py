from location import Location

class House(Location):
    def __init__(self, name, article, description, action, additional_property):
        super().__init__(name, article, description, action, available_items=["key", "letter"])
        self.additional_property = additional_property
        
    def __str__(self):
        return("Before you, an old house plunges into darkness, cobwebs dance in the moonlight and a door that has been closed for centuries hides ancient secrets. Find they key to open the way to the forgotten secrets.")
    
    def additional_property_description(self):
        return"It's an old cottage. Available things here are: " + ", ".join(self.available_items)