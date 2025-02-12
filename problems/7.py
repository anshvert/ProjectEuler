# https://projecteuler.net/problem=7

def prime(num):
    for i in range(3,int(num ** 0.5) + 1,2):
        if num % i == 0:
            return False
    return True

pCount,start,pr = 1,3,None
while pCount < 10001:
    if prime(start):
        pCount += 1
        pr = start
    start += 2

print(pr)
