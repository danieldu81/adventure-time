import hashlib

#room 3 introduction and directions
print "Welcome to room 3!\n"
print "===================================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must enter the correct password"
print "into the computer and then change the current path of the engine."
print "===================================================================================================="
print "\nYou can get help with the \'?\' command. Good luck!"

passwords = "ketchup, mustard, ranch" #possible passwords for room
engine = False #variable to keep track of state of engine
password = False #variable to keep track of state of computer password
backpack = [] #list to keep track of state of backpack
cmd = '' #variable to keep track of user's commands
  
#function to access computer and password  
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
        print "The computer looks very interesting." #if password has already been entered correctly before, display filler message
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
        print "The computer screen seems to require a password." #if password has not yet been entered correctly, prompt user
        while password == False:
            passDecision = raw_input("Enter a password : ") #keep prompting user to enter correct password if incorrect one is entered
            if hashlib.sha256(passDecision.lower()).hexdigest().upper() == "0BC3A5AE30466DE3D77B506D364EABC28B1B7CEEA061C2519328C7BE72827483": #compare entered phrase to correct HASH-256 encoded phrase
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
                password = True #set variable password to true
            else:
                print "Sorry, that is incorrect."

#function to access engine                
def engine():
    if password == False: #do not allow user to access engine if correct password has not been entered into computer
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
            print "The engine looks very interesting." #if engine has already been fixed before, display filler message
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
            if "welder" in backpack: #if user has welder in backpack, prompt to use the welder to fix engine
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
                    print "The ship's engine has been fixed." #fix engine if user agrees to use welder
                    engine = True

#function to access door to next room    
def door():
    print "The door to the next room lies in front of you."
    if engine == True and password == True: #if password and engine are both true, display message that door requires wrench
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
        if "wrench" in backpack: #if user has wrench in backpack, prompt to use wrench to fix door
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
                print "You enter the next room." #if user agrees to use wrench, fix door and exit program for user to enter next room
                global cmd
                cmd = 'quit' #set cmd to quit to exit program      

#function to access cabinet 1
def cabinet1():
    if "welder" in backpack:
        print "There is nothing in Cabinet 1." #if welder is already in backpack, say cabinet 1 is empty
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
        welderDecision = raw_input("Would you like to put the welder into your backpack A)Yes B)No : ") #prompt user to put welder into backpack
        if welderDecision.upper() == "A" or welderDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put welder into backpack
            else:
                backpack.append("welder")
                print "The welder has been added to your backpack." #otherwise add welder into backpack

#function to access cabinet 2                
def cabinet2():
    if "hammer" in backpack:
        print "There is nothing in Cabinet 2." #if hammer is already in backpack, say cabinet 2 is empty
    else:
        print "                          \`.  "  
        print ".--------------.___________) \ "
        print "|//////////////|___________[ ] "
        print "`--------------'           ) ( " 
        print "                           '-' "
        print "There seems to be a hammer in Cabinet 2."   
        hammerDecision = raw_input("Would you like to put the hammer into your backpack A)Yes B)No : ") #prompt user to put hammer into backpack
        if hammerDecision.upper() == "A" or hammerDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put hammer into backpack
            else:
                backpack.append("hammer")
                print "The hammer has been added to your backpack." #otherwise add hammer into backpack

#function to access cabinet 3
def cabinet3():
    if "wrench" in backpack:
        print "There is nothing in Cabinet 3." #if wrench is already in backpack, say cabinet 3 is empty
    else:
        print " .----.                                .---.   "
        print "'---,  `.____________________________.'  _  `. "
        print "     )   ____________________________   <_>  : "
        print ".---'  .'                            `.     .' "
        print " `----'                                `---'   "  
        print "There seems to be a wrench in Cabinet 3."         
        wrenchDecision = raw_input("Would you like to put the wrench into your backpack A)Yes B)No : ") #prompt user to put wrench into backpack
        if wrenchDecision.upper() == "A" or wrenchDecision.upper() == "YES":
            if len(backpack) > 5:
                print "Your backpack seems to be full." #if backpack has 5 items, do not put wrench into backpack
            else:
                backpack.append("wrench")
                print "The wrench has been added to your backpack." #otherwise add wrench into backpack

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
        item = raw_input('room 3 : drop item => ') #remove item that user enters
        backpack.remove(item)
    except:
        err('backpack error (invalid item to drop)') #show error message if entry does not match any backpack item

#function to display format of all errors
def err(text):
    print 'room 3 : error : %s' % text #print error message
    
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
userDictionary = {'?': help, 'quit': bye, 'computer': computer, 'engine': engine, 
                'door': door, 'cabinet 1': cabinet1, 'cabinet 2': cabinet2, 'cabinet 3': cabinet3,
                'show backpack': showBackpack, 'drop item': dropItem}
        
#user input prompt/commands
while cmd not in ['quit']:
    cmd = raw_input('room 3 => ').strip() #strip user input of whitespace
    try:
        userDictionary[cmd]() #see if the command is in the dictionary
    except:
        try:
            assert cmd[-1] == '?'  #see if command is <func>?
            userDictionary[cmd[:-1]](h=True, f=cmd[:-1])
        except:
            err('unrecognized input. try \'?\' for help') #show error message for unrecognized input