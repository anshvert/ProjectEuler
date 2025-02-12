# https://projecteuler.net/problem=6

def sqSum(s,e):
    return ((e * (e + 1)) // 2) ** 2

def sumSQ(s,e):
    c = 0
    for i in range(s,e+1):
        c += i ** 2
    return c

print(sqSum(1,100) - sumSQ(1,100))