''' room5.py

This room contains 5 pressure plates. The player must correctly place 5 items 
from his inventory onto the 5 pressure plates to balance an Atwood's machine and
proceed to the next stage. 

'''
import inventory

# for testing, generate a user inventory
inv = inventory.Inventory()
axe = inventory.Item('axe', 'a mighty weapon', 3)
sword = inventory.Item('sword', 'an awesome weapon', 2)
rail_gun = inventory.Item('rail gun', 'a terrifying weapon', 4)
inv.pick_item(axe)
inv.pick_item(sword)
inv.pick_item(rail_gun)

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
      |   |                     there is a +- 5 N tolerance on
    +---+ |                     the weights
    | 1 | |
    +---+ |                         |   g = 10 m/s^2
         _+_                        v
        / O \ 
        |   |
      +---+ |
      | 2 | |
      +---+ |                    pulleys are assumed to be massless
         ___+___
        /   O   \ 
        |       |
      __+__   +---+
     /  O  \  | 5 |
     |     |  +---+
   +---+ +---+
   | 3 | | 4 |
   +---+ +---+
'''
# dict holds the actual values of the machine:
atw_mcn = {1:inventory.NULL, 2:inventory.NULL, 3:inventory.NULL, 
           4:inventory.NULL, 5:inventory.NULL}

# the room's environment can hold items
room_items = []

# greet user and explain predicament
print 'Welcome to room 5!\n'
print ('In this room is a formidable problem: a complex Atwood\'s machine that'
        ' requires five weights to be correctly used to put the system in '
        'equilibrium. Assume that the downward acceleration on this space '
        'station just so happens to be 10 m/s^2.')

# user functions 
def show_machine():
    # show the machine state to the user
    print atw_str
    print 'current machine state:'
    for i, item in enumerate(atw_mcn):
        print '%d %3d %s' % (i, item.weight, item.name)
def dummy():
    pass  # this function intentionally left blank
def help():
    print 'Available commands:'
    for key in usr_dict:
        print '  '+key
def place_items():
    # interactively allow the user to place items on the machine
    print 'Verily thou art courageous!'
    print 'Enter the inventory index of the item to place when prompted.'
    for i in range(1, 6):
        try:
            index = int(raw_input('room 5 : mass #'+str(i)+' => '))
            assert index >= 0
            atw_mcn[i] = inv.drop_item(index)
            assert atw_mcn[i] != inventory.NULL
        except:
            err('invalid item provided')
            break
    
# dict exposing funcs to user by mapping user command strings to funcs
usr_dict = {
    'show machine': show_machine,
    'quit': dummy, 'leave': dummy, 'exit': dummy, 'q': dummy, 'X': dummy,
    '?': help,
    'place items': place_items
}

# user input prompt
cmd = ''
while cmd not in ['quit', 'leave', 'exit', 'q', 'X']:
    cmd = raw_input('room 5 => ')
    try:
        usr_dict[cmd]()
    except:
        print 'room 5: error: unrecognized input. try \'?\' for help'