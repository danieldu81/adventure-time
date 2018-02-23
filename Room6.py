''' Room6.py

This room contains an AI named JEFF who seeks to kill the user.

'''

import inventory

# room metadata
name = 'room 6'
win = False

# user inventory object
inv = inventory.Inventory()

def err(text):
    print 'room 6 : error : %s' % text

def try_item(args):
    # if an argument was given, try that item:
    if len(args) > 0:
        pass
    
    # otherwise, allow the user to interactively select an item
    else:
        print 'Current inventory state:\n'
        inv.print_inv()

def bye(args):
    pass  # purposely left empty---exit is handled in loop

usr_dict = {
    'try': try_item,
    'q': bye
}

def play(global_inv):
    global inv
    inv = global_inv
    
    # greet player
    print 'Welcome to room 6!\n'
    print ('This room houses the artificial intelligence known as the '
            'Janitorial Entity for Fighting Foreigners (JEFF). As the name '
            'might suggest, JEFF\'s primary purpose is to protect the ship '
            'from invaders. However, due to your accelerated awakening, it '
            'believe you to be an intruder! Please exterminate JEFF before it '
            'exterminates you.\n')
    
    # give a special message if the user has the crowbar
    if 'crowbar' in [item.name for item in inv.as_tuple()]:
        print 'I see you have a crowbar...'
        print 'Of course, brute force is NEVER the right solution...NEVER...'
    
    # user input loop
    cmd = ''
    while cmd not in ['q', 'quit']:
        raw_in = raw_input('room 6 => ').strip().split(' ')
        cmd = raw_in[0]
        try:
            usr_dict[cmd](raw_in[1:])
        except:
            err('unrecognized command')
        

if __name__ == '__main__':
    play(inventory.Inventory())