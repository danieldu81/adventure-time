# an entry in the user inventory
class Item:
    # class-wide restrictions on inventory items
    MAX_N_LEN = 16
    
    def __init__(self, name, description='an item', weight=1):
        # constructor populates data fields
        self.name = name
        self.description = description
        self.weight = weight
        
    def as_tuple(self):
        # returns this item as a tuple
        return (self.name, self.weight, self.description)

# the NULL object is used for raising errors?
NULL = Item('NULL', 'empty', -1)

# the user inventory
class Inventory:
    def __init__(self):
        # constuctor initializes an empty list
        self.items = []
        
    def pick_item(self, item):
        # accepts the item object to append, but we cannot append NULL
        # return 1 on success and -1 on failure
        if item.weight <= 0:
            return -1
        self.items += [item]
        return 1
        
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
            
    def as_tuple(self):
        # returns the inventory items as a tuple
        return tuple(self.items)
        
    def print_inv(self):
        # prints inventory 
        # returns the number of items printed
        print 'index :             name : weight : ( description )'
        print '==================================='
        for i, item in enumerate(self.items):
            tmp = (i,) + item.as_tuple()
            print '%5d : %16s : %6d : ( %s )' % tmp
        return len(self.items)