# Solution to Room 7

### problem statement
Solve an encrypted matrix with a randomly generated encoding matrix, e.g.:

```
=== ciphertext ===
1367 1922 1144 1551 2082 1328 1479 1996 1277 1328 1996 1021 1293 1664 1157


=== encoding matrix ===
  7   8   7
  7   9   6
  3   7   1
```

### solution
By hand, this is some basic but tedious arithmetic. If have a graphing
calculator, you can just use that to solve it.

Looking through the source code, the matrices are securely generated and the
plaintext of the password is destroyed immediately after creation, so there's no way to get around having to actually do the math. (Unless you want to do a pre-image attack on SHA-256, which is not recommended.) Perhaps the easiest way to solve this problem, besides using a graphing calculator, is to write a
Python script to solve it:

```python
# use numpy for linear algebra routines
import numpy as np

# define the encoding and encrypted matrices
encoding_matrix = [[7, 8, 7], [7, 9, 6], [3, 7, 1]]
ciphertext = [[1367, 1922, 1144],
              [1551, 2082, 1328],
              [1479, 1996, 1277],
              [1328, 1996, 1021],
              [1293, 1664, 1157]]

# the decoding matrix is just the inverse of the encoding matrix
decoding_matrix = np.linalg.inv(encoding_matrix)

# the plaintext of the password can be found by multiplying the encrypted
# message by the decoding matrix
plaintext = np.dot(ciphertext, decoding_matrix).tolist()

# map the numbers to ASCII characters and print the final result
print ''.join([chr(int(round(c))) for row in plaintext for c in row])
```

This gives us our final answer of `m1WUq7qFB6YmcH`. We can try it with the
command: `guess m1WUq7qFB6YmcH`. 
