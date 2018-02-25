import inventory    # probably not strictly needed
import random       # randomize each password to make it un-guessable
import numpy as np  # matrix math
import string       # generate a random password for each session
import hashlib      # for extra security, don't pass around password plaintext

name = 'room 7'
win = False

inv = inventory.Inventory()

def print_matrix(mat, rounding=False, squeeze=False):
    # prints a matrix
    # if `rounding' is set, only round to the nearest int when printing
    # if `squeeze' is set, print the entire matrix in one line

    # TODO: automatically find digits in longest number in matrix
    for r in mat:
        for c in r:
            if rounding:
                print '%3d' %c,
            else:
                print '%7.3f' % c,
        if not squeeze:
            print ''
    if squeeze:
        print ''  # compensate by adding a newline at the end

def str2matrix(text, size=3):
    # converts a text string to a matrix with given dimensions
    # uses ASCII encoding
    ret = []
    buf = ''
    for i, c in enumerate(text):
        buf += c
        if i % size == size-1:
            ret += [[ord(a) for a in buf]]
            buf = ''
        elif i == len(text)-1:  # pad the end of the string with spaces
            ret += [[ord(a) for a in buf] + [ord(' ')]*(size-(len(text)%size))]
    return ret

def gen_enc_matrix(n_rows=3, n_cols=3, max_num=10):
    # generates a random encoding matrix with the numbers provided
    # in theory, n_rows == n_cols for the encoding to work

    # returns the encoding matrix on success
    # returns a [[-1]] matrix on failure
    err_val = [[-1]]
    if n_rows != n_cols:
        return err_val

    rng = random.SystemRandom()  # more cryptographically secure
    m_invertible = False
    while not m_invertible:
        ret = []
        for r in range(0, n_rows):
            tmp = []
            for c in range(0, n_cols):
                tmp += [rng.randint(0, max_num)]
            ret += [tmp]
        try:
            np.linalg.inv(ret)
            m_invertible = True
        except:
            pass
    return ret  # this could be in the loop, but is here for clarity

def init_problem(pword_len=14, m_size=3):
    # generates a random problem
    # accepts two optional arguments:
    #   pword_len: the length of the password
    #   m_size: the size of the [square] encoding matrix to use
    #           m_size=3 is recommended if you want it to be solvable by hand
    # returns the problem as a tuple:
    #   (
    #       sha256 hash of password,
    #       encoded matrix,
    #       encoding matrix
    #   )
    enc_m = gen_enc_matrix(n_rows=m_size, n_cols=m_size)
    rng = random.SystemRandom()
    password = ''.join([rng.choice(string.ascii_letters + string.digits)
                       for _ in range(pword_len)])
    ciphertext = np.dot(str2matrix(password, size=m_size), enc_m).tolist()
    return (hashlib.sha256(password).hexdigest(), ciphertext, enc_m)

def solve_problem(ciphertext, enc_m):
    # finds the solution to the encryption problem
    # this is not made available to the user, but exists for easier debugging
    # returns the decrypted password on success and empty string on failure
    # failure should never occur on a well-crafted problem
    try:
        dec_m = np.linalg.inv(enc_m).tolist()
        plaintext = np.dot(ciphertext, dec_m).tolist()
        return ''.join([chr(int(round(c))) for row in plaintext for c in row])
    except:
        return ''

def check_sol(guess, real_pword_hash):
    # checks if a given solution is correct
    if hashlib.sha256(guess.strip()).hexdigest() == real_pword_hash:
        print 'Success!'
        global win
        win = True
    else:
        print 'Nope.'

def err(text):
    print 'room7 : error : %s' % text

def leave():
    pass

# function to display commands in order to help user understand how to use
# program
def help(h=False, f=None):
    if h:
        print 'Help entry for: '+f
        print '  ? - the help function'
        print '      can be invoked alone to display available commands'
        print '      can be invoked after a function for contextual help'
        print '  examples'
        print '      ?'
        print '      guess?'
        return
    print 'Available commands:' # print each command in usr_dict
    for key in usr_dict:
        print '  '+key

usr_dict = {
    'q': leave,
    'guess': check_sol,
    '?': help
}

def play(global_inv):
    global inv
    inv = global_inv

    # say hello and be nice to user
    print 'Welcome to room 7!\n'
    print ('You have reached the [escape] pod bay doors. Unfortunately, you '
            'just destroyed the AI, so there is no one to open the door. '
            'Luckily, you recognize the encryption on the door...the password '
            'is encrypted as a matrix, and you know the encoding matrix! '
            'Invert the matrix to find the password and escape the spaceship!')
    print '\nHint: The character encoding is ASCII.'
    print '      You can make a guess by supplying your guess to the \'guess\''
    print '        command.'
    print 'Okay, I guess you can use a TI-nspire if you REALLY want...\n'

    # randomly and securely generate the problem
    pword_hash, ciphertext, enc_m = init_problem(pword_len=14, m_size=3)
    print 'The problem is as follows:'
    print '=== ciphertext ==='
    print_matrix(ciphertext, rounding=True, squeeze=True)
    print ''
    print '=== encoding matrix ==='
    print_matrix(enc_m, rounding=True)

    # for debugging
    # sol = solve_problem(ciphertext, enc_m)
    # print sol

    # user input loop
    cmd = ''
    while cmd not in ['q']:
        cmd = raw_input('room 7 => ')
        try:
            usr_dict[cmd]()
        except:
            try:
                # is command `guess <pass>'?
                a, b = cmd.strip().split(' ')
                usr_dict[a](b, pword_hash)
            except:
                err('command not recognized')
    return win

if __name__ == '__main__':
    play(inventory.Inventory())
