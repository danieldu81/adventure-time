''' Room1.py

This room is completely dark and the player must navigate in the dark till they
find a light source. Afterwords they can find a key and exit the dark room.

'''
import random

# A specified location in room one
class Grid:
    def __init__(self, x, y, item='', description='', interact=True):
        self.x = x
        self.y = y
        self.item = item
        self.description = description
        self.interact = interact

    def as_tuple(self):
        return(self.x, self.y, self.item, self.description, self.interact)

# Class that creates the entire room
class Room:
    def __init__(self):
        self.room = []
    
    def build_room(self):
        for x in range(0,5):
            for y in range(0,5):
                if x==4 and y==0: # Location of the cryo chamber
                    temp = Grid(x, y, "Cryo Chamber", "You can see blue liquid inside the cryo chamber.", False)
                    self.room.append(temp.as_tuple())
                elif x==2 and y==2: # Location of the table
                    temp = Grid(x, y, "Table", "There seems to be a table here.", False)
                    self.room.append(temp.as_tuple())
                elif x==0 and y==1: # Location of the key
                    temp = Grid(x, y, "Key", "On the wall there hangs a key.")
                    self.room.append(temp.as_tuple())
                elif x==4 and y==3: # Location of the Glowstick
                    temp = Grid(x, y, "Glowstick", "There seems to be a glowstick on the floor.")
                    self.room.append(temp.as_tuple())
                elif x==3 and y==0: # Location of the door
                    temp = Grid(x, y, "Door", "There is a door in front of you.")
                    self.room.append(temp.as_tuple())   
                else: # Empty space
                    temp = Grid(x, y)
                    self.room.append(temp.as_tuple())

    def find_location(self, x, y): # Finds current location and item stored there (if any)
        for item in self.room:
            if x==item[0] and y==item[1]:
                return item

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
    elif x>4:
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
    z = -1
    valid = True
    while z!=1 and z!=2 and z!=3 and z!=4:
        z = int(raw_input("Where would you like to go? 1)Up 2)Down 3)Left 4)Right : "))
    if z==1:
        x2, y2 = move_up(x,y)
    if z==2:
        x2, y2 = move_down(x,y)
    if z==3:
        x2, y2 = move_left(x,y)
    if z==4:
        x2, y2 = move_right(x,y)
    
    x2, y2, valid = check_valid(x2, y2)
    return x2, y2, valid

def random_message(): # Prints a random message
    messages = ['You feel someone watching you...', 'The hair on the back of your neck prickles...',
    'Something does not feel right...', 'It is too quiet...', 'You trip and fall!', 'You stub your toe.']
    x = random.randint(0,6)
    print messages[x]

room1 = Room()
room1.build_room()
in_room = True

#print("\n\n")
x = 0
y = 4
valid = True
found = False

while found == False:
    x, y, valid = move(x,y)
    if valid == False:
        print("There is a wall in your way.")
    else:
        current_loc = room1.find_location(x, y)
        if current_loc[2] != '':
            print current_loc[3]
            if x==4 and y==3:
                print("You found glowsticks!")
                break
        else:
            random_message()