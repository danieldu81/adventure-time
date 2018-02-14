print "=================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must enter the"
print "correct password into the computer and then change the current path of the engine."
print "=================================================================================="

passwords = "ketchup, mustard, ranch"
engine = False
password = False
backpack = []

def routes():
    print "There appears to be three routes that you can take."
    routeDecision = raw_input("Would you like to go to the room's A)control B)door C)cabinets : ")
    if routeDecision == "A":
        control()
    elif routeDecision == "B":
        door()
    elif routeDecision == "C":
        cabinets()
    else:
        print "That is not a valid option."
        routes()
    
def control():
    print "There seems to be a computer and the ship's engine in front of you."
    comEngDecision = raw_input("Would you like to check the computer and engine out A)Yes B)No : ")
    if comEngDecision == "A":
        accDecision = raw_input("Which one would you like to access A)computer B)engine : ")
        if accDecision == "A":
            print "The computer has been accessed."
            if password == True:  
                print "The computer looks very interesting."
                control()
            else:
                print "The computer screen seems to require a password."
                while password == False:
                    passDecision = raw_input("Enter a password : ")
                    if passDecision == "ketchup":
                        print "That is the correct password."
                        print "The computer's error has been fixed."
                        global password
                        password = True
                        control()
                    else:
                        print "Sorry, that is incorrect."
                        control()
        elif accDecision == "B":
            if password == False:
                print "The engine cannot be fixed without accessing the computer first."
                control()
            else:
                print "The engine seems to require a welder to fix it."
                if "welder" in backpack:
                    print "You seem to have a welder in your backpack."
                    engDecision = raw_input("Would you like to use it on the engine A)Yes B)No : ")
                    if engDecision == "A":
                        print "The ship's engine has been fixed."
                        global engine
                        engine = True
                        control()
                    elif engDecision == "B":
                        control()
                    else:
                        print "That is not a valid option."
                        control()
                else:
                    control()
        else:
            print "That is not a valid option."
            control()
    elif comEngDecision == "B":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        control()
    
def door():
    print "The door to the next room lies in front of you."
    if engine == True and password == True:
        print "There seems to be a loose bolt in the door that requires a wrench."
        if "wrench" in backpack:
            boltDecision = raw_input("Would you like to use your wrench to fix the loose bolt A)Yes B)No : ")
            if boltDecision == "A":
                print "You successfully fix the door, which now opens to the next room."
                print "You enter the next room."
            elif boltDecision == "B":
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
    print "There seems to be a set of three cabinets in front of you."
    cabinetsDecision = raw_input("Would you like to examine the cabinets A)Yes B)No : ")
    if cabinetsDecision == "A":
        cabNumDecision = raw_input("Which cabinet would you like to open A)Cabinet 1 B)Cabinet 2 C)Cabinet 3 : ")
        if cabNumDecision == "A":
            if "welder" in backpack:
                print "There is nothing in Cabinet 1."
                cabinets()
            else:
                print "There seems to be a welder in Cabinet 1."
                welderDecision = raw_input("Would you like to put the welder into your backpack A)Yes B)No ")
                if welderDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("welder")
                        print "The welder has been added to your backpack."
                        cabinets()
                elif welderDecision == "B":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision == "B":
            if "hammer" in backpack:
                print "There is nothing in Cabinet 2."
                cabinets()
            else:
                print "There seems to be a hammer in Cabinet 2."
                hammerDecision = raw_input("Would you like to put the hammer into your backpack A)Yes B)No : ")
                if hammerDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("hammer")
                        print "The hammer has been added to your backpack."
                        cabinets()
                elif hammerDecision == "B":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision == "C":
            if "wrench" in backpack:
                print "There is nothing in Cabinet 3."
                cabinets()
            else:
                print "There seems to be a wrench in Cabinet 3."
                wrenchDecision = raw_input("Would you like to put the wrench into your backpack A)Yes B)No : ")
                if wrenchDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("wrench")
                        print "The wrench has been added to your backpack."
                        cabinets()
                elif wrenchDecision == "B":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        else:
            print "That is not a valid option."
            cabinets()
    elif cabinetsDecision == "B":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        cabinets()
        
routes()