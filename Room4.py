import hashlib

print "Welcome to room 4!\n"
print "===================================================================================================="
print "You have entered the command center."
print "You are surrounded by many computers which are not functioning. To access the terminal, type in the"
print "correct password into the matching computer. Then, send an SOS to nearby ships using a keycard."
print "===================================================================================================="
print "\nYou can get help with the \'?\' command. Good luck!"

passwords = "ketchup, mustard, ranch"
message = False
password = False
backpack = []
cmd = ''
   
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
    print "Computer 1 looks very interesting, but it appears to be broken."
        
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
    print "Computer 2 looks very interesting, but it appears to be broken."
        
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
        print "Computer 3 looks very interesting."
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
        print "Computer 3 seems to require a password."
        while password == False:
            passDecision = raw_input("Enter a password : ")
            if hashlib.sha256(passDecision.lower()).hexdigest().upper() == "A1D648CFFA6E2BA0F94C51F51E0CB8F2BE4FA6C3D227176016291F9CE64E90E7":
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
                password = True
            else:
                print "Sorry, that is incorrect."
               
def SOS():
    global message
    if password == False:
        print "A computer must be fixed before sending the SOS message."
    elif message == True:
        print "An SOS message has already been sent."
    else: 
        print "The ship's communication line with nearby ships has been opened."
        print "A keycard is needed to send an SOS message."
        if "keycard" in backpack:
            print " _____ "
            print "|\ ~ /|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|/_~_\|"
            print "You seem to have a keycard in your backpack."
            keycardDecision = raw_input("Would you like to use your keycard to send an SOS message to the ships A)Yes B)No : ")
            if keycardDecision.upper() == "A" or keycardDecision.upper() == "YES":
                print " ___  ___  ___  "
                print "/ __|/ _ \/ __| "
                print "\__ \ (_) \__ \ "
                print "|___/\___/|___/ "
                print "An SOS message has been sent."
                message = True
                print "The keycard has self-destructed."
                backpack.remove("keycard")
    
def door():
    print "The door to the next room lies in front of you."
    print "An SOS message must be sent before proceeding."
    if message == True:
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
        if "USB" in backpack:
            print " _   ,--()"
            print "( )-'-.------|>"
            print " -     `--[]"
            usbDecision = raw_input("Would you like to use your USB to open the door A)Yes B)No : ")
            if usbDecision.upper() == "A" or usbDecision.upper() == "YES":
                print " ______________   "
                print "|\ ___________ /| "
                print "| |  /|,| |   | | "
                print "| | |,x,| |   | | "
                print "| | |,x,' |   | | "
                print "| | |,x   ,   | | "
                print "| | |/    |%==| | "
                print "| |    /] ,   | | "
                print "| |   [/ ()   | | "
                print "| |       |   | | "
                print "| |       |   | | "
                print "| |       |   | | "
                print "| |      ,'   | | "
                print "| |   ,'      | | "
                print "|_|,'_________|_| "
                print "You successfully open the door, which now leads to the next room."
                print "You enter the next room."
                global cmd
                cmd = 'quit'
                
def cabinet1():
    if "CD" in backpack:
        print "There is nothing in Cabinet 1."
    else:
        print " _________"
        print "|^|     | |"
        print "| |_____| |"
        print "|  _____  |"
        print "| |     | |"
        print "| |_____| |"
        print "|_|_____|_|"
        print "There seems to be a CD in Cabinet 1."       
        cdDecision = raw_input("Would you like to put the CD into your backpack A)Yes B)No : ")
        if cdDecision.upper() == "A" or cdDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("CD")
                print "The CD has been added to your backpack."
    
def cabinet2():
    if "keycard" in backpack or message == True:
        print "There is nothing in Cabinet 2."
    else:
        print " _____ "
        print "|\ ~ /|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|/_~_\|"
        print "There seems to be a keycard in Cabinet 2."
        kcDecision = raw_input("Would you like to put the keycard into your backpack A)Yes B)No : ")
        if kcDecision.upper() == "A" or kcDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("keycard")
                print "The keycard has been added to your backpack."
    
def cabinet3():
    if "USB" in backpack:
        print "There is nothing in Cabinet 3."
    else:
        print " _   ,--()"
        print "( )-'-.------|>"
        print " -     `--[]"
        print "There seems to be a USB in Cabinet 3."
        usbbDecision = raw_input("Would you like to put the USB into your backpack A)Yes B)No : ")
        if usbbDecision.upper() == "A" or usbbDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("USB")
                print "The USB has been added to your backpack."

# the room provides a wrapper for inventory functions
def showBackpack(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show your current backpack'
        return
    if len(backpack) < 1:
        print 'your backpack is empty'
        return -1
    print '\nCurrent state of your backpack:'
    for item in backpack:
        print item
    return

def dropItem(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      interactively drop an item from your backpack'
        return
    if len(backpack) < 1:
        err('no items to drop')
        return
    try:
        showBackpack()  # we have already checked for
        item = raw_input('room 4 : drop item => ')
        backpack.remove(item)
    except:
        err('backpack error (invalid item to drop)')

# log error --- standardize this later
def err(text):
    print 'room 4 : error : %s' % text
    
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
        print '      computer?'
        return
    print 'Available commands:'
    for key in userDictionary:
        print '  '+key
    print 'you can get contextual help with <cmd>?'
        
userDictionary = {'?': help, 'quit': bye, 'computer 1': computer1, 'computer 2': computer2, 'computer 3': computer3,
                'door': door, 'cabinet 1': cabinet1, 'cabinet 2': cabinet2, 'cabinet 3': cabinet3,
                'send sos': SOS, 'show backpack': showBackpack, 'drop item': dropItem}
        
# user input prompt
while cmd not in ['quit']:
    cmd = raw_input('room 4 => ').strip()
    try:
        userDictionary[cmd]()  # see if the command is in the dict
    except:
        try:
            assert cmd[-1] == '?'  # see if command is <func>?
            userDictionary[cmd[:-1]](h=True, f=cmd[:-1])
        except:
            err('unrecognized input. try \'?\' for help')