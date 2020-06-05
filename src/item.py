class Item:
    def __init__(self, id, item_name, is_in_room):
        self.id = id
        self.item_name = item_name
        self.is_in_room = is_in_room
    
    def __str__(self):
        return(self.item_name)