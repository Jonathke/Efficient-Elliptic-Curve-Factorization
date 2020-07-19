import random

def exponensiation(x, a, G):
    a = "{0:b}".format(a)[::-1]
    out = 1
    val = x
    for c in a:
        if c == '1':
            out = (out*val)%G
        val = (val**2)%G
    if out == G-1:
        out = -1
    return out

def jacobiSymbol(a, n, s):
    if a == 0:
        return 0
    if a == 1:
        return s
    if a == 2:
        if n%8 == 1 or n%8 == 7:
            return s
        else:
            return -s
    if a >= n:
        return jacobiSymbol(a%n, n, s)
    elif a%2 == 1:
        if n%4 == 3 and a%4 == 3:
            return jacobiSymbol(n, a, -s)
        else:
            return jacobiSymbol(n, a, s)
    else:
        return s*jacobiSymbol(2, n, 1)*jacobiSymbol(a//2, n, 1)

def solowayStrassen(a, n):
    if n%2 == 0:
        return False
    return exponensiation(a, (n-1)//2, n) == jacobiSymbol(a, n, 1)

def SSTest(n):
    for i in range(50):
        if not solowayStrassen(random.randint(2, n-1) , n):
            return False
    return True
