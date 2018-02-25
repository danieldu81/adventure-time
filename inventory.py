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
    def __init__(self, max_len=-1, max_weight=-1):
        # constuctor initializes an empty list
        # optionally, if max_len or max_weight are positive, they form upper
        # bounds on the size of the inventory
        self.items = []
        self.max_len = max_len
        self.max_weight = max_weight

    def pick_item(self, item):
        # accepts the Item object to append, but we cannot append invalid Items
        # return 1 on success and -1 on failure
        if self.max_len > 0 and len(self.items) >= self.max_len:
            # reject if max_len is set and we have reached it
            return -1
        if (self.max_weight > 0 and
            sum([item.weight for item in self.items]) >= self.max_weight):
            # reject if max_weight is set and we have reached it
            return -1
        if item.weight <= 0:
            # reject if NULL or invalid weight
            return -1
        if len(item.name) > Item.MAX_N_LEN:
            # reject if name too long
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
        if self.max_len > 0:
            print 'MAX INVENTORY LENGTH: %d' % self.max_len
        if self.max_weight > 0:
            print 'MAX TOTAL WEIGHT: %d' % self.max_weight
        print 'index :             name : weight : ( description )'
        print '==================================='
        for i, item in enumerate(self.items):
            tmp = (i,) + item.as_tuple()
            print '%5d : %16s : %6d : ( %s )' % tmp
        return len(self.items)
