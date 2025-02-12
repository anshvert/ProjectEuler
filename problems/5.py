# https://projecteuler.net/problem=5
from math import gcd

def getLCM(s,e):
    lcm = 1
    for i in range(s+1,e+1):
        lcm = lcm * i // gcd(lcm,i)
    return lcm

print(getLCM(1,20))