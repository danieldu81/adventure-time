#room 3 introduction and directions
print "\nWelcome to room 3!\n"
print "===================================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must enter the correct password"
print "into the computer and then change the current path of the engine."
print "===================================================================================================="
print "\nYou can get help with the \'?\' command. Good luck!"

import hashlib
import inventory

passwords = "ketchup, mustard, ranch" #possible passwords for room
engine = False #variable to keep track of state of engine
password = False #variable to keep track of state of computer password
inv = inventory.Inventory() #generate a user inventory
cmd = '' #variable to keep track of user's commands

cabinet1 = inventory.Inventory() #create inventory for cabinet 1
cabinet2 = inventory.Inventory() #create inventory for cabinet 2
cabinet3 = inventory.Inventory() #create inventory for cabinet 3

welder = inventory.Item('welder', description='a welding tool', weight=3) #create welder item
hammer = inventory.Item('hammer', description='an exceedingly dangerous weapon', weight=2) #create hammer item
wrench = inventory.Item('wrench', description='a wretched wrench', weight=2) #create wrench item

cabinet1.pick_item(welder) #put welder in cabinet 1
cabinet2.pick_item(hammer) #put hammer in cabinet 2
cabinet3.pick_item(wrench) #put wrench in cabinet 3
  
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
        passDecision = raw_input("Enter a password : ").strip() #keep prompting user to enter correct password if incorrect one is entered
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
            print inv.as_tuple()
            if "welder" in [item.name for item in inv.as_tuple()]: #if user has welder in inventory, prompt to use the welder to fix engine
                print "  .-------------.     "
                print " /             / |    "
                print "/+============+\ |    "
                print "||            || |    "
                print "||            || |    " 
                print "||            ||/@@@  "  
                print "\+============+/    @ " 
                print "                   @  "
                print "                  @   "
                print "You seem to have a welder in your inv."
                engDecision = raw_input("Would you like to use it on the engine A)Yes B)No : ").strip()
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
        if "wrench" in [item.name for item in inv.as_tuple()]: #if user has wrench in inventory, prompt to use wrench to fix door
            print " .----.                                .---.   "
            print "'---,  `.____________________________.'  _  `. "
            print "     )   ____________________________   <_>  : "
            print ".---'  .'                            `.     .' "
            print " `----'                                `---'   "  
            boltDecision = raw_input("Would you like to use your wrench to fix the loose bolt A)Yes B)No : ").strip()
            if boltDecision.upper() == "A" or boltDecision.upper() == "YES":
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
                print "You successfully fix the door, which now opens to the next room."
                print "You enter the next room." #if user agrees to use wrench, fix door and exit program for user to enter next room
                global cmd
                cmd = 'quit' #set cmd to quit to exit program  
                
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
    if "welder" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 1." #if welder is already in inventory, say cabinet 1 is empty
        return -1
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
        welderDecision = raw_input("Would you like to put the welder into your inventory A)Yes B)No : ").strip() #prompt user to put welder into inventory
        if welderDecision.upper() == "A" or welderDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put welder into inventory
            else:
                try:
                    show_cabinet_1() #display items in cabinet 1
                    index = int(raw_input('room 3 : pick up at [room] index => ').strip()) #prompt user to choose item at index
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
    if "hammer" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 2." #if hammer is already in inventory, say cabinet 2 is empty
        return -1
    else:
        print "                          \`.  "  
        print ".--------------.___________) \ "
        print "|//////////////|___________[ ] "
        print "`--------------'           ) ( " 
        print "                           '-' "
        print "There seems to be a hammer in Cabinet 2."   
        hammerDecision = raw_input("Would you like to put the hammer into your inventory A)Yes B)No : ").strip() #prompt user to put hammer into inventory
        if hammerDecision.upper() == "A" or hammerDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put hammer into inventory
            else:
                try:
                    show_cabinet_2() #display items in cabinet 2
                    index = int(raw_input('room 3 : pick up at [room] index => ').strip()) #prompt user to choose item at index
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
    if "wrench" in [item.name for item in inv.as_tuple()]:
        print "There is nothing in Cabinet 3." #if wrench is already in inventory, say cabinet 3 is empty
        return -1
    else:
        print " .----.                                .---.   "
        print "'---,  `.____________________________.'  _  `. "
        print "     )   ____________________________   <_>  : "
        print ".---'  .'                            `.     .' "
        print " `----'                                `---'   "  
        print "There seems to be a wrench in Cabinet 3."         
        wrenchDecision = raw_input("Would you like to put the wrench into your inventory A)Yes B)No : ").strip() #prompt user to put wrench into inventory
        if wrenchDecision.upper() == "A" or wrenchDecision.upper() == "YES":
            if len(inv.as_tuple()) > 5:
                print "Your inventory seems to be full." #if inventory has 5 items, do not put wrench into inventory
            else:
                try:
                    show_cabinet_3() #display items in cabinet 3
                    index = int(raw_input('room 3 : pick up at [room] index => ').strip()) #prompt user to choose item at index
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
        index = int(raw_input('room 3 : drop at [inventory] index => ').strip()) #user input index
        tmp = inv.drop_item(index) #drop item at index
        assert tmp != inventory.NULL
        assert cabinet1.pick_item(tmp) > 0
        assert cabinet2.pick_item(tmp) > 0
        assert cabinet3.pick_item(tmp) > 0
    except:
        err('inventory error (invalid item to drop)') #show error message if entry does not match any inventory item

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
                'door': door, 'cabinet 1': cabinet_1, 'cabinet 2': cabinet_2, 'cabinet 3': cabinet_3,
                'show inv': showInv, 'drop item': dropItem}
        
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