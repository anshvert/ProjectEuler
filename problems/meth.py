def Sieve(n):
    if n >= 2:
        yield 2
    sieve = [True] * (n + 1)
    for p in range(3,n + 1, 2):
        if sieve[p]:
            yield p
            for mul in range(p*p, n + 1, 2 * p):
                sieve[mul] = False
