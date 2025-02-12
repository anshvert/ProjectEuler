from meth import *

n = 2000000
sm = 0
for prime in Sieve(n):
    sm += prime
print(sm)