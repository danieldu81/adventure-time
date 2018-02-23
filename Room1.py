''' Room1.py

This room is completely dark and the player must navigate in the dark till they
find a light source. Afterwords they can find a key and exit the dark room.

'''
import random, inventory

name = 'room 1'
win = False

# Class that creates the entire room
class Room:
    def __init__(self):
        self.room = []
    
    def build_room(self):
        for x in range(0,3):
            for y in range(0,5):
                if x==0 and y==4: # Location of the cryo chamber
                    temp = [x, y, "Cryo Chamber", "You can see blue liquid inside the cryo chamber.", False]
                    self.room.append(temp)
                elif x==1 and y==2: # Location of the table
                    temp = [x, y, "Table", "There seems to be a table here.", False]
                    self.room.append(temp)
                elif x==0 and y==1: # Location of the key
                    temp = [x, y, "Key", "There seems to be something on the wall...", True]
                    self.room.append(temp)
                elif x==2 and y==3: # Location of the Glowstick
                    temp = [x, y, "Glowstick", "There seems to be a glowstick on the floor.", True]
                    self.room.append(temp)
                elif x==1 and y==0: # Location of the door
                    temp = [x, y, "Door", "There seems to be a door in front of you.", True]
                    self.room.append(temp)   
                else: # Empty space
                    temp = [x, y, '', '', True]
                    self.room.append(temp)
    def light_up(self):
        self.room[4][3] = 'The blue cryo gel shifts and rotates. It is very mesmerizing...'
        self.room[7][3] = 'There is a metal table bolted to the floor. The table is clean.'
        self.room[1][3] = 'You look up and see a key hanging on the wall.'
        self.room[13][3] = ''
        self.room[5][3] = 'There is a sliding door that seems to require a key to open...'
    
    def update(self):
        self.room[1][3] = ''
        self.room[5][3] = 'You stand before the door.'

    def find_location(self, x, y): # Finds current location and item stored there (if any)
        for item in self.room:
            if x==item[0] and y==item[1]:
                return item
    
    def print_map(self, x, y):
        grid = ''
        for y2 in range(0, 5):
            grid = grid + '+---+---+---+\n|'
            for x2 in range(0,3):
                if (x==x2 and y==4-y2):
                    grid = grid + ' X |'
                else:
                    grid = grid + '   |'
            grid = grid + "\n"
        grid = grid + '+---+\ /+---+'
        print(grid)
        
    def print_room(self): # Prints the room (Debugging)
        for item in self.room:
            print item

def move_right(x,y): # Moves the character right
    return x+1, y

def move_left(x,y): # Moves the character left
    return x-1, y

def move_up(x,y): # Moves the character up
    return x, y+1

def move_down(x,y): # Moves the character down
    return x, y-1

def check_valid(x,y): # Checks to see if the move is valid
    if x<0:
        return x+1, y, False
    elif x>2:
        return x-1, y, False
    elif y>4:
        return x, y-1, False
    elif y<0:
        return x, y+1, False
    else:
        return x, y, True

def move(x,y): # Allows the user to choose where they move to
    x2 = -1
    y2 = -1
    z = ''
    valid = True
    while z!='w' and z!='a' and z!='s' and z!='d' and z!= '?' and z!= 'm':
        z = raw_input("Where would you like to go? Use WASD to navigate through the room : ")
        z = z.lower()
    if z=='w':
        x2, y2 = move_up(x,y)
        x2, y2, valid = check_valid(x2, y2)
        return x2, y2, valid
    if z=='s':
        x2, y2 = move_down(x,y)
        x2, y2, valid = check_valid(x2, y2)
        return x2, y2, valid
    if z=='a':
        x2, y2 = move_left(x,y)
        x2, y2, valid = check_valid(x2, y2)
        return x2, y2, valid
    if z=='d':
        x2, y2 = move_right(x,y)
        x2, y2, valid = check_valid(x2, y2)
        return x2, y2, valid
    if z =='?':
        print_help()
        return x, y, True
    if z =='m' and glowFound == True:
        room1.print_map(x, y)
        return x, y, True    
    else:
        print("You currently do not have access to this feature.")
        return x, y, True
    
def dark_messages(): # Prints a random message before obtaining glowsticks
    messages = ['You feel someone watching you...', 'The hair on the back of your neck prickles...',
    'Something does not feel right...', 'It is too quiet...', 'You trip and fall!', 'You stub your toe.']
    x = random.randint(0,5)
    print messages[x]

def light_messages(): # Prints a random message when you have glowsticks
    messages = ['Time is a-ticking...', 'The room looks so much better in the light!']
    x = random.randint(0,1)
    print messages[x]

def print_help():
    print 'Help'

global room1
room1 = Room()
room1.build_room()
in_room = True

#print("\n\n")
x = 0
y = 4
valid = True
global glowFound
glowFound = False
keyFound = False
doorFound = False

print('You come to screaming about your Mommy, enclosed in a blanket of solid cryogenic gel. With a start you remember who and where you are,' + 
        '\nand you begin to wonder why you were woken up. With a quiet *hiss* the cryogenic chamber opens up and you stumble to the ground. Your' + 
        '\nvision blurs and as you struggle to stand up, you notice that the ship is entirely silent. After a few minutes your vision clears and' + 
        '\nyour legs stop feeling like jelly. A feeling of dread encompasses you and you look around, but the room is enshrouded in darkness. With' +
        '\na start you realize that something has gone terribly wrong. Before you can panic, your training kicks in. The first thing you need to do' +
        '\nis to find a light so you can make your next move...\n')

while glowFound == False:
    x, y, valid = move(x,y)
    if valid == False:
        print("There is a wall in your way.")
    else:
        current_loc = room1.find_location(x, y)
        if current_loc[2] != '':
            print current_loc[3]
            if x==2 and y==3:
                glowFound = True
        else:
            dark_messages()
print(' ____________________________\n(_(_________________________()')
print('Hooray you found the glowstick!! \n\nThe room is lit up with an eerie green glow. At the other end of the room you see something hanging on the wall. You also see a door on' + 
        '\none side of the room.') 
               
while keyFound == False:
    room1.light_up()
    x, y, valid = move(x,y)
    if valid == False:
        print("There is a wall in your way.")
    else:
        current_loc = room1.find_location(x, y)
        if current_loc[2] != '':
            print current_loc[3]
            if x==0 and y==1:
                keyFound = True
        else:
            light_messages()
            
print(' _____________' + 
   '\n/      _      \\' + 
   '\n[] :: (_) :: []' +
   '\n[] ::::::::: []' +
   '\n[] ::::::::: []' + 
   '\n[] ::::::::: []' +
   '\n[] ::::::::: []' +
   '\n[_____________]' +
   '\n    I     I' +
   '\n    I_   _I' +
   '\n     /   \\' +
   '\n     \   /' +
   '\n     (   )' +
   '\n     /   \\' + 
   '\n     \___/')
print('Hooray you found the key!! Head to the door to move on to the next room!')
 
while doorFound == False:
    room1.update()
    x, y, valid = move(x,y)
    if valid == False:
        print("There is a wall in your way.")
    else:
        current_loc = room1.find_location(x, y)
        if current_loc[2] != '':
            print current_loc[3]
            if x==1 and y==0:
                doorFound = True
        else:
            light_messages()
print("           .-----.----.-----. " +    
      "\n          / /-.| |////| |.-\ \\" + 
      "\n         / /|_|| |////| ||_|\ \\" + 
      "\n        /  :   : |////| :   :  \\" +
      "\n       /  /___:  |////|  :___\  \\" +
      "\n      /   :   |_ |////| _|   :___\\" +   
      "\n     /   /    |_||////||_|    \   \\" +    
      "\n    /    :    |_||////||_|    :    \\" +
     "\n   /____/____ |_||////||_| ____\____\\" + 
    "\n  /     :    |   |////|   |    :     \\" +
   "\n /     /     | _ |////| _ |     \     \\" +
   "\n \     :     || ||////|| ||     :     /" +
    "\n  \   /    .'-\ ||////|| /-`.    \   /" +
    "\n   '-'---------'-'----'-'---------'-'")
print("Congratulations on completing the first room!")