import hashlib

print "Welcome to room 3!\n"
print "===================================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must enter the correct password"
print "into the computer and then change the current path of the engine."
print "===================================================================================================="
print "\nYou can get help with the \'?\' command. Good luck!"

passwords = "ketchup, mustard, ranch"
engine = False
password = False
backpack = []
cmd = ''
        
def computer():
    print "The computer has been accessed."
    global password
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
        print "The computer looks very interesting."
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
        print "The computer screen seems to require a password."
        while password == False:
            passDecision = raw_input("Enter a password : ")
            if hashlib.sha256(passDecision.lower()).hexdigest().upper() == "0BC3A5AE30466DE3D77B506D364EABC28B1B7CEEA061C2519328C7BE72827483":
                print "That is the correct password."
                print "   _______________   " 
                print "  |  ___________  |  "
                print "  | |           | |  "
                print "  | |           | |  "   
                print "  | |   FIXED   | |  "    
                print "  | |           | |  "  
                print "  | |___     ___| |  "  
                print "  |_____|\_/|_____|  "  
                print "    _|__|/ \|__|_    "
                print "   / *********** \   "     
                print " /  *************  \ "    
                print "---------------------"
                print "The computer's error has been fixed."
                password = True
            else:
                print "Sorry, that is incorrect."
                
def engine():
    if password == False:
        print "The engine cannot be fixed without accessing the computer first."
    else:
        global engine
        if engine == True:
            print "  __________   " 
            print " /         /|   "
            print "/_________/ |  "
            print "|         | |  "   
            print "| |====|  | |  "    
            print "|         | |  "  
            print "| |====|  | |  "  
            print "|   ___   | |  "  
            print "|  |ENG|  | |  "
            print "|   ---   | |  "     
            print "|         | |  "    
            print "|_________|/   " 
            print "The engine looks very interesting."
        else:
            print "  __________   " 
            print " /         /|   "
            print "/_________/ |  "
            print "|         | |  "   
            print "| |====|  | |  "    
            print "|         | |  "  
            print "| |====|  | |  "  
            print "|   ___   | |  "  
            print "|  |ENG|  | |  "
            print "|   ---   | |  "     
            print "|         | |  "    
            print "|_________|/   "  
            print "The engine seems to require a welder to fix it."
            if "welder" in backpack:
                print "  .-------------.     "
                print " /             / |    "
                print "/+============+\ |    "
                print "||            || |    "
                print "||            || |    " 
                print "||            ||/@@@  "  
                print "\+============+/    @ " 
                print "                   @  "
                print "                  @   "
                print "You seem to have a welder in your backpack."
                engDecision = raw_input("Would you like to use it on the engine A)Yes B)No : ")
                if engDecision.upper() == "A" or engDecision.upper() == "YES":
                    print "The ship's engine has been fixed."
                    engine = True
    
def door():
    print "The door to the next room lies in front of you."
    if engine == True and password == True:
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
        print "There seems to be a loose bolt in the door that requires a wrench." 
        if "wrench" in backpack:
            print " .----.                                .---.   "
            print "'---,  `.____________________________.'  _  `. "
            print "     )   ____________________________   <_>  : "
            print ".---'  .'                            `.     .' "
            print " `----'                                `---'   "  
            boltDecision = raw_input("Would you like to use your wrench to fix the loose bolt A)Yes B)No : ")
            if boltDecision.upper() == "A" or boltDecision.upper() == "YES":
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
                print "You successfully fix the door, which now opens to the next room."
                print "You enter the next room." 
                global cmd
                cmd = 'quit'       

def cabinet1():
    if "welder" in backpack:
        print "There is nothing in Cabinet 1."
    else:
        print "  .-------------.     "
        print " /             / |    "
        print "/+============+\ |    "
        print "||            || |    "
        print "||            || |    " 
        print "||            ||/@@@  "  
        print "\+============+/    @ " 
        print "                   @  "
        print "                  @   "
        print "There seems to be a welder in Cabinet 1."
        welderDecision = raw_input("Would you like to put the welder into your backpack A)Yes B)No : ")
        if welderDecision.upper() == "A" or welderDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("welder")
                print "The welder has been added to your backpack."
                
def cabinet2():
    if "hammer" in backpack:
        print "There is nothing in Cabinet 2."
    else:
        print "                          \`.  "  
        print ".--------------.___________) \ "
        print "|//////////////|___________[ ] "
        print "`--------------'           ) ( " 
        print "                           '-' "
        print "There seems to be a hammer in Cabinet 2."   
        hammerDecision = raw_input("Would you like to put the hammer into your backpack A)Yes B)No : ")
        if hammerDecision.upper() == "A" or hammerDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("hammer")
                print "The hammer has been added to your backpack."

def cabinet3():
    if "wrench" in backpack:
        print "There is nothing in Cabinet 3."
    else:
        print " .----.                                .---.   "
        print "'---,  `.____________________________.'  _  `. "
        print "     )   ____________________________   <_>  : "
        print ".---'  .'                            `.     .' "
        print " `----'                                `---'   "  
        print "There seems to be a wrench in Cabinet 3."         
        wrenchDecision = raw_input("Would you like to put the wrench into your backpack A)Yes B)No : ")
        if wrenchDecision.upper() == "A" or wrenchDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full."
            else:
                backpack.append("wrench")
                print "The wrench has been added to your backpack."

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
        item = raw_input('room 3 : drop item => ')
        backpack.remove(item)
    except:
        err('backpack error (invalid item to drop)')

# log error --- standardize this later
def err(text):
    print 'room 3 : error : %s' % text
    
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
        
userDictionary = {'?': help, 'quit': bye, 'computer': computer, 'engine': engine, 
                'door': door, 'cabinet 1': cabinet1, 'cabinet 2': cabinet2, 'cabinet 3': cabinet3,
                'show backpack': showBackpack, 'drop item': dropItem}
        
# user input prompt
while cmd not in ['quit']:
    cmd = raw_input('room 3 => ').strip()
    try:
        userDictionary[cmd]()  # see if the command is in the dict
    except:
        try:
            assert cmd[-1] == '?'  # see if command is <func>?
            userDictionary[cmd[:-1]](h=True, f=cmd[:-1])
        except:
            err('unrecognized input. try \'?\' for help')