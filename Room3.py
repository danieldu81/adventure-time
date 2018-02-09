print "=================================================================================="
print "You have entered the engine room."
print "In order to redirect the ship away from the incoming asteroid, you must diagnose"
print "the issue with the engine and access the computer that houses the error."
print "=================================================================================="

passwords = "ketchup, mustard, ranch"
backpack = []

print "There appears to be three routes that you can take."

def initDecision():
    decision = raw_input("Would you like to go left, straight, or right?")
    if decision == "left":
        initLeft();
    elif decision == "straight":
        initStraight();
    elif decision == "right":
        initRight();
    else:
        print "That is not a valid option"
    
def initLeft():
    print "There seems to be a computer and the ship's engine in front of you."
    decision = raw_input("Would you check the computer and engine out?")
    if decision == "yes":
        decision2 = raw_input("Which one would you like to access first?")
        if decision2 == "computer":
            print "The computer screen seems to require a password"
            while password == false:
                decision3 = raw_input("Enter a password")
                if decision3 == "ketchup":
                    password = true
                else:
                    print "Sorry, that is incorrect"
        elif decision2 == "engine":
            
        else: 
            initLeft()
    else:
        "You return to the beginning intersection"
    
def initStraight():
    print "The door to the next room lies in front of you."
    print "There seems to be a loose bolt in the door."
    if "wrench" in backpack:
        decision = raw_input("Would you like to use your wrench to fix the loose bolt?")
        if decision == "yes":
            print "You successfully fix the door, which now opens to the next room."
            print "You enter the next room."
        else:
            "You return to the beginning intersecton"
    
def initRight():
    print "There seems to be a set of three cabinets in front of you."
    decision = raw_input("Would you like to examine the cabinets?"
        if decision == "yes":
            decision2 = raw_input("Which cabinet would you like to open (1/2/3)?"
                if decision == "1":
                    print "There seems to be a welder in the cabinet."
                    decision3 = raw_input("Would you like to put the welder into your backpack?"
                    if decision3 == "yes":
                        backpack.append("welder")
                    else:
                        initRight()
                elif decision == "2":
                    print "There seems to be a hammer in the cabinet."
                    decision3 = raw_input("Would you like to put the hammer into your backpack?"
                    if decision3 == "yes":
                        backpack.append("hammer")
                    else:
                        initRight()
                else:
                    print "There seems to be a wrench in the cabinet."
                    decision3 = raw_input("Would you like to put the wrench into your backpack?"
                    if decision3 == "yes":
                        backpack.append("wrench")
                    else:
                        initRight()
        else:
            "You return to the beginning intersection"