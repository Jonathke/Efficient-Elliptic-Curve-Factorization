from random import randint

precomp_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def isPrime(n):
    return not MRwitness(n)

def MRwitness(n, k=10):
    if n < 2: return False
    for p in precomp_primes:
        if n % p == 0:
            return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        a = randint(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return a
            if x == n-1:
                break
        else:
            return a
    return 0
