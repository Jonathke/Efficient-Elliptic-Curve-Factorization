from random import randint
import sys
from math import log, gcd

from ellipticCurve import *
from millerRabin import *
from modNarithmetic import *

def lenstra(n):
    R = IntegersModN(n)
    X = R(2)
    for i in range(1,n//2-1):
        curve = Curve(R(i))
        print("        Trying curve: %s" % (curve))
        P = Point(X, R(1), curve)
        dmax = max(int(log(n, 2)**(1.61)), 20)
        for i in range (1,dmax+1):
            P = i*P
            fac = gcd(int(P.Z), n)
            if fac > 1:
                print("            Divisible by "+str(fac))
                return fac

if __name__ == "__main__":
    print(lenstra(101*103*101))
