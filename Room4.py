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
    routeDecision = raw_input("Would you like to go to the room's A)computers B)door C)cabinets : ")
    if routeDecision == "A":
        computers()
    elif routeDecision == "B":
        door()
    elif routeDecision == "C":
        cabinets()
    else:
        print "That is not a valid option."
        routes()
    
def computers():
    print "There seems to be a set of three computers in front of you."
    exComDecision = raw_input("Would you like to examine the computers A)Yes B)No : ")
    if exComDecision == "A":
        numComDecision = raw_input("Which computer would you like to open A)Computer 1 B)Computer 2 C)Computer 3 : ")
        if numComDecision == "A":
            print "Computer 1 has been opened."
            print "Computer 1 looks very interesting, but it appears to be broken."
            computers()
        elif numComDecision == "B":
            print "Computer 2 has been opened."
            print "Computer 2 looks very interesting, but it appears to be broken."
            computers()
        elif numComDecision == "C":
            print "Computer 3 has been opened."
            if password == True and message == True:  
                print "Computer 3 looks very interesting."
                computers()
            elif password == True and message == False:
                SOS()
            else:
                print "Computer 3 seems to require a password."
                while password == False:
                    passDecision = raw_input("Enter a password : ")
                    if passDecision == "ranch":
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
    elif exComDecision == "B":
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
        keycardDecision = raw_input("Would you like to use your keycard to send an SOS message to the ships A)Yes B)No : ")
        if keycardDecision == "A":
            print "An SOS message has been sent."
            global message
            message = True
            print "The keycard has self-destructed."
            backpack.remove("keycard")
            computers()
        elif keycardDecision == "B":
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
            usbDecision = raw_input("Would you like to use your USB to open the door A)Yes B)No : ")
            if usbDecision == "A":
                print "You successfully open the door, which now leads to the next room."
                print "You enter the next room."
            elif usbDecision == "B":
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
    cabDecision = raw_input("Would you like to examine the cabinets A)Yes B)No : ")
    if cabDecision == "A":
        cabNumDecision = raw_input("Which cabinet would you like to open A)Cabinet 1 B)Cabinet 2 C)Cabinet 3 : ")
        if cabNumDecision == "A":
            if "CD" in backpack:
                print "There is nothing in Cabinet 1."
                cabinets()
            else:
                print "There seems to be a CD in Cabinet 1."
                cdDecision = raw_input("Would you like to put the CD into your backpack A)Yes B)No : ")
                if cdDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("CD")
                        print "The CD has been added to your backpack."
                        cabinets()
                elif cdDecision == "B":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision == "B":
            if "keycard" in backpack:
                print "There is nothing in Cabinet 2."
                cabinets()
            else:
                print "There seems to be a keycard in Cabinet 2."
                kcDecision = raw_input("Would you like to put the keycard into your backpack A)Yes B)No : ")
                if kcDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("keycard")
                        print "The keycard has been added to your backpack."
                        cabinets()
                elif kcDecision == "B":
                    cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        elif cabNumDecision == "C":
            if "USB" in backpack:
                print "There is nothing in Cabinet 3."
                cabinets()
            else:
                print "There seems to be a USB in Cabinet 3."
                usbbDecision = raw_input("Would you like to put the USB into your backpack A)Yes B)No: ")
                if usbbDecision == "A":
                    if len(backpack) > 5:
                        print "Your backpack seems to be full."
                        cabinets()
                    else:
                        backpack.append("USB")
                        print "The USB has been added to your backpack."
                        cabinets()
                elif usbbDecision == "B":
                        cabinets()
                else:
                    print "That is not a valid option."
                    cabinets()
        else:
            print "That is not a valid option."
            cabinets()
    elif cabDecision == "B":
        print "You return to the beginning intersection."
        routes()
    else:
        print "That is not a valid option."
        cabinets()
        
routes()