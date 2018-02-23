import sys, time
import inventory
import Room5, Room7

# TODO: fix title sequence to fit within 80 characters
asciiTitle = '         ___           ___         ___           ___           ___                    ___           ___           ___           ___     \n'
asciiTitle += '        /  /\\         /  /\\       /  /\\         /  /\\         /  /\\                  /  /\\         /  /\\         /  /\\         /  /\\    \n'
asciiTitle += '       /  /:/_       /  /::\\     /  /::\\       /  /:/        /  /:/_                /  /::\\       /  /::\\       /  /:/        /  /:/_   \n'
asciiTitle += '      /  /:/ /\\     /  /:/\\:\\   /  /:/\\:\\     /  /:/        /  /:/ /\\              /  /:/\\:\\     /  /:/\\:\\     /  /:/        /  /:/ /\\  \n'
asciiTitle += '     /  /:/ /::\\   /  /:/~/:/  /  /:/~/::\\   /  /:/  ___   /  /:/ /:/_            /  /:/~/:/    /  /:/~/::\\   /  /:/  ___   /  /:/ /:/_ \n'
asciiTitle += '    /__/:/ /:/\\:\\ /__/:/ /:/  /__/:/ /:/\\:\\ /__/:/  /  /\\ /__/:/ /:/ /\\          /__/:/ /:/___ /__/:/ /:/\\:\\ /__/:/  /  /\\ /__/:/ /:/ /\\ \n'
asciiTitle += '    \\  \\:\\/:/~/:/ \\  \\:\\/:/   \\  \\:\\/:/__\\/ \\  \\:\\ /  /:/ \\  \\:\\/:/ /:/          \\  \\:\\/:::::/ \\  \\:\\/:/__\\/ \\  \\:\\ /  /:/ \\  \\:\\/:/ /:/\n'
asciiTitle += '     \\  \\::/ /:/   \\  \\::/     \\  \\::/       \\  \\:\\  /:/   \\  \\::/ /:/            \\  \\::/~~~~   \\  \\::/       \\  \\:\\  /:/   \\  \\::/ /:/ \n'
asciiTitle += '      \\__\\/ /:/     \\  \\:\\      \\  \\:\\        \\  \\:\\/:/     \\  \\:\\/:/              \\  \\:\\        \\  \\:\\        \\  \\:\\/:/     \\  \\:\\/:/  \n'
asciiTitle += '        /__/:/       \\  \\:\\      \\  \\:\\        \\  \\::/       \\  \\::/                \\  \\:\\        \\  \\:\\        \\  \\::/       \\  \\::/   \n'
asciiTitle += '        \\__\\/         \\__\\/       \\__\\/         \\__\\/         \\__\\/                  \\__\\/         \\__\\/         \\__\\/         \\__\\/'

title = 'Welcome to Space Race, an interactive text-based video game created by students for students!\n\n'

print(asciiTitle)
print('{:^140s}'.format(title))

print("Get ready for a FANTASTIC adventure! Your adventure will start in...")
'''for i in xrange(5,0,-1):
    time.sleep(1)
    print i'''

print("\nThe year is 20XX. Your name is Zeev from planet Penseev and currently you are hurtling 65 km/s towards an unknown planet.As\none of the few survivors of the human race, it is your responsibility to travel from planet to planet in the hopes of finding a new\nhome for your people. Unbeknownst to you, the ship has malfunctioned and as a result you have been woken up early from your cryosleep...\n\n")

print('========================================================================================================================================')

# setup user variables
inv = inventory.Inventory()

for i, room in enumerate([Room5, Room7]):
    room.play(inv)
inv.print_inv()
