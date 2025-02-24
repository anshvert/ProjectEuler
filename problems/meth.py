def Sieve(n):
    if n >= 2:
        yield 2
    sieve = [True] * (n + 1)
    for p in range(3,n + 1, 2):
        if sieve[p]:
            yield p
            for mul in range(p*p, n + 1, 2 * p):
                sieve[mul] = False

def divisors_count(num):
    c = 0
    for i in range(1,int(num**0.5) + 1):
        if num % i == 0:
            if num // i != i:
                c += 2
            else:
                c += 1
    return c