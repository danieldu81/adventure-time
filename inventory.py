# an entry in the user inventory
class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

# the NULL object is used for raising errors?
NULL = Item('NULL', 'an error occurred', -1)

# the user inventory
class Inventory:
    def __init__(self):
        self.items = []
    def pick_item(self, item):
        # accepts the item object to append
        self.items += [item]
    def drop_item(self, index):
        # returns the item removed
        # if no object was removed, return the NULL object
        try:
            assert index >= 0 and index < len(self.items)
            tmp = self.items[int(index)]
            del self.items[int(index)]
            return tmp
        except:
            return NULL
    def list_items(self):
        return [i for i in self.items]