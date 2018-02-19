import hashlib

#room 4 introduction and directions
print "Welcome to room 4!\n"
print "===================================================================================================="
print "You have entered the command center."
print "You are surrounded by many computers which are not functioning. To access the terminal, type in the"
print "correct password into the matching computer. Then, send an SOS to nearby ships using a keycard."
print "===================================================================================================="
print "\nYou can get help with the \'?\' command. Good luck!"

passwords = "ketchup, mustard, ranch" #possible passwords for room
message = False #variable to keep track of state of engine
password = False #variable to keep track of state of computer password
backpack = [] #list to keep track of state of backpack
cmd = '' #variable to keep track of user's commands
   
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
        while password == False:
            passDecision = raw_input("Enter a password : ") #keep prompting user to enter correct password if incorrect one is entered
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
        if "keycard" in backpack: #if user has keycard in backpack, prompt to use the keycard to send SOS message
            print " _____ "
            print "|\ ~ /|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|}}:{{|"
            print "|/_~_\|"
            print "You seem to have a keycard in your backpack."
            keycardDecision = raw_input("Would you like to use your keycard to send an SOS message to the ships A)Yes B)No : ")
            if keycardDecision.upper() == "A" or keycardDecision.upper() == "YES":
                print " ___  ___  ___  " #send SOS message if user agrees to use keycard
                print "/ __|/ _ \/ __| "
                print "\__ \ (_) \__ \ "
                print "|___/\___/|___/ "
                print "An SOS message has been sent."
                message = True
                print "The keycard has self-destructed."
                backpack.remove("keycard") #remove keycard from backpack once used

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
        if "USB" in backpack: #if user has USB in backpack, prompt to use USB to open door
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
                print "You enter the next room." #if user agrees to use USB, open door and exit program
                global cmd
                cmd = 'quit' #set cmd to quit to exit program

#function to access cabinet 1                
def cabinet1():
    if "CD" in backpack:
        print "There is nothing in Cabinet 1." #if CD is already in backpack, say cabinet 1 is empty
    else:
        print " _________"
        print "|^|     | |"
        print "| |_____| |"
        print "|  _____  |"
        print "| |     | |"
        print "| |_____| |"
        print "|_|_____|_|"
        print "There seems to be a CD in Cabinet 1."       
        cdDecision = raw_input("Would you like to put the CD into your backpack A)Yes B)No : ") #prompt user to put CD into backpack
        if cdDecision.upper() == "A" or cdDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put CD into backpack
            else:
                backpack.append("CD")
                print "The CD has been added to your backpack." #otherwise add CD into backpack

#function to access cabinet 2    
def cabinet2():
    if "keycard" in backpack or message == True:
        print "There is nothing in Cabinet 2." #if keycard is already in backpack or SOS message has already been sent, say cabinet 2 is empty
    else:
        print " _____ "
        print "|\ ~ /|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|}}:{{|"
        print "|/_~_\|"
        print "There seems to be a keycard in Cabinet 2."
        kcDecision = raw_input("Would you like to put the keycard into your backpack A)Yes B)No : ") #prompt user to put keycard into backpack
        if kcDecision.upper() == "A" or kcDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put keycard into backpack
            else:
                backpack.append("keycard")
                print "The keycard has been added to your backpack." #otherwise add keycard into backpack

#function to access cabinet 3    
def cabinet3():
    if "USB" in backpack:
        print "There is nothing in Cabinet 3." #if USB is already in backpack, say cabinet 3 is empty
    else:
        print " _   ,--()"
        print "( )-'-.------|>"
        print " -     `--[]"
        print "There seems to be a USB in Cabinet 3."
        usbbDecision = raw_input("Would you like to put the USB into your backpack A)Yes B)No : ") #prompt user to put USB into backpack
        if usbbDecision.upper() == "A" or usbbDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put USB into backpack
            else:
                backpack.append("USB")
                print "The USB has been added to your backpack." #otherwise add USB into backpack

#function to display contents of user backpack
def showBackpack(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      show your current backpack'
        return
    if len(backpack) < 1: #if nothing in backpack, display appropriate message
        print 'your backpack is empty'
        return -1
    print '\nCurrent state of your backpack:' #display all contents in backpack with quantities (1)
    for item in backpack:
        print "1 " + item
    return

#function to drop items from user backpack
def dropItem(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '      interactively drop an item from your backpack'
        return
    if len(backpack) < 1: #if nothing in backpack, display appropriate message
        err('no items to drop')
        return
    try:
        showBackpack()  #display contents of backpack
        item = raw_input('room 4 : drop item => ') #remove item that user enters
        backpack.remove(item)
    except:
        err('backpack error (invalid item to drop)') #show error message if entry does not match any backpack item

#function to display format of all errors
def err(text):
    print 'room 4 : error : %s' % text #print error message
    
#function that intentionally does nothing in order to exit program    
def bye(h=False, f=None):
    if h:
        print 'Help entry for: quit, leave, exit, q, X'  # need many aliases
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
    print 'you can get contextual help with <cmd>?'
        
#dictionary containing commands and respective function calls         
userDictionary = {'?': help, 'quit': bye, 'computer 1': computer1, 'computer 2': computer2, 'computer 3': computer3,
                'door': door, 'cabinet 1': cabinet1, 'cabinet 2': cabinet2, 'cabinet 3': cabinet3,
                'send sos': SOS, 'show backpack': showBackpack, 'drop item': dropItem}
        
#user input prompt/commands
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