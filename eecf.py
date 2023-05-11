from lenstrasAlgorithm import *
from millerRabin import isPrime, precomp_primes
import sys,getopt
from math import floor, ceil

factors = []
primefactors = []

def perfectpower(n):
    n = float(n)
    latest = n
    lowest = None
    i = 2
    while latest > 2:
        if (abs((n**(1/i))-round(n**(1/i))) < 0.0000001):
            if round(n**(1/i))**i == n:
                lowest = [i, round(n**(1/i))]
        latest = n**(1/i)
        i += 1
    return lowest


def factor(n):
    print("    Factoring: " + str(n))
    #check if prime
    if isPrime(n):
        print("        It is prime!")
        return [1, n]
    #check if perfect power
    if not perfectpower(n) == None:
        ret = [0]
        l = perfectpower(n)
        for i in range(l[0]):
            ret.append(l[1])
        return ret
    for p in precomp_primes:
        if n % p ==0:
            print(f"        Divisible by {p}")
            primefactors.append(p)
            return [0, n//p]
    m = lenstra(n)
    return [0, m, n//m]

def nextPrime(r):
    if r % 2 == 0:
        return nextPrime(r+1)
    if isPrime(r):
        return r
    else:
        return nextPrime(r+2)

def random_Nbit(n):
    range_start = 2**(n-1)
    range_end = (2**n)-1
    return randint(range_start, range_end)

def main(argv):
    short_options = "hd:D:n:"
    long_options = ["help", "demo", "number", "demoHARD"]
    global factors
    global primefactors
    try:
        opts, args = getopt.getopt(argv, short_options, long_options)
    except getopt.GetoptError:
        print("Invalid arguments. Run eccf.py -h for usage tips")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("py eecf.py -d (--demo) d: Factor a random number with d bits\n"
                  "py eecf.py -D (--demoHARD) d: Factor a number with d bits, consisting of two primes of [d/2] bits\n"
                  "py eecf.py -n (--number) n: Factor the provided number n\n"
                  "py eecf.py -h (--help): Help")
            sys.exit()
        elif opt in ("-d", "--demo"):
            n = random_Nbit(int(arg))
        elif opt in ("-D", "--demoHARD"):
            n = nextPrime(random_Nbit(floor(int(arg)/2)))*nextPrime(random_Nbit(ceil(int(arg)/2)))
        elif opt in ("-n", "--number"):
            n = int(arg)
    print(f"\nTrying to factor {n}\n----------------------------------------")
    factors.append(n)
    while len(factors) > 0:
        recovered = primefactors + factors
        if len(recovered) > 1:
            recovered.sort()
            print(f"\n{n} = " + " * ".join([str(p) for p in primefactors + factors]) + "\n")
        fl = factor(factors.pop())
        if fl[0] == 0:
            factors = fl[1:] + factors
        else:
            primefactors = primefactors + fl[1:]
    primefactors.sort()
    m = 1
    for p in primefactors:
        m = m * p
    assert m == n
    print("\n -------- !DONE! -------- \n")
    print(str(n) + " = {}".format(" * ".join([str(i) for i in primefactors])))


if __name__ == "__main__":
    main(sys.argv[1:])
