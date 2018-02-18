import hashlib

print "===================================================================================================="
print "You have entered the command center."
print "You are surrounded by many computers which are not functioning. To access the terminal, type in the"
print "correct password into the matching computer. Then, send an SOS to nearby ships using a keycard."
print "===================================================================================================="

passwords = "ketchup, mustard, ranch"
message = False
password = False
backpack = []

def routes():
    print "                            .______                          "
    print "                            |   _  \                         "
    print "                            |  |_)  |                        "
    print "                            |   _  <                         "
    print "                            |  |_)  |                        "
    print "                            |______/                         "
    print "                               /\                            "
    print "                              /  \                           "
    print "     ___         ___         / __ \        ___        ______ "
    print "    /   \       /  /        / |  | \       \  \      /      |"
    print "   /  ^  \     /  / ______    |  |     _____\  \    |  ,----'"
    print "  /  /_\  \   <  < |______|   |  |    |______>  >   |  |     "
    print " /  _____  \   \  \           |  |          /  /    |  `----."
    print "/__/     \__\   \__\          |__|         /__/      \______|"
    print "There appears to be three routes that you can take."
    routeDecision = raw_input("Would you like to go to the room's A)computers B)door C)cabinets : ")
    if routeDecision.upper() == "A" or routeDecision.upper() == "COMPUTERS":
        computers()
    elif routeDecision.upper() == "B" or routeDecision.upper() == "DOOR":
        door()
    elif routeDecision.upper() == "C" or routeDecision.upper() == "CABINETS":
        cabinets()
    else:
        print "That is not a valid option."
        routes()
    
def computers():
    print "   _______________       _______________       _______________   " 
    print "  |  ___________  |     |  ___________  |     |  ___________  |  "
    print "  | |           | |     | |           | |     | |           | |  "
    print "  | |           | |     | |           | |     | |           | |  "   
    print "  | |     1     | |     | |     2     | |     | |     3     | |  "    
    print "  | |           | |     | |           | |     | |           | |  "  
    print "  | |___     ___| |     | |___     ___| |     | |___     ___| |  "  
    print "  |_____|\_/|_____|     |_____|\_/|_____|     |_____|\_/|_____|  "  
    print "    _|__|/ \|__|_         _|__|/ \|__|_         _|__|/ \|__|_    "
    print "   / *********** \       / *********** \       / *********** \   "     
    print " /  *************  \   /  *************  \   /  *************  \ "    
    print "--------------------- --------------------- ---------------------"
    print "There seems to be a set of three computers in front of you." 
    exComDecision = raw_input("Would you like to examine the computers A)Yes B)No : ")
    if exComDecision.upper() == "A" or exComDecision.upper() == "YES":
        numComDecision = raw_input("Which computer would you like to open A)Computer 1 B)Computer 2 C)Computer 3 : ")
        if numComDecision.upper() == "A" or numComDecision.upper() == "COMPUTER 1":
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
            computers()
        elif numComDecision.upper() == "B" or numComDecision.upper() == "COMPUTER 2":
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
            computers()
        elif numComDecision.upper() == "C" or numComDecision.upper() == "COMPUTER 3":
            print "Computer 3 has been opened."
            if password == True and message == True:  
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
                computers()
            elif password == True and message == False:
                SOS()
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
                        global password
                        password = True
                        SOS()
                    else:
                        print "Sorry, that is incorrect."
                        computers()
        else:
            print "That is not a valid option."
            computers()
    elif exComDecision.upper() == "B" or exComDecision.upper() == "NO":
        print "You return to the beginning intersecton."
        routes()
    else:
        print "That is not a valid option."
        computers()
        
            
def SOS():
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
            global message
            message = True
            print "The keycard has self-destructed."
            backpack.remove("keycard")
            computers()
        elif keycardDecision.upper() == "B" or keycardDecision.upper() == "NO":
            computers()
        else:
            print "That is not a valid option."
            SOS()
    else:
        computers()
    
def door():
    print "   ______________   "
    print "  |\ ___________ /| "
    print "  | |  _ _ _ _  | | "
    print "  | | | | | | | | | "
    print "  | | |-+-+-+-| | | "
    print "  | | |-+-+=+%| | | "
    print "  | | |_|_|_|_| | | "
    print "  | |    ___    | | "
    print "  | |   [___] ()| | "
    print "  | |         ||| | "
    print "  | |         ()| | "
    print "  | |           | | "
    print "  | |           | | "
    print "  | |           | | "
    print "  |_|___________|_| "
    print "The door to the next room lies in front of you."
    if message == True and password == True:
        print "There seems to be slot in the door that requires a USB."
        print "   _   ,--()"
        print "  ( )-'-.------|>"
        print "   -     `--[]"
        if "USB" in backpack:
            usbDecision = raw_input("Would you like to use your USB to open the door A)Yes B)No : ")
            if usbDecision.upper() == "A" or usbDecision.upper() == "YES":
                print "   ______________   "
                print "  |\ ___________ /| "
                print "  | |  /|,| |   | | "
                print "  | | |,x,| |   | | "
                print "  | | |,x,' |   | | "
                print "  | | |,x   ,   | | "
                print "  | | |/    |%==| | "
                print "  | |    /] ,   | | "
                print "  | |   [/ ()   | | "
                print "  | |       |   | | "
                print "  | |       |   | | "
                print "  | |       |   | | "
                print "  | |      ,'   | | "
                print "  | |   ,'      | | "
                print "  |_|,'_________|_| "
                print "You successfully open the door, which now leads to the next room."
                print "You enter the next room."
            elif usbDecision.upper() == "B" or usbDecision.upper() == "NO":
                print "You return to the beginning intersecton."
                routes()
            else:
                print "That is not a valid option."
                door()
        else:
            print "You return to the beginning intersection."
            routes()
    else:
        print "The ship still seems to have problems."
        print "You return to the beginning intersection."
        routes()
    
def cabinets():
    print "   __________    __________    __________  "
    print "  |  __  __  |  |  __  __  |  |  __  __  | "
    print "  | |  ||  | |  | |  ||  | |  | |  ||  | | "
    print "  | |__||__| |  | |__||__| |  | |__||__| | "
    print "  |  __  __(1)  |  __  __(2)  |  __  __(3) "
    print "  | |  ||  | |  | |  ||  | |  | |  ||  | | "
    print "  | |  ||  | |  | |  ||  | |  | |  ||  | | "
    print "  | |__||__| |  | |__||__| |  | |__||__| | "
    print "  |__________|  |__________|  |__________| " 
    print "There seems to be a set of three cabinets in front of you."
    cabDecision = raw_input("Would you like to examine the cabinets A)Yes B)No : ")
    if cabDecision.upper() == "A" or cabDecision.upper() == "YES":
        cabNumDecision = raw_input("Which cabinet would you like to open A)Cabinet 1 B)Cabinet 2 C)Cabinet 3 : ")
        if cabNumDecision.upper() == "A" or cabNumDecision.upper() == "CABINET 1":
            if "CD" in backpack:
                print "There is nothing in Cabinet 1."
                cabinets()
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
                        cabinets()
                    else:
                        backpack.append("CD")
                        print "The CD has been added to your backpack."
                        cabinets()
                elif cdDecision.upper() == "B" or cdDecision.upper() == "NO":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision.upper() == "B" or cabNumDecision.upper() == "CABINET 2":
            if "keycard" in backpack:
                print "There is nothing in Cabinet 2."
                cabinets()
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
                        cabinets()
                    else:
                        backpack.append("keycard")
                        print "The keycard has been added to your backpack."
                        cabinets()
                elif kcDecision.upper() == "B" or kcDecision.upper() == "NO":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision.upper() == "C" or cabNumDecision.upper() == "CABINET 3":
            if "USB" in backpack:
                print "There is nothing in Cabinet 3."
                cabinets()
            else:
                print "   _   ,--()"
                print "  ( )-'-.------|>"
                print "   -     `--[]"
                print "There seems to be a USB in Cabinet 3."
                usbbDecision = raw_input("Would you like to put the USB into your backpack A)Yes B)No: ")
                if usbbDecision.upper() == "A" or usbbDecision.upper() == "YES":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("USB")
                        print "The USB has been added to your backpack."
                        cabinets()
                elif usbbDecision.upper() == "B" or usbbDecision.upper() == "NO":
                        cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        else:
            print "That is not a valid option."
            cabinets()
    elif cabDecision.upper() == "B" or cabDecision.upper() == "NO":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        cabinets()
        
routes()