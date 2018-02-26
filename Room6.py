''' Room6.py

This room contains an AI named JEFF who seeks to kill the user.

'''

import inventory
import hashlib

# room metadata
name = 'room 6'
win = False

# user and room inventory objects
inv = inventory.Inventory()
room_items = inventory.Inventory()

# init the room with some potentially useful items
room_items.pick_item(inventory.Item('apple',
                             description='keeps doctors away', weight=1))
room_items.pick_item(inventory.Item('banana',
                             description='monkey like', weight=1))
room_items.pick_item(inventory.Item('orange',
                             description='not to be compared to apple',
                             weight=1))
room_items.pick_item(inventory.Item('chestnut',
                             description='a solid road in Holmdel, NJ',
                             weight=1))
room_items.pick_item(inventory.Item('penguin',
                             description='tux, is that you?', weight=3))

# sha256 hash of the 'special object' name, so the casual user looking at the
# source code still doesn't know what the item is
item_hash = 'be0c96b17d8481575fa72aee2fe75c42f269bfb893012fcaffb561583ba07827'

def err(text):
    # format error messages consistently
    print 'room 6 : error : %s' % text

def print_help(name):
    # print man pages consistently
    print 'Help entry for function: %s' % name

def help_func(args, helpmode=False, alias=None):
    # shows help text to user
    # can be global or contextual
    if helpmode:
        print_help(alias)
        print '  the help function'
        print '  can be invoked alone for a list of available commands'
        print '  can also be invoked contextually for more precise help'
        print '  examples'
        print '    try?  # prints the help entry for the <try> function'
        print '    ??  # prints the help entry for the <?> function'
        print '    ?  # provides a list of available commands'
        return
    print 'available commands:'
    for i in usr_dict:
        print '  %s' % i
    print 'for contextual help, use <func>?'

def try_item(args, helpmode=False, alias=None):
    # attempts to use an item(s) on JEFF
    if helpmode:
        print_help(alias)
        print '  use an item in your inventory'
        print '  attempt to make use of an item to destroy JEFF'
        print '  when you use an item, one of three things can happen:'
        print '    1. the item is invalid and an error occurs'
        print '    2. the item cannot destroy JEFF, and you lose it forever'
        print '    3. the item successfully destroys JEFF but cannot be reused'
        print '  this function can be invoked either with a list of items'
        print '  or interactively'
        print '  examples:'
        print '    %s banana starfruit  # try the banana and starfruit' % alias
        print '    %s  # interactively try an item from your inventory' % alias
        return

    def use(i):
        print 'trying to use the \'%s\' to combat JEFF...' % i
        if i not in [item.name for item in inv.as_tuple()]:
            print ('Ah! Surely thou art not a liar? O deceitful player, '
                   'use not that which belongeth not unto thee, lest '
                   'thou invoke the wrath of JEFF upon thyself! Heed this '
                   'warning, else live not to regret it.')
        else:
            index = [item.name for item in inv.as_tuple()].index(i)
            inv.drop_item(index)
            if hashlib.sha256(i).hexdigest() == item_hash:
                print 'Success! You have destroyed JEFF with your %s!' % i
                print 'You can now leave this room and proceed on your quest.'
                global win
                win = True
                return
            else:
                print ('Alas! Vainly hast thou ventur\'d! For three days '
                       'and three nights thou did\'st strive, yet on the '
                       'fourth day JEFF prevailed mightily. Behold! Thine '
                       '\'%s\' hath been torn asunder and cannot be used '
                       'again! If thou be brave, make thee another '
                       'attempt.') % i

    # if an argument(s) was given, try that item:
    if len(args) > 0:
        for i in args:
            use(i)

    # otherwise, allow the user to interactively select an item
    else:
        try:
            print 'Current inventory state:\n'
            inv.print_inv()
            index = int(raw_input('room 6 : use item at index => '))
            assert index >= 0 and index < len(inv.as_tuple())
            use(inv.as_tuple()[index].name)
        except:
            err('try : invalid item to try on JEFF')

def show_inv(args, helpmode=False, alias=None):
    # show either user inventory or room items
    if helpmode:
        print_help(alias)
        print '  the display function'
        print '  shows the current status of a collection of objects'
        print '  there are two valid arguments: <room> and <inv>'
        return
    if len(args) != 1:
        err('command `show\' takes exactly one argument')
        return
    global inv
    global room_items
    try:
        inventory = {'inv': inv, 'room': room_items}[args[0]]
        if len(inventory.as_tuple()) == 0:
            print '[empty]'
        else:
            inventory.print_inv()
    except:
        err('show : unrecognized argument')

def pick_item(args, helpmode=False, alias=None):
    # picks up an item from room to user inventory
    if helpmode:
        print_help(alias)
        print '  the pick up function'
        print '  picks up an item from the room into the user inventory'
        print '  can be invoked with a list of item(s) to pick up'
        print '  can also be invoked interactively by supplying no arguments'
        print '  examples:'
        print '    pick kiwi  # pick up the <kiwi> item'
        print '    pick  # interactively select an item to pick up'
        return
    if len(inv.as_tuple()) + len(args) > inv.max_len:
        err('not enough space in inventory')
        return
    def pick(i):
        print 'attempting to pick up item \'%s\'' % i
        if i not in [item.name for item in room_items.as_tuple()]:
            err('pick : item \''+i+'\' not found in room')
        else:
            index = [item.name for item in room_items.as_tuple()].index(i)
            tmp = room_items.drop_item(index)
            try:
                assert tmp != inventory.NULL
                assert inv.pick_item(tmp) > 0
                print 'successfully picked up item \'%s\'' % i
            except:
                err('inventory error : cannot pick specified item')
                # if we fail, don't forget to put tmp back in the room
                room_items.pick_item(tmp)
    if len(args) > 0:
        for i in args:
            pick(i)
    else:
        try:
            print 'Current state of room:'
            room_items.print_inv()
            index = int(raw_input('room 6 : pick up at [room] index => '))
            assert index >= 0 and index < len(room_items.as_tuple())
            pick(room_items.as_tuple()[index].name)
        except:
            err('inventory error : invalid item to pick up')

def drop_item(args, helpmode=False, alias=None):
    # drop item from user inventory to room
    if helpmode:
        print_help(alias)
        print '  drops an item from the user inventory into the room'
        print '  can be invoked with an argument list or interactively'
        print '  examples:'
        print '    %s apple pear  # drops the <apple> and <pear> items' % alias
        print '    %s  # interactively drop items' % alias
        return
    global inv
    global room_items
    if len(inv.as_tuple()) < 1:
        err('drop : no items to drop')
        return
    def drop(i):
        print 'attempting to drop item \'%s\'' % i
        if i not in [item.name for item in inv.as_tuple()]:
            err('drop : item \''+i+'\' not found in user inventory')
        else:
            try:
                index = [item.name for item in inv.as_tuple()].index(i)
                tmp = inv.drop_item(index)
                assert tmp != inventory.NULL
                assert room_items.pick_item(tmp) > 0
                print 'successfully dropped item \''+i+'\''
            except:
                err('inventory error : invalid item to drop')
    if len(args) > 0:
        for i in args:
            drop(i)
    else:
        try:
            print 'Current state of user inventory:'
            inv.print_inv()
            index = int(raw_input('room 6 : drop at [inventory] index => '))
            assert index >= 0 and index < len(inv.as_tuple())
            drop(inv.as_tuple()[index].name)
        except:
            err('inventory error : invalid item to drop')

def bye(args, helpmode=False, alias=None):
    # leaves---implemented in user input loop
    if helpmode:
        print_help(alias)
        print '  exits the room'
        return
    pass  # purposely left empty---exit is handled in loop

usr_dict = {
    '?': help_func,
    'try': try_item,
    'show': show_inv,
    'pick': pick_item,
    'drop': drop_item,
    'q': bye
}

def play(global_inv):
    global inv
    inv = global_inv

    # greet player
    print '\n'+'='*80
    print 'Welcome to room 6!\n'
    print ('This room houses the artificial intelligence known as the '
           'Janitorial Entity for Fighting Foreigners (JEFF). As the name '
           'might suggest, JEFF\'s primary purpose is to protect the ship '
           'from invaders. However, due to your accelerated awakening, it '
           'believe you to be an intruder! Please exterminate JEFF before it '
           'exterminates you.\n')
    print '='*80+'\n'
    print 'Hint: try using one of the items in your backpack to help...\n'

    # give a special message if the user has the *special thing*
    for item in inv.as_tuple():
        if hashlib.sha256(item.name).hexdigest() == item_hash:
           print 'I see you have an item called \'%s\'...' % item.name
           print 'You know, brute force is NEVER the right solution...NEVER...'
           break

    # user input loop
    cmd = ''
    while cmd not in ['q', 'quit']:
        raw_in = raw_input('room 6 => ').strip().split(' ')
        cmd = raw_in[0]
        try:
            usr_dict[cmd](raw_in[1:])
        except:
            try:
                # is command <func>?
                assert cmd[-1] == '?'
                usr_dict[cmd[:-1]](raw_in[1:], helpmode=True, alias=cmd[:-1])
            except:
                err('unrecognized command')
    return win

if __name__ == '__main__':
    play(inventory.Inventory())
