import hashlib

print "===================================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must enter the correct password"
print "into the computer and then change the current path of the engine."
print "===================================================================================================="

passwords = "ketchup, mustard, ranch"
engine = False
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
    routeDecision = raw_input("Would you like to go to the room's A)control B)door C)cabinets : ")
    if routeDecision.upper() == "A" or routeDecision.upper() == "CONTROL":
        control()
    elif routeDecision.upper() == "B" or routeDecision.upper() == "DOOR":
        door()
    elif routeDecision.upper() == "C" or routeDecision.upper() == "CABINETS":
        cabinets()
    else:
        print "That is not a valid option."
        routes()

def control():
    print "   _______________            _________    " 
    print "  |  ___________  |          /         /   "
    print "  | |           | |         /_________/ |  "
    print "  | |           | |         |         | |  "   
    print "  | |           | |         | |====|  | |  "    
    print "  | |           | |         |         | |  "  
    print "  | |___     ___| |         | |====|  | |  "  
    print "  |_____|\_/|_____|         |   ___   | |  "  
    print "    _|__|/ \|__|_           |  |ENG|  | |  "
    print "   / *********** \          |   ---   | |  "     
    print " /  *************  \        |         | |  "    
    print "---------------------       |_________|/   " 
    print "There seems to be a computer and the ship's engine in front of you."
    comEngDecision = raw_input("Would you like to check the computer and engine out A)Yes B)No : ")
    if comEngDecision.upper() == "A" or comEngDecision.upper() == "YES":
        accDecision = raw_input("Which one would you like to access A)computer B)engine : ")
        if accDecision.upper() == "A" or accDecision.upper() == "COMPUTER":
            print "The computer has been accessed."
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
                control()
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
                        global password
                        password = True
                        control()
                    else:
                        print "Sorry, that is incorrect."
                        control()
        elif accDecision.upper() == "B" or accDecision.upper() == "ENGINE":
            if password == False:
                print "The engine cannot be fixed without accessing the computer first."
                control()
            else:
                print "  _________    " 
                print " /         /   "
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
                    print "    .-------------.     "
                    print "   /             / |    "
                    print "  /+============+\ |    "
                    print "  ||            || |    "
                    print "  ||            || |    " 
                    print "  ||            ||/@@@  "  
                    print "  \+============+/    @ " 
                    print "                     @  "
                    print "                    @   "
                    print "You seem to have a welder in your backpack."
                    engDecision = raw_input("Would you like to use it on the engine A)Yes B)No : ")
                    if engDecision.upper() == "A" or engDecision.upper() == "YES":
                        print "The ship's engine has been fixed."
                        global engine
                        engine = True
                        control()
                    elif engDecision.upper() == "B" or engDecision.upper() == "NO":
                        control()
                    else:
                        print "That is not a valid option."
                        control()
                else:
                    control()
        else:
            print "That is not a valid option."
            control()
    elif comEngDecision.upper() == "B" or comEngDecision.upper() == "NO":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        control()
    
def door():
    print "The door to the next room lies in front of you."
    if engine == True and password == True:
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
        print "There seems to be a loose bolt in the door that requires a wrench." 
        if "wrench" in backpack:
            boltDecision = raw_input("Would you like to use your wrench to fix the loose bolt A)Yes B)No : ")
            print " .----.                                .---.   "
            print "'---,  `.____________________________.'  _  `. "
            print "     )   ____________________________   <_>  : "
            print ".---'  .'                            `.     .' "
            print " `----'                                `---'   "  
            if boltDecision.upper() == "A" or boltDecision.upper() == "YES":
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
                print "You successfully fix the door, which now opens to the next room."
                print "You enter the next room."                
            elif boltDecision.upper() == "B" or boltDecision.upper() == "NO":
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
    cabinetsDecision = raw_input("Would you like to examine the cabinets A)Yes B)No : ")
    if cabinetsDecision.upper() == "A" or cabinetsDecision.upper() == "YES":
        cabNumDecision = raw_input("Which cabinet would you like to open A)Cabinet 1 B)Cabinet 2 C)Cabinet 3 : ")
        if cabNumDecision.upper() == "A" or cabNumDecision.upper() == "CABINET 1":
            if "welder" in backpack:
                print "There is nothing in Cabinet 1."
                cabinets()
            else:
                print "    .-------------.     "
                print "   /             / |    "
                print "  /+============+\ |    "
                print "  ||            || |    "
                print "  ||            || |    " 
                print "  ||            ||/@@@  "  
                print "  \+============+/    @ " 
                print "                     @  "
                print "                    @   "
                print "There seems to be a welder in Cabinet 1."
                welderDecision = raw_input("Would you like to put the welder into your backpack A)Yes B)No ")
                if welderDecision.upper() == "A" or welderDecision.upper() == "YES":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("welder")
                        print "The welder has been added to your backpack."
                        cabinets()
                elif welderDecision.upper() == "B" or welderDecision.upper() == "NO":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision.upper() == "B" or cabNumDecision.upper() == "CABINET 2":
            if "hammer" in backpack:
                print "There is nothing in Cabinet 2."
                cabinets()
            else:
                print "                           \`.  "  
                print " .--------------.___________) \ "
                print " |//////////////|___________[ ] "
                print " `--------------'           ) ( " 
                print "                            '-' "
                print "There seems to be a hammer in Cabinet 2."   
                hammerDecision = raw_input("Would you like to put the hammer into your backpack A)Yes B)No : ")
                if hammerDecision.upper() == "A" or hammerDecision.upper() == "YES":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("hammer")
                        print "The hammer has been added to your backpack."
                        cabinets()
                elif hammerDecision.upper() == "B" or hammerDecision.upper() == "NO":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision.upper() == "C" or cabNumDecision.upper() == "CABINET 3":
            if "wrench" in backpack:
                print "There is nothing in Cabinet 3."
                cabinets()
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
                        cabinets()
                    else:
                        backpack.append("wrench")
                        print "The wrench has been added to your backpack."
                        cabinets()
                elif wrenchDecision.upper() == "B" or wrenchDecision.upper() == "NO":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        else:
            print "That is not a valid option."
            cabinets()
    elif cabinetsDecision.upper() == "B" or cabinetsDecision.upper() == "NO":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        cabinets()
        
routes()