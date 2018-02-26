''' Room2.py

This room is completely empty except for a massive computer located in the middle of the room. The user will go to the computer and manipulate the code to turn on all lights, run a ship analysis, analyze the ship's logs, and gains passwords for the remainder of the room.

'''
import time, inventory, random

# room metedata for main.py
name = 'room 2'
win = False

# Variables
lightsOn = False
seenOne = False
seenTwo = False
seenThree = False
passwordsGotten = False
data = False
canExit = False

def show_password():
  text = r'''
   ____   ____  _____ _____ __    __   ___   ____   ___
  |    \ /    |/ ___// ___/|  |__|  | /   \ |    \ |   \   __
  |  o  )  o  (   \_(   \_ |  |  |  ||     ||  D  )|    \ |  |
  |   _/|     |\__  |\__  ||  |  |  ||  O  ||    / |  D  ||__|
  |  |  |  _  |/  \ |/  \ ||  `  '  ||     ||    \ |     | __
  |  |  |  |  |\    |\    | \      / |     ||  .  \|     ||  |
  |__|  |__|__| \___| \___|  \_/\_/   \___/ |__|\_||_____||__|

                       ____   ____  _____ _____ __    __   ___   ____   ___
                      |    \ /    |/ ___// ___/|  |__|  | /   \ |    \ |   \
                      |  o  )  o  (   \_(   \_ |  |  |  ||     ||  D  )|    \
                      |   _/|     |\__  |\__  ||  |  |  ||  O  ||    / |  D  |
                      |  |  |  _  |/  \ |/  \ ||  `  '  ||     ||    \ |     |
                      |  |  |  |  |\    |\    | \      / |     ||  .  \|     |
                      |__|  |__|__| \___| \___|  \_/\_/   \___/ |__|\_||_____|
  '''
  print text

def mainframe(): # Function for the main directory of the computer
  cmd = ''
  while cmd not in ['quit']:
      cmd = raw_input('admin@solaris: ~$ ').strip() #strip user input of whitespace
      try:
          if commands[cmd]() == 0:
              return
      except:
          error('Unrecognized input. Try \'?\' for help') #show error message for unrecognized input

def listCommands(h=False, f=None): # Function that lists commands in main directory
  for key in commands:
    print '  '+key

def help(h=False, f=None): # Function that provides help in the main directory
  for key in descriptions:
    print '  '+key+"\t\t"+descriptions[key]


def grid(h=False, f=None): # Function for the grid directory
  input = ''
  while input not in ['quit']:
    input = raw_input('admin@solaris:/grid ~$ ').strip()
    try:
      gridCommands[input]()
      if input == "cd ..":
        return 1
    except:
      error('Unrecognized input. Try \'?\' for help\n')
  return 0

def onGrid(h=False, f=None): # Program that turns on lights
  global lightsOn
  if lightsOn == False:
    print("Lights are turned on.")
    lightsOn = True
  else:
    print("Lights are already on.")

def listGrid(h=False, f=None): # Function that lists commands in the grid directory
  for key in gridCommands:
    print '  '+key

def helpGrid(h=False, f=None): # Function that provides help in the grid directory
  for key in gridDescriptions:
    print '  '+key+"\t\t"+gridDescriptions[key]


def logs(h=False, f=None): # Function for the logs directory
  global seenOne, seenTwo, seenThree, logsSeen
  input = ''
  while input not in ['quit']:
    input = raw_input('admin@solaris:/logs ~$ ').strip()
    try:
      logsCommands[input]()
      if input == "cd ..":
        return 1
    except:
      error('Unrecognized input. Try \'?\' for help')
  return 0

def logOne(h=False, f=None): # Log one document
  global seenOne
  seenOne = True
  log = "Ship's log, 1/1/20XX. The USS Chanas has begun her year long journey towards\nPlanet Joprao located on the far edges of the solar system. With no surviving\npassengers on board, full control has been given to entity JEFF, the\nresiding captain of the ship. JEFF is hoping to land upon Joprao and establish a\ncolony before making contact with the rest of the fleet. End log."
  print log

def logTwo(h=False, f=None): # Log two document
  global seenTwo
  seenTwo = True
  log = "Ship's log, 7/30/20XX. The USS Chanas has just begun superspeed travel.\nConfirmation for superspeed was recieved from the fleet commander at 13:00.\nThere will be no more communication with the fleet until a colony is established\non Joprao. Within the next five months, Planet Joprao will be in sight. End log."
  print log

def logThree(h=False, f=None): # Log three document
  global seenThree
  seenThree = True
  log = "Ship's log, 10/20/20XX. Today was a very exciting day. JEFF discovered a bug in\nthe UPS (Universal Positioning System) code that may have adjusted the course of\nthe ship. The course has been updated after this slight detour. The ship will\nmake the jump to superspeed later in the week. On top of that a rogue entity was\ndiscovered within one of the cryo chambers. JEFF is taking all precautions to\nprevent the entity from damaging the ship. End log."
  print log

def listLogs(h=False, f=None): # Function that lists commands in the logs directory
  for key in logsCommands:
    print '  '+key

def helpLogs(h=False, f=None): # Function that provides help in the logs directory
  for key in logsDescriptions:
    print '  '+key+"\t\t"+logsDescriptions[key]


def passwords(h=False, f=None): # Function for the password directory
  input = ''
  while input not in ['quit']:
    input = raw_input('admin@solaris:/passwords ~$ ').strip()
    try:
      passwordsCommands[input]()
      if input == "cd ..":
        return 1
    except:
      error('Unrecognized input. Try \'?\' for help')
  return 0

def display(h=False, f=None): # Function for passwords file
  global passwordsGotten
  passwords = ['ketchup', 'mustard', 'hotsauce', 'mayo', 'soysauce', 'hotsauce', 'barbequesauce', 'sourcream', 'relish', 'wasabi', 'vinegar', 'chutney', 'salsa', 'sriracha', 'bluecheese']
  random.shuffle(passwords)
  line = ''
  count = 1
  for word in passwords:
    if count == 1 or count == 6 or count == 11:
      line += word
    elif count == 5 or count == 10 or count == 15:
      line += '   ' + word
      print line
      line = ''
    else:
      line += '   ' + word
    count += 1
  passwordsGotten = True

def listPasswords(h=False, f=None): # Function that lists commands in the passwords directory
  for key in passwordsCommands:
    print '  '+key

def helpPasswords(h=False, f=None): # Function that proivdes help in the passwords directory
  for key in passwordsDescriptions:
    print '  '+key+"\t\t"+passwordsDescriptions[key]


def quit(h=False, f=None): # Function that exits the computer
  pass

def back(h=False, f=None): # Function that pushes the user back a directory
  pass

def error(text):
    print(text)

def exitRoom():
    global data
    if data == True:
        print("You get out of the chair and head towards the door. Congratulations on completing room two!")
        return True
    else:
        print("You attempt to get out of the chair, but you cannot seem to.")
        return False

# Dictionaries
commands = {'cd grid': grid, 'cd logs': logs, 'cd passwords': passwords, 'quit': quit, '?': help, 'compgen -b': listCommands}
descriptions = {'quit   ': 'Quits the program', 'compgen -b': 'Lists all commands/directories', 'cd passwords': 'Takes you to password directory\n', 'cd grid': 'Takes you to the power grid directory', 'cd logs': 'Takes you to the logs directory'}

gridCommands = {'power on': onGrid, 'cd ..': back, 'compgen -b': listGrid, '?': helpGrid, 'quit': quit,}
gridDescriptions = {'power on': 'Turns on the lights', 'compgen -b': 'Lists all commands\n', 'cd ..  ': 'Go back a directory', 'quit   ': 'Quits the program'}

logsCommands = {'cat log1': logOne, 'cat log2': logTwo, 'cat log3': logThree, 'cd ..': back, 'compgen -b': listLogs, '?':helpLogs, 'quit': quit,}
logsDescriptions = {'cat log1': 'Log from 1/1/20XX', 'cat log2': 'Log from 7/30/20XX\n', 'cat log3': 'Log from 10/20/20XX', 'compgen -b': 'Lists all commands', 'cd ..  ': 'Go back a directory', 'quit   ': 'Quits the program'}

passwordsCommands = {'show': display, 'cd ..': back, 'compgen -b': listPasswords, '?': helpPasswords, 'quit': quit,}
passwordsDescriptions = {'show   ': 'Displays a list of possible passwords used in the game.\n', 'compgen -b': 'Lists all commands', 'cd ..  ': 'Go back a directory', 'quit   ': 'Quits the program'}

def play(global_inv):
    # This room also does not require the global inventory and if the room has been completed, nothing can be done in this room
    global win
    global data
    if win == True:
        print '\n' + '='*80
        print 'You have already learned everything you can from this room.'
        print 'There is nothing more for you here.'
        print 'Now go in peace'
        print '='*80+'\n'
    else:
        print "\nWelcome to the second room!\n"
        print "="*80
        print "You make your way to the server room."
        print "In front of you is a massive computer that takes up the entirety of the room. At\none end is the door you came through, and at the other is the door out. The\nblinking lights coming from the command console hypnotize you and draw you\ntowards them. You walk towards the console and turn the computer on. With a \npurr, the computer comes to life. However before you can proceed, a password is \nrequired to access the programs written on the computer."
        print "="*80
        print "\nYou can get help with the \'?\' command. Good luck!"

        #time.sleep(10)
        print("\n\nEnter a valid administrator password: ")
        #time.sleep(2.5)
        print("\nYou do not know the administrator password. You look around the room and your\neyes glance over a poster on the wall.")
        #time.sleep(1.5)
        show_password()

        password = ''
        password = raw_input("Enter a valid administrator password: ")
        while(password != 'password'):
            password = raw_input("Invalid. Please enter a valid administrator password: ")

        print("The computer comes to life. You seem to recall that typing 'compgen -b' lists\nall the builtin shell commands.")
        print "N.B. The sysadmin got lazy, so not all standard UNIX commands"
        print "  will work..."
        mainframe()

        if (lightsOn==True and seenOne==True and seenTwo==True and seenThree==True and passwordsGotten==True):
            print("With a start the computer screen goes black. You attempt to turn on the computer,\nbut nothing happens. You sit in silence wondering what your next move is. All of a\bsudden the loudspeaker turns on and a robotic voice says, \"Intruder alert.\nIntruder alert. All foreign objects will be destroyed. Initiating lockdown\nsequence.\"")
            data = True

        while win == False:
            canExit = exitRoom()
            if canExit == True:
                win = True
                break
            else:
                password = ''
                password = raw_input("Enter a valid administrator password: ")
                while(password != 'password'):
                    password = raw_input("Invalid. Please enter a valid administrator password: ")

                print("The computer comes to life. You seem to recall that typing 'compgen -b' lists all\nthe possible commands.")
                mainframe()

                if (lightsOn==True and seenOne==True and seenTwo==True and seenThree==True and passwordsGotten==True):
                    print("With a start the computer screen goes black. You attempt to turn on the computer, but nothing happens. You sit in silence wondering what your next move is. All of a\bsudden the loudspeaker turns on and a robotic voice says, \"Intruder alert. Intruder alert. All foreign objects will be destroyed. Initiating lockdown sequence.\"")
                    data = True

if __name__ == '__main__':
    play(inventory.Inventory())
