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
    print "There appears to be three routes that you can take."
    decision = raw_input("Would you like to go to the room's computers, door, or cabinets? ")
    if decision == "computers":
        computers()
    elif decision == "door":
        door()
    elif decision == "cabinets":
        cabinets()
    else:
        print "That is not a valid option."
        routes()
    
def computers():
    print "There seems to be a set of three computers in front of you."
    decision = raw_input("Would you like to examine the computers? ")
    if decision == "yes":
        decision2 = raw_input("Which computer would you like to open (1/2/3)? ")
        if decision2 == "1":
            print "Computer 1 has been opened."
            print "The computer looks very interesting."
            computers()
        elif decision2 == "2":
            print "Computer 2 has been opened."
            print "The computer looks very interesting."
            computers()
        elif decision2 == "3":
            print "Computer 3 has been opened."
            if password == True and message == True:  
                print "The computer looks very interesting."
                computers()
            elif password == True and message == False:
                SOS()
            else:
                print "The computer screen seems to require a password."
                while password == False:
                    decision3 = raw_input("Enter a password. ")
                    if decision3 == "ranch":
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
    elif decision == "no":
        print "You return to the beginning intersecton."
        routes()
    else:
        print "That is not a valid option."
        computers()
        
            
def SOS():
    print "The ship's communication line with nearby ships has been opened."
    print "A keycard is needed to send an SOS message."
    if "keycard" in backpack:
        print "You seem to have a keycard in your backpack."
        decision = raw_input("Would you like to use your keycard to send an SOS message to the ships? ")
        if decision == "yes":
            print "An SOS message has been sent."
            global message
            message = True
            print "The keycard has self-destructed."
            backpack.remove("keycard")
            computers()
        elif decision == "no":
            computers()
        else:
            print "That is not a valid option."
            SOS()
    else:
        computers()
    
def door():
    print "The door to the next room lies in front of you."
    if message == True and password == True:
        print "There seems to be slot in the door that requires a USB."
        if "USB" in backpack:
            decision = raw_input("Would you like to use your USB to open the door? ")
            if decision == "yes":
                print "You successfully open the door, which now leads to the next room."
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
            if "CD" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a CD in the cabinet."
                decision3 = raw_input("Would you like to put the CD into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("CD")
                        print "The CD has been added to your backpack."
                        cabinets()
                else:
                    cabinets()
        elif decision2 == "2":
            if "keycard" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a keycard in the cabinet."
                decision3 = raw_input("Would you like to put the keycard into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("keycard")
                        print "The keycard has been added to your backpack."
                        cabinets()
                else:
                    cabinets()
        elif decision2 == "3":
            if "USB" in backpack:
                print "There is nothing in the cabinet."
                cabinets()
            else:
                print "There seems to be a USB in the cabinet."
                decision3 = raw_input("Would you like to put the USB into your backpack? ")
                if decision3 == "yes":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("USB")
                        print "The USB has been added to your backpack."
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