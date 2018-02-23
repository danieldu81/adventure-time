''' Room1.py

This room is completely empty except for a massive computer located in the middle of the room. The user will go to the computer and manipulate the code to turn on all lights, run a ship analysis, analyze the ship's logs, and gains passwords for the remainder of the room.

'''

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

def mainframe():
  cmd = ''
  while cmd not in ['quit']:
      cmd = raw_input('admin@solaris: ~$ ').strip() #strip user input of whitespace
      try:
          commands[cmd]() #see if the command is in the dictionary
      except:
          try:
              assert cmd[-1] == '?' #see if command is <func>?
              commands[cmd[:-1]](h=True, f=cmd[:-1])
          except:
              error('Unrecognized input. Try \'?\' for help\n') #show error message for unrecognized input
  print("You shut down the computer. It's probably bad for your eyes anyways.")


def grid(h=False, f=None):
  input = ''
  while input not in ['quit']:
    input = raw_input('admin@solaris:/grid ~$ ').strip() #strip user input of whitespace
    try:
      gridCommands[input]() #see if the command is in the dictionary
      if input == "cd ..":
        mainframe()
    except:
      error('Unrecognized input. Try \'?\' for help\n')

def onGrid(h=False, f=None):
  if lightsOn == False:
    print("Lights are turned on.")
    lightsOn = True
  else:
    print("Lights are already on.")

def listGrid(h=False, f=None):
  for key in gridCommands:
    print '   '+key
  print
  
def helpGrid(h=False, f=None):
  for key in gridDescriptions:
    print '   '+key+"\t\t"+gridDescriptions[key]

def endGrid(h=False, f=None):
  pass
  

def analysis(h=False, f=None):
  print("analysis")

def logs(h=False, f=None):
  print("logs")

def passwords(h=False, f=None):
  print("passwords")

def commands(h=False, f=None):
  for key in commands:
    print '  '+key
  print
  
def quit(h=False, f=None):
  pass
  
def help(h=False, f=None):
  for key in descriptions:
    print '   '+key+"\t\t"+descriptions[key]

def error(text):
  print(text)

  
commands = {'cd grid': grid, 'cd analysis': analysis, 'cd logs': logs, 'cd passwords': passwords, 'quit': quit, '?': help, 'compgen': commands}
descriptions = {'quit   ': 'Quits the program', 'compgen': 'Lists all commands/directories', 'cd passwords': 'Takes you to password directory', 'cd grid': 'Takes you to the power grid directory', 'cd logs': 'Takes you to the logs directory', 'cd analysis': 'Takes you to the analysis directory\n'}

lightsOn = False
gridCommands = {'power on': onGrid, 'cd ..': endGrid, 'compgen': listGrid, '?': helpGrid}
gridDescriptions = {'power on': 'Turns on the lights', 'compgen': 'Lists all commands\n', 'cd ..': 'Go back a directory'}

analysisRun = False
analysisCommands = {}
analysisDescriptions = {}

logsSeen = False
logsCommands = {}
logsDescriptions = {}

passwordsGotten = False
passwordsCommands = {}
passwordsDescrptions = {}

print "\nWelcome to the second room!\n"
print "="*80
print "You make your way to the server room."
print "In front of you is a massive computer that takes up the entirety of the room. At\none end is the door you came through, and at the other is the door out. The\nblinking lights coming from the command console hypnotize you and draw you\ntowards them. You walk towards the console and turn the computer on. With a \npurr, the computer comes to life. However before you can proceed, a password is \nrequired to access the programs written on the computer."
print "="*80
print "\nYou can get help with the \'?\' command. Good luck!"

print("\n\nEnter a valid administrator password: ")
print("\nYou do not know the administrator password. You look around the room and your\neyes glance over a poster on the wall.")
show_password()

password = ''
password = raw_input("Enter a valid administrator password: ")
while(password != 'password'):
  password = raw_input("Invalid. Please enter a valid administrator password: ")

print("The computer comes to life. You seem to recall that typing 'compgen' lists all\nthe possible commands.\n")
mainframe()
