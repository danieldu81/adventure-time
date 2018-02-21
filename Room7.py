import inventory  # probably not strictly needed
import random
import numpy as np  # matrix math

# totally secure matrix encryption!
password = 'Gallia est omnis divisa in partes tres...'
cipher_text = []
encoding_matrix = []

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

def test_matrix():
    enc_m = gen_enc_matrix()
    inv_m = np.linalg.inv(enc_m).tolist()  # should be guaranteed to work
    print '=== encoding matrix is ==='
    print_matrix(enc_m)
    print ''
    print '=== inverted matrix is ==='
    print_matrix(inv_m)
    print ''
    print '=== original message is ==='
    print password
    print ''
    print '=== encrypted message is ==='
    ciphertext = np.dot(str2matrix(password), enc_m).tolist()
    print_matrix(ciphertext, rounding=True, squeeze=True)
    print ''
    print '=== multiplying by inv yields ==='
    decrypted = np.dot(ciphertext, inv_m).tolist()
    print_matrix(decrypted, rounding=True)
    print ''
    print '=== this maps to ASCII letters ==='
    print ''.join([chr(int(round(a))) for b in decrypted for a in b])

def err(text):
    print 'room7 : error : %s' % text

def play():
    # say hello and be nice to user
    print 'Welcome to room 7!\n'
    print ('You have reached the [escape] pod bay doors. Unfortunately, you '
            'just destroyed the AI, so there is no one to open the door. '
            'Luckily, you recognize the encryption on the door...the password '
            'is encrypted as a matrix, and you know the encoding matrix! '
            'Invert the matrix to find the password and escape the spaceship!')
    print '\nHint: The character encoding is ASCII'
    print 'Okay, I guess you can use a TI-nspire if you REALLY want...'
    
    # user input loop
    cmd = ''
    while cmd not in ['quit', 'leave', 'exit', 'q', 'X']:
        cmd = raw_input('room 7 => ')

if __name__ == '__main__':
    test_matrix()
    #play()