# Solution to Room 5

### problem statement
Place the masses on the following machine such that it is in equilibrium:

```
//////////////////////////////////////////////////////////////////////
========+=============================================================
        |
       _+_
      / O \
      |   |
    +---+ |                     downward acceleration on this
    | 1 | |                     spaceship:
    +---+ |                         |   g = 10 m/s^2
         _+_                        v
        / O \
        |   |
      +---+ |
      | 2 | |
      +---+ |                    pulleys are assumed to be massless
         ___+___                 strings are also massless
        /   O   \                basically don't overthink it
        |       |
      __+__   +---+
     /  O  \  | 5 |
     |     |  +---+
   +---+ +---+
   | 3 | | 4 |
   +---+ +---+
```

### solution
After admiring the wonderful ASCII art, we see that `m3 = m4`, `m3 + m4 = m5`,
`m3 + m4 + m5 = m2`, and `m2 + m3 + m4 + m5 = m1`. Looking at the room items,
this would work for `m1 = 8 kg`, `m2 = 4 kg`, `m3 = 1 kg`, `m4 = 1 kg`, and
`m5 = 2 kg`. Use the `place` command to place the items like that and then
use the `solve` command to verify your solution!
