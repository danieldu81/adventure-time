import sys, time
import inventory
import Room3, Room4, Room5, Room7

title_space = r'''
         ___           ___         ___           ___           ___
        /  /\         /  /\       /  /\         /  /\         /  /\
       /  /:/_       /  /::\     /  /::\       /  /:/        /  /:/_
      /  /:/ /\     /  /:/\:\   /  /:/\:\     /  /:/        /  /:/ /\
     /  /:/ /::\   /  /:/~/:/  /  /:/~/::\   /  /:/  ___   /  /:/ /:/_
    /__/:/ /:/\:\ /__/:/ /:/  /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/ /\
    \  \:\/:/~/:/ \  \:\/:/   \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:/ /:/
     \  \::/ /:/   \  \::/     \  \::/       \  \:\  /:/   \  \::/ /:/
      \__\/ /:/     \  \:\      \  \:\        \  \:\/:/     \  \:\/:/
        /__/:/       \  \:\      \  \:\        \  \::/       \  \::/
        \__\/         \__\/       \__\/         \__\/         \__\/'''
title_race = r'''
      ___           ___           ___           ___
     /  /\         /  /\         /  /\         /  /\
    /  /::\       /  /::\       /  /:/        /  /:/_
   /  /:/\:\     /  /:/\:\     /  /:/        /  /:/ /\
  /  /:/~/:/    /  /:/~/::\   /  /:/  ___   /  /:/ /:/_
 /__/:/ /:/___ /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/ /\
 \  \:\/:::::/ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:/ /:/
  \  \::/~~~~   \  \::/       \  \:\  /:/   \  \::/ /:/
   \  \:\        \  \:\        \  \:\/:/     \  \:\/:/
    \  \:\        \  \:\        \  \::/       \  \::/
     \__\/         \__\/         \__\/         \__\/'''

title = 'Welcome to Space Race, an interactive text-based video game created by students for students!\n\n'

print title_space
print title_race
print('{:^80s}'.format(title))
print '(This game may or may not be solvable in O(n)...)'

print("Get ready for a FANTASTIC adventure! Your adventure will start in...")
'''for i in xrange(5,0,-1):
    time.sleep(1)
    print i'''

print("\nThe year is 20XX. Your name is Zeev from planet Penseev and currently you are hurtling 65 km/s towards an unknown planet." 
" As one of the few survivors of the human race, it is your responsibility to travel from planet to planet in the hopes of finding a new home for your people."
" However, the ship and its AI JEFF do not know that you have survived, which would cause JEFF to attack you as a foreign entity if it sees you." 
" Clear all of the rooms, defeat JEFF, and escape to the escape pods as fast as you can.\n\n" 
"Now, you have been woken up early from your cryosleep...\n\n")

print '='*80

# setup user variables
inv = inventory.Inventory(max_len=7)

# setup rooms
# for this to work, each room must make available three things:
#   1. a global variable `name' that stores the room's name
#   2. a global function `play()'' that accepts one argument, the universal
#      user inventory main.inv, and handles all of the gameplay for that room
#   3. a global variable `win' that stores whether or not that room's challenge
#      has been completed as a bool
# all gameplay mechanics are left to individual rooms
rooms = [Room3, Room4, Room5, Room7]  # list of rooms
current_room = 0

def to_room():
    # lets the user decide which room to go to
    # returns 1 for next room, 0 for staying in current room, and -1 for prev
    print 'you have left the room'
    print ('would you like to go [n] next room, [p] previous room, or [r] '
           'repeat current room?')
    print 'you can also quit the game with [q]'
    move = ''
    while True:
        # maybe prune this giant if-else tree, but it works for now
        move = raw_input('move [n/p/r/q] => ').lower()
        if move == 'n':
            if rooms[current_room].win:
                if current_room < len(rooms)-1:
                    return 1
                else:
                    print 'you have already reached the last room'
                    move = ''
            else:
                print ('you cannot enter the next room until you have solved '
                       'the present one')
                move = ''
        elif move == 'p':
            if current_room != 0:
                return -1
            else:
                print 'you area already at the first room'
                move = ''
        elif move == 'r':
            return 0
        elif move == 'q':
            print 'exiting the game...'
            print 'WARNING: your progress will not be saved'
            print 'please come back next time!'
            sys.exit(0)
        else:
            print 'error : command not recognized'

def list_rooms():
    # lists all the rooms and whether they are complete or incomplete
    print 'this is the current state of your game:'
    for i, r in enumerate(rooms):
        status = 'INCOMPLETE'
        if r.win:
            status = 'COMPLETE'
        current = ''
        if i == current_room:
            current = '<- current room'
        print '%s : %s %s' % (r.name, status, current)

while not Room7.win:
    # user play loop
    rooms[current_room].play(inv)
    list_rooms()
    current_room += to_room()

print 'Thou art victorious!'
print 'Your brave actions have ensured the survival of the human race...'
print '...for the next ten minutes, anyway.'
