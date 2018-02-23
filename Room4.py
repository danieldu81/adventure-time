import hashlib
import inventory

name = 'room 4'
win = False

passwords = "ketchup, mustard, ranch" #possible passwords for room
message = False #variable to keep track of state of engine
password = False #variable to keep track of state of computer password
inv = inventory.Inventory() #generate a user inventory
cmd = '' #variable to keep track of user's commands

cabinet1 = inventory.Inventory() #create inventory for cabinet 1
cabinet2 = inventory.Inventory() #create inventory for cabinet 2
cabinet3 = inventory.Inventory() #create inventory for cabinet 3

CD = inventory.Item('CD', description='a very sharp discus', weight=2) #create CD item
keycard = inventory.Item('keycard', description='a panacea to your issues', weight=1) #create keycard item
USB = inventory.Item('USB', description='a wicked device', weight=1) #create USB item

cabinet1.pick_item(CD) #put CD in cabinet 1
cabinet2.pick_item(keycard) #put keycard in cabinet 2
cabinet3.pick_item(USB) #put USB in cabinet 3

#function to access computer 1
def computer1():
    print "   _______________   "
    print "  |  ___________  |  "
    print "  | |           | |  "
    print "  | |           | |  "
    print "  | |   BROKEN  | |  "
    print "  | |           | |  "
    print "  | |___     ___| |  "
    print "  |_____|\_/|_____|  "
    print "    _|__|/ \|__|_    "
    print "   / *********** \   "
    print " /  *************  \ "
    print "---------------------"
    print "Computer 1 has been opened."
    print "Computer 1 looks very interesting, but it appears to be broken." #display filler message

#function to access computer 2
def computer2():
    print "   _______________   "
    print "  |  ___________  |  "
    print "  | |           | |  "
    print "  | |           | |  "
    print "  | |   BROKEN  | |  "
    print "  | |           | |  "
    print "  | |___     ___| |  "
    print "  |_____|\_/|_____|  "
    print "    _|__|/ \|__|_    "
    print "   / *********** \   "
    print " /  *************  \ "
    print "---------------------"
    print "Computer 2 has been opened."
    print "Computer 2 looks very interesting, but it appears to be broken." #display filler message

#function to access computer 3 and password
def computer3():
    global password
    print "Computer 3 has been opened."
    if password == True:
        print "   _______________   "
        print "  |  ___________  |  "
        print "  | |           | |  "
        print "  | |           | |  "
        print "  | |           | |  "
        print "  | |           | |  "
        print "  | |___     ___| |  "
        print "  |_____|\_/|_____|  "
        print "    _|__|/ \|__|_    "
        print "   / *********** \   "
        print " /  *************  \ "
        print "---------------------"
        print "Computer 3 looks very interesting." #if password has already been entered correctly before, display filler message
    else:
        print "   _______________   "
        print "  |  ___________  |  "
        print "  | |           | |  "
        print "  | |           | |  "
        print "  | |  PASSWORD | |  "
        print "  | |           | |  "
        print "  | |___     ___| |  "
        print "  |_____|\_/|_____|  "
        print "    _|__|/ \|__|_    "
        print "   / *********** \   "
        print " /  *************  \ "
        print "---------------------"
        print "Computer 3 seems to require a password." #if password has not yet been entered correctly, prompt user
        passDecision = raw_input("Enter a password : ").strip() #keep prompting user to enter correct password if incorrect one is entered
        if hashlib.sha256(passDecision.lower()).hexdigest().upper() == "A1D648CFFA6E2BA0F94C51F51E0CB8F2BE4FA6C3D227176016291F9CE64E90E7": #compare entered phrase to correct HASH-256 encoded phrase
            print "   _______________   "
            print "  |  ___________  |  "
            print "  | |           | |  "
            print "  | |           | |  "
            print "  | |  ACCESSED | |  "
            print "  | |           | |  "
            print "  | |___     ___| |  "
            print "  |_____|\_/|_____|  "
            print "    _|__|/ \|__|_    "
            print "   / *********** \   "
            print " /  *************  \ "
            print "---------------------"
            print "That is the correct password."
            print "Computer 3 has been accessed."
            password = True #set variable password to true
        else:
            print "Sorry, that is incorrect."

#function to send SOS message
def SOS():
    global message
    if password == False:
        print "A computer must be fixed before sending the SOS message." #do not allow user to send SOS message if correct password has not been entered into computer 3
    elif message == True:
        print "An SOS message has already been sent." #if SOS message has already been sent before, display filler message
    else:
        print "The ship's communication line with nearby ships has been opened."
        print "A keycard is needed to send an SOS message."
        if "keycard" in [item.name for item in inv.as_tuple()]: #if user has keycard in inventory, prompt to use the keycard to send SOS message
            print " _____ "
            print "|\ ~ /|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|/_~_\|"
            print "You seem to have a keycard in your inventory."
            keycardDecision = raw_input("Would you like to use your keycard to send an SOS message to the ships A)Yes B)No : ").strip()
            if keycardDecision.upper() == "A" or keycardDecision.upper() == "YES":
                print " ___  ___  ___  " #send SOS message if user agrees to use keycard
                print "/ __|/ _ \/ __| "
                print "\__ \ (_) \__ \ "
                print "|___/\___/|___/ "
                print "An SOS message has been sent."
                message = True

#function to access door to next room
def door():
    print "The door to the next room lies in front of you."
    print "An SOS message must be sent before proceeding."
    if message == True: #if user has sent SOS message, display message that door requires USB to open
        print " ______________   "
        print "|\ ___________ /| "
        print "| |  _ _ _ _  | | "
        print "| | | | | | | | | "
        print "| | |-+-+-+-| | | "
        print "| | |-+-+=+%| | | "
        print "| | |_|_|_|_| | | "
        print "| |    ___    | | "
        print "| |   [___] ()| | "
        print "| |         ||| | "
        print "| |         ()| | "
        print "| |           | | "
        print "| |           | | "
        print "| |           | | "
        print "|_|___________|_| "
        print "There seems to be slot in the door that requires a USB."
        if "USB" in [item.name for item in inv.as_tuple()]: #if user has USB in inventory, prompt to use USB to open door
            print " _   ,--()"
            print "( )-'-.------|>"
            print " -     `--[]"
            usbDecision = raw_input("Would you like to use your USB to open the door A)Yes B)No : ").strip()
            if usbDecision.upper() == "A" or usbDecision.upper() == "YES":
                print " ______________   "
                print "|\ ___________ /| "
                print "| |  /|,| |   | | "
                print "| | |,x,| |   | | "
                print "| | |,x,' |   | | "
                print "| | |,x   ,   | | "
                print "| | |/    |   | | "
                print "| |    /] ,   | | "
                print "| |   [/ ()   | | "
                print "| |       |   | | "
                print "| |       |   | | "
                print "| |       |   | | "
                print "| |      ,'   | | "
                print "| |   ,'      | | "
                print "|_|,'_________|_| "
                print "You successfully open the door, which now leads to the next room."
                print "You enter the next room." #if user agrees to use USB, open door and exit program
                global cmd
                cmd = 'quit' #set cmd to quit to exit program
                global win
                win = True

def show_cabinet_1(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 1'
        return
    if len(cabinet1.as_tuple()) < 1:
        print 'Cabinet 1 is empty and void' #display empty message if cabinet 1 is empty
        return -1
    print '\nCurrent items visible in Cabinet 1:' #display current items in cabinet 1
    return cabinet1.print_inv()

def show_cabinet_2(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 2'
        return
    if len(cabinet2.as_tuple()) < 1:
        print 'Cabinet 2 is empty and void' #display empty message if cabinet 2 is empty
        return -1
    print '\nCurrent items visible in Cabinet 2:' #display current items in cabinet 2
    return cabinet2.print_inv()

def show_cabinet_3(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 3'
        return
    if len(cabinet3.as_tuple()) < 1:
        print 'Cabinet 3 is empty and void' #display empty message if cabinet 3 is empty
        return -1
    print '\nCurrent items visible in Cabinet 3:' #display current items in cabinet 3
    return cabinet3.print_inv()

#function to access cabinet 1
def cabinet_1(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 1'
        return
    if "CD" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 1." #if CD is already in inventory, say cabinet 1 is empty
        return -1
    else:
        print " _________"
        print "|^|     | |"
        print "| |_____| |"
        print "|  _____  |"
        print "| |     | |"
        print "| |_____| |"
        print "|_|_____|_|"
        print "There seems to be a CD in Cabinet 1."
        cdDecision = raw_input("Would you like to put the CD into your inventory A)Yes B)No : ").strip() #prompt user to put CD into inventory
        if cdDecision.upper() == "A" or cdDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put CD into inventory
            else:
                try:
                    show_cabinet_1() #display items in cabinet 1
                    index = int(raw_input('room 4 : pick up at [room] index => ').strip()) #prompt user to choose item at index
                    tmp = cabinet1.drop_item(index) #drop item from cabinet 1
                    assert tmp != inventory.NULL
                    assert inv.pick_item(tmp) > 0 #pick up item into inventory
                except:
                     err('inventory error (invalid item to pick up)')

#function to access cabinet 2
def cabinet_2(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 2'
        return
    if "keycard" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 2." #if keycard is already in inventory, say cabinet 2 is empty
        return -1
    else:
        print " _____ "
        print "|\ ~ /|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|/_~_\|"
        print "There seems to be a keycard in Cabinet 2."
        kcDecision = raw_input("Would you like to put the keycard into your inventory A)Yes B)No : ").strip() #prompt user to put keycard into inventory
        if kcDecision.upper() == "A" or kcDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put keycard into inventory
            else:
                try:
                    show_cabinet_2() #display items in cabinet 2
                    index = int(raw_input('room 4 : pick up at [room] index => ').strip()) #prompt user to choose item at index
                    tmp = cabinet2.drop_item(index) #drop item from cabinet 2
                    assert tmp != inventory.NULL
                    assert inv.pick_item(tmp) > 0 #pick up item into inventory
                except:
                     err('inventory error (invalid item to pick up)')

#function to access cabinet 3
def cabinet_3(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show the items currently visible in Cabinet 3'
        return
    if "USB" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 3." #if USB is already in inventory, say cabinet 3 is empty
        return -1
    else:
        print " _   ,--()"
        print "( )-'-.------|>"
        print " -     `--[]"
        print "There seems to be a USB in Cabinet 3."
        usbbDecision = raw_input("Would you like to put the USB into your inventory A)Yes B)No : ").strip() #prompt user to put USB into inventory
        if usbbDecision.upper() == "A" or usbbDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put hammer into inventory
            else:
                try:
                    show_cabinet_3() #display items in cabinet 3
                    index = int(raw_input('room 4 : pick up at [room] index => ').strip()) #prompt user to choose item at index
                    tmp = cabinet3.drop_item(index) #drop item from cabinet 3
                    assert tmp != inventory.NULL
                    assert inv.pick_item(tmp) > 0 #pick up item into inventory
                except:
                     err('inventory error (invalid item to pick up)')

#function to display contents of user inv
def showInv(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show your current inventory'
        return
    if len(inv.as_tuple()) < 1: #if nothing in inventory, display appropriate message
        print 'your inventory is empty'
        return -1
    print '\nCurrent state of your inventory:' #display all contents in inventory
    return inv.print_inv()

#function to drop items from user inv
def dropItem(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      interactively drop an item from your inventory'
        return
    if len(inv.as_tuple()) < 1: #if nothing in inventory, display appropriate message
        err('no items to drop')
        return
    try:
        showInv()  #display contents of inventory
        index = int(raw_input('room 4 : drop at [inventory] index => ').strip()) #user input index
        tmp = inv.drop_item(index) #drop item at index
        assert tmp != inventory.NULL
        assert cabinet1.pick_item(tmp) > 0
        assert cabinet2.pick_item(tmp) > 0
        assert cabinet3.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to drop)') #show error message if entry does not match any inventory item

#function to display format of all errors
def err(text):
    print 'room 4 : error : %s' % text #print error message

#function that intentionally does nothing in order to exit program
def bye(h=False, f=None):
    if h:
        print 'Help entry for: quit'
        print '  * - the exit function'
        print '      leaves the room'
        print '      all aliases of this function are equivalent'

#function to display commands in order to help user understand how to use program
def help(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '  ? - the help function'
        print '      can be invoked alone to display available commands'
        print '      can be invoked after a function for contextual help'
        print '  examples'
        print '      ?'
        print '      computer?'
        return
    print 'Available commands:' #print each command in userDictionary for user to use
    for key in userDictionary:
        print '  '+key

#dictionary containing commands and respective function calls
userDictionary = {'?': help, 'quit': bye, 'computer 1': computer1, 'computer 2': computer2, 'computer 3': computer3,
                'door': door, 'cabinet 1': cabinet_1, 'cabinet 2': cabinet_2, 'cabinet 3': cabinet_3,
                'send sos': SOS, 'show inv': showInv, 'drop item': dropItem}

def play(global_inv):
    global inv
    inb = global_inv

    #room 4 introduction and directions
    print "\nWelcome to room 4!\n"
    print "="*80
    print "You have entered the command center."
    print "You are surrounded by many computers which are not functioning. To access the terminal, type in the"
    print "correct password into the matching computer. Then, send an SOS to nearby ships using a keycard."
    print "="*80
    print "\nYou can get help with the \'?\' command. Good luck!"

    #user input prompt/commands
    global cmd
    while cmd not in ['quit']:
        cmd = raw_input('room 4 => ').strip() #strip user input of whitespace
        try:
            userDictionary[cmd]() #see if the command is in the dictionary
        except:
            try:
                assert cmd[-1] == '?' #see if command is <func>?
                userDictionary[cmd[:-1]](h=True, f=cmd[:-1])
            except:
                err('unrecognized input. try \'?\' for help') #show error message for unrecognized input

if __name__ == '__main__':
    play(inventory.Inventory())
