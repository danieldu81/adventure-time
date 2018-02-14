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
    decision = raw_input("Would you like to go to the room's control, door, or cabinets? ")
    if decision == "control":
        control()
    elif decision == "door":
        door()
    elif decision == "cabinets":
        cabinets()
    else:
        print "That is not a valid option."
        routes()
    
def control():
    print "There seems to be a computer and the ship's engine in front of you."
    decision = raw_input("Would you like to check the computer and engine out? ")
    if decision == "yes":
        decision2 = raw_input("Which one would you like to access? ")
        if decision2 == "computer":
            print "The computer has been accessed."
            if password == True:  
                print "The computer looks very interesting."
                control()
            else:
                print "The computer screen seems to require a password."
                while password == False:
                    decision3 = raw_input("Enter a password. ")
                    if decision3 == "ketchup":
                        print "That is the correct password."
                        print "The computer's error has been fixed."
                        global password
                        password = True
                        control()
                    else:
                        print "Sorry, that is incorrect."
                        control()
        elif decision2 == "engine":
            if password == False:
                print "The engine cannot be fixed without accessing the computer first."
                control()
            else:
                print "The engine seems to require a welder to fix it."
                if "welder" in backpack:
                    print "You seem to have a welder in your backpack."
                    decision3 = raw_input("Would you like to use it on the engine? ")
                    if decision3 == "yes":
                        print "The ship's engine has been fixed."
                        global engine
                        engine = True
                        control()
                    else:
                        control()
                else:
                    control()
        else:
            print "That is not a valid option."
            control()
    else:
        print "You return to the beginning intersection."
        routes()
    
def door():
    print "The door to the next room lies in front of you."
    if engine == True and password == True:
        print "There seems to be a loose bolt in the door that requires a wrench."
        if "wrench" in backpack:
            decision = raw_input("Would you like to use your wrench to fix the loose bolt? ")
            if decision == "yes":
                print "You successfully fix the door, which now opens to the next room."
                print "You enter the next room."
            else:
                print "You return to the beginning intersecton."
                routes()
        else:
            print "You return to the beginning intersection."
            routes()
    else:
        print "The ship still seems to have problems."
        print "You return to the beginning intersection."
        routes()
    
def cabinets():
    print "There seems to be a set of three cabinets in front of you."
    decision = raw_input("Would you like to examine the cabinets? ")
    if decision == "yes":
        decision2 = raw_input("Which cabinet would you like to open (1/2/3)? ")
        if decision2 == "1":
            if "welder" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a welder in the cabinet."
                decision3 = raw_input("Would you like to put the welder into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("welder")
                        print "The welder has been added to your backpack."
                        cabinets()
                else:
                    cabinets()
        elif decision2 == "2":
            if "hammer" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a hammer in the cabinet."
                decision3 = raw_input("Would you like to put the hammer into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("hammer")
                        print "The hammer has been added to your backpack."
                        cabinets()
                else:
                    cabinets()
        elif decision2 == "3":
            if "wrench" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a wrench in the cabinet."
                decision3 = raw_input("Would you like to put the wrench into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("wrench")
                        print "The wrench has been added to your backpack."
                        cabinets()
                else:
                    cabinets()
        else:
            print "That is not a valid option."
            cabinets()
    else:
        print "You return to the beginning intersection."
        routes()
        
routes()