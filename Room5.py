''' room5.py

This room contains 5 pressure plates. The player must correctly place 5 items
from his inventory onto the 5 pressure plates to balance an Atwood's machine and
proceed to the next stage.

'''
import inventory

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
# the actual values of the machine are stored in an Inventory object of length 5
atw_mcn = inventory.Inventory(max_len=5)

# check the atwood machine
def solve_machine(h=False, f=None):
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
        print r'your flag: ezctf{f=ma}'
    except:
        print 'your solution to the Atwood machine is incorrect'

# the room's environment can hold items
room_items = inventory.Inventory()

# just for testing now
axe = inventory.Item('axe',
                    description='a mighty weapon',
                    weight=3)
sword = inventory.Item('sword',
                    description='an awesome weapon',
                    weight=2)
rail_gun = inventory.Item('rail gun',
                    description='a terrifying weapon',
                    weight=4)
water_pistol = inventory.Item('water pistol',
                    description='a weapon of mass destruction',
                    weight=1)
glasses = inventory.Item('glasses',
                    description='useful apparatus',
                    weight=1)
chinaman = inventory.Item('chinaman',
                    description='ching chong ding dong',
                    weight=0.1)
room_items.pick_item(axe)
room_items.pick_item(sword)
room_items.pick_item(rail_gun)
room_items.pick_item(water_pistol)
room_items.pick_item(glasses)
room_items.pick_item(chinaman)

def show_room_items(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in the room'
        return
    if len(room_items.as_tuple()) < 1:
        print 'the room is empty and void'
        return -1
    print '\nCurrent items visible in room:'
    return room_items.print_inv()

# the room provides a wrapper for inventory functions
def wrap_inv_show(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show your current inventory'
        return
    if len(inv.as_tuple()) < 1:
        print 'your inventory is empty'
        return -1
    print '\nCurrent state of your inventory:'
    return inv.print_inv()

def wrap_inv_drop(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      interactively drop an item from your inventory'
        return
    if len(inv.as_tuple()) < 1:
        err('no items to drop')
        return
    try:
        wrap_inv_show()  # we have already checked for
        index = int(raw_input('room 5 : drop at [inventory] index => '))
        tmp = inv.drop_item(index)
        assert tmp != inventory.NULL
        assert room_items.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to drop)')

def wrap_inv_pick(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      interactively pick up an item in the room'
        return
    if len(room_items.as_tuple()) < 1:
        err('no items to pick up')
        return
    try:
        show_room_items()  # guaranteed to work here, so we don't need to catch
        index = int(raw_input('room 5 : pick up at [room] index => '))
        tmp = room_items.drop_item(index)
        assert tmp != inventory.NULL
        assert inv.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to pick up)')

# greet user and explain predicament
print 'Welcome to room 5!\n'
print ('In this room is a formidable problem: a complex Atwood\'s machine that'
        ' requires five weights to be correctly used to put the system in '
        'equilibrium. Assume that the downward acceleration on this space '
        'station just so happens to be 10 m/s^2.')
print '\nYou can get help with the \'?\' command. Good luck!'

# other functions
def show_machine(h=False, f=None):
    # show the machine state to the user
    if h:
        print 'Help entry for: '+f
        print '      prints the ASCII representation of the riddle'
        print '      also displays current configuration of machine'
        return
    print atw_str
    print 'current machine state: (item #, mass (kg), name)'
    for i in range(1, atw_mcn.max_len+1):
        if i <= len(atw_mcn.as_tuple()):
            tmp = atw_mcn.as_tuple()[i-1]
            print '#%d, %2d, %s' % (i, tmp.weight, tmp.name)
        else:
            print '#%d,  <no item at this index>' % i

def bye(h=False, f=None):
    # this function intentionally does nothing
    # exit is implemented in the user input loop
    if h:
        print 'Help entry for: quit, leave, exit, q, X'  # need many aliases
        print '  * - the exit function'
        print '      leaves the room'
        print '      all aliases of this function are equivalent'

def help(h=False, f=None):
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

def place_items(h=False, f=None):
    # interactively allow the user to place items on the machine
    if h:
        print 'help entry for: '+f
        print '      place items on the Atwood\'s machine'
        print '      interactive loop to submit your solution'
        return
    if len(inv.as_tuple()) < atw_mcn.max_len:
        err('insufficient items to use machine (requires at least five)')
        return
    print 'Verily thou art courageous!'
    print 'Enter the inventory index of the item to place when prompted.'
    print 'Any items you displace from the machine will be dropped in the room.'
    print 'You can enter \'-1\' to keep the machine item at that index.'
    for i in range(1, atw_mcn.max_len+1):
        try:
            print '\nCurrent state of your inventory:'
            inv.print_inv()
            index = int(raw_input('room 5 : mass #'+str(i)+' => '))
            if index == -1:
                continue
            assert index >= 0
            room_items.pick_item(atw_mcn.drop_item(i-1))
            assert atw_mcn.pick_item(inv.drop_item(index)) > 0
        except:
            err('inventory error (invalid item at index)')
            break

# dict exposing funcs to user by mapping user command strings to funcs
usr_dict = {
    'show machine': show_machine,
    'quit': bye, 'leave': bye, 'exit': bye, 'q': bye, 'X': bye,
    '?': help,
    'place items': place_items,
    'show room': show_room_items,
    'show inv': wrap_inv_show,
    'drop item': wrap_inv_drop,
    'pick item': wrap_inv_pick,
    'solve machine': solve_machine
}

# user input prompt
cmd = ''
while cmd not in ['quit', 'leave', 'exit', 'q', 'X']:
    cmd = raw_input('room 5 => ').strip()
    try:
        usr_dict[cmd]()  # see if the command is in the dict
    except:
        try:
            assert cmd[-1] == '?'  # see if command is <func>?
            usr_dict[cmd[:-1]](h=True, f=cmd[:-1])
        except:
            err('unrecognized input. try \'?\' for help')
