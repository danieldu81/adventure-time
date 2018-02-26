''' Room5.py

This room contains 5 pressure plates. The player must correctly place 5 items
from his inventory onto the 5 pressure plates to balance an Atwood's machine
and proceed to the next stage.

'''
import inventory

#################
# ROOM METADATA #
#################

name = 'room 5'
win = False  # if the `win' flag is set, main.py is notified

# for testing, generate a user inventory
inv = inventory.Inventory()

# log error --- standardize this later
def err(text):
    print 'room 5 : error : %s' % text

# the atwood machine to be solved:
atw_str = r'''
//////////////////////////////////////////////////////////////////////
========+=============================================================
        |
       _+_
      / O \
      |   |
    +---+ |                     downward acceleration on this
    | 1 | |                     spaceship:
    +---+ |                         |   g = 10 m/s^2
         _+_                        v
        / O \
        |   |
      +---+ |
      | 2 | |
      +---+ |                    pulleys are assumed to be massless
         ___+___                 strings are also massless
        /   O   \                basically don't overthink it
        |       |
      __+__   +---+
     /  O  \  | 5 |
     |     |  +---+
   +---+ +---+
   | 3 | | 4 |
   +---+ +---+
'''

##############
# SETUP ROOM #
##############

# the actual values of the machine are stored in an Inventory object
atw_mcn = inventory.Inventory(max_len=5)

# initialize Atwood machine with dummy masses
for i in range(1, atw_mcn.max_len+1):
    n = str(i)+'_kg'
    atw_mcn.pick_item(inventory.Item(n,
                                     description='a '+n+' mass',
                                     weight=i))

# the room's environment can hold unlimited items
room_items = inventory.Inventory()

# initialize room items
axe = inventory.Item('axe',
                    description='a mighty weapon',
                    weight=4)
sword = inventory.Item('sword',
                    description='an awesome weapon',
                    weight=2)
rail_gun = inventory.Item('rail_gun',
                    description='a terrifying weapon',
                    weight=8)
water_pistol = inventory.Item('water_pistol',
                    description='a weapon of mass destruction',
                    weight=1)
glasses = inventory.Item('glasses',
                    description='useful apparatus',
                    weight=1)
crowbar = inventory.Item('crowbar',
                    description='brute force is never the solution',
                    weight=2)
room_items.pick_item(axe)
room_items.pick_item(sword)
room_items.pick_item(rail_gun)
room_items.pick_item(water_pistol)
room_items.pick_item(glasses)
room_items.pick_item(crowbar)


##################
# USER FUNCTIONS #
##################

def solve_machine(args, h=False, f=None):
    # checks if a given solution to the Atwood's machine is correct
    if h:
        print 'Help entry for: '+f
        print '      checks if a solution to the Atwood machine is valid'
        print '  related:'
        print '      you can use \'show machine\' to view the current masses'
        return
    w = [item.weight for item in atw_mcn.as_tuple()]
    if len(w) < atw_mcn.max_len:
        err('some machine masses are empty')
        return
    try:
        t_weight = w[2]
        assert t_weight == w[3]
        t_weight += w[3]
        assert t_weight == w[4]
        t_weight += w[4]
        assert t_weight == w[1]
        t_weight += w[1]
        assert t_weight == w[0]
        print 'your solution to the Atwood machine is correct'
        print 'you may proceed to the next room in triumph'
        global win
        win = True
    except:
        print 'your solution to the Atwood machine is incorrect'

def wrap_inv_drop(args, h=False, f=None):
    # drops items from the inventory into the room
    if h:
        print 'Help entry for: '+f
        print '      interactively drop an item from your inventory'
        print ('      if you supply a list of item NAMES, you can skip the '
               'interactive part')
        return
    if len(inv.as_tuple()) < 1:
        err('no items to drop')
        return
    if len(args) > 0:
        for i in args:
            if i not in [item.name for item in inv.as_tuple()]:
                err('item \''+i+'\' not found in user inventory')
                continue
            index = [item.name for item in inv.as_tuple()].index(i)
            try:
                tmp = inv.drop_item(index)
                assert tmp != inventory.NULL
                assert room_items.pick_item(tmp) > 0
                print 'dropped inventory item \'%s\'' % i
            except:
                err('could not drop item \''+i+'\'')
        return
    try:
        show_inv(['inv'])  # we have already checked for errors
        index = int(raw_input('room 5 : drop at [inventory] index => '))
        tmp = inv.drop_item(index)
        assert tmp != inventory.NULL
        assert room_items.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to drop)')

def wrap_inv_pick(args, h=False, f=None):
    # picks up items from the room into the inventory
    if h:
        print 'Help entry for: '+f
        print '      interactively pick up an item in the room'
        print '      alternatively, you can supply a list of item NAMES'
        return
    if len(room_items.as_tuple()) < 1:
        err('no items to pick up')
        return
    if len(inv.as_tuple()) + len(args) > inv.max_len and inv.max_len > 0:
        err('not enough space in inventory')
        print len(inv.as_tuple())
        print len(args)
        return
    if len(args) > 0:
        for i in args:
            if i not in [item.name for item in room_items.as_tuple()]:
                err('item \''+i+'\' not found in the room')
                continue
            index = [item.name for item in room_items.as_tuple()].index(i)
            tmp = room_items.drop_item(index)
            try:
                assert tmp != inventory.NULL
                assert inv.pick_item(tmp) > 0
                print 'picked up item \'%s\' into user inventory' % i
            except:
                err('unable to pick up item \''+i+'\'')
                room_items.pick_item(tmp)  # put dropped item back in room
        return
    try:
        show_inv(['room'])  # guaranteed to work here, so no need to catch
        index = int(raw_input('room 5 : pick up at [room] index => '))
        tmp = room_items.drop_item(index)
        assert tmp != inventory.NULL
        assert inv.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to pick up)')

def show_inv(args, h=False, f=None):
    # displays the requested inventory
    if h:
        print 'Help entry for: '+f
        print '      display function'
        print '      can be invoked in three ways:'
        print '        show room     # shows items in the room'
        print '        show inv      # shows current state of user inventory'
        print ('        show machine  # shows ASCII representation and current'
               ' state of Atwood\'s machine')
        return
    if len(args) != 1:
        err('show takes exactly one argument')
        return

    if args[0] == 'room':
        if len(room_items.as_tuple()) < 1:
            print 'the room is empty and void'
            return -1
        print '\nCurrent items visible in room:'
        return room_items.print_inv()

    elif args[0] == 'inv':
        if len(inv.as_tuple()) < 1:
            print 'your inventory is empty'
            return -1
        print '\nCurrent state of your inventory:'
        return inv.print_inv()

    elif args[0] == 'machine':
        print atw_str
        print 'current machine state: (item #, mass (kg), name)'
        for i in range(1, atw_mcn.max_len+1):
            if i <= len(atw_mcn.as_tuple()):
                tmp = atw_mcn.as_tuple()[i-1]
                print '#%d, %2d, %s' % (i, tmp.weight, tmp.name)
            else:
                print '#%d,  <no item at this index>' % i

    else:
        err('show : argument not recognized')

def bye(args, h=False, f=None):
    # this function intentionally does nothing
    # exit is implemented in the user input loop
    if h:
        print 'Help entry for: quit, leave, exit, q, X'  # need many aliases
        print '  * - the exit function'
        print '      leaves the room'
        print '      all aliases of this function are equivalent'

def help(args, h=False, f=None):
    # user help function
    if h:
        print 'Help entry for: '+f
        print '  ? - the help function'
        print '      can be invoked alone to display available commands'
        print '      can be invoked after a function for contextual help'
        print '  examples'
        print '      ?'
        print '      show machine?'
        return
    print 'Available commands:'
    for key in usr_dict:
        print '  '+key
    print 'you can get contextual help with <cmd>?'

def place_items(args, h=False, f=None):
    # allows the user to place items on the machine
    if h:
        print 'help entry for: '+f
        print '      place items on the Atwood\'s machine'
        print '      you must supply exactly one argument for each weight'
        print '      to leave a mass as is, use \'-\''
        print '  example:'
        print '      place axe sword - - rail_gun'
        return

    if len(args) != atw_mcn.max_len:
        err('must supply exactly '+str(atw_mcn.max_len)+' arguments')

    if len(args) == atw_mcn.max_len:
        for i in args:
            if i not in [item.name for item in inv.as_tuple()] and i != '-':
                err('item \''+i+'\' not found in user inventory')
                return  # I just realized putting all these returns is
                        # basically just putting GOTOs everywhere...

        # first clear out the machine
        atw_items = []
        for _ in range(0, atw_mcn.max_len):
            atw_items += [atw_mcn.drop_item(0)]

        # loop through items and place them on the machine in order provided
        for i, thing in enumerate(args):
            if thing == '-':
                atw_mcn.pick_item(atw_items[i])
                continue
            # `i' is guaranteed to exist in inventory now
            index = [item.name for item in inv.as_tuple()].index(thing)
            try:
                assert index >= 0 and index < len(inv.as_tuple())
                tmp = inv.drop_item(index)
                assert tmp != inventory.NULL
                room_items.pick_item(atw_items[i])
                assert atw_mcn.pick_item(tmp) > 0
            except:
                # if a dropping error occurs, replace the machine item with
                # the item originally there, so the index is not messed up
                err('inventory error : invalid item at index')
                atw_mcn.pick_item(atw_items[i])
        return
# dict exposing funcs to user by mapping user command strings to funcs
usr_dict = {
    'quit': bye, 'leave': bye, 'exit': bye, 'q': bye, 'X': bye,
    '?': help,
    'place': place_items,
    'show': show_inv,
    'drop': wrap_inv_drop,
    'pick': wrap_inv_pick,
    'solve': solve_machine
}


######################
# GAMEPLAY MECHANICS #
######################

def play(global_inv):
    # set file inventory to be global inventory
    # this is like the worst naming ever, but oh well
    global inv
    inv = global_inv

    # greet user and explain predicament
    print '\n'+'='*80
    print 'Welcome to room 5!\n'
    print ('In this room is a formidable problem: a complex Atwood\'s machine '
        'that requires five weights to be correctly used to put the system '
        'in equilibrium. Assume that the downward acceleration on this space '
        'station just so happens to be 10 m/s^2.')
    print '\nYou can get help with the \'?\' command. Good luck!'
    print '='*80+'\n'

    # user input prompt
    cmd = ''
    while cmd not in ['quit', 'leave', 'exit', 'q', 'X']:
        raw_in = raw_input('room 5 => ').strip().split(' ')
        cmd = raw_in[0]
        try:
            usr_dict[cmd](raw_in[1:])  # see if the command is in the dict
        except:
            try:
                assert cmd[-1] == '?'  # see if command is <func>?
                usr_dict[cmd[:-1]](raw_in[1:], h=True, f=cmd[:-1])
            except:
                err('unrecognized input. try \'?\' for help')
    return win

if __name__ == '__main__':
    play(inventory.Inventory())
