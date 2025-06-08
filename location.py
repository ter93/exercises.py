class Location:
    def __init__(self, name, article, description, action, available_items=None):
        self.name = name
        self.article = article
        self.description = description
        self.action = action
        self.available_items = available_items if available_items is not None else []

