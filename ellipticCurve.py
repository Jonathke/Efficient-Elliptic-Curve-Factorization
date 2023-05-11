class Curve(object):
    #Montgomery curve
    def __init__(self, A):
        self.A = A

    def testPoint(self, x, y):
        return y**2 == x**3 + self.A*x**2 + x

    def __str__(self):
        return f'y^2 = x^3 + {self.A}x^2 + x'


class Point(object):
    def __init__(self, X, Z, curve):
        self.X = X
        self.Z = Z
        self.curve = curve

    def normalize(self):
        return Point(self.X*self.Z**(-1), 1, self.curve)

    def __str__(self):
        return f"({self.X}: {self.Z})"

    def XZ(self):
        return [self.X, self.Z]

    def __mul__(self, n):
        """
        montgomery-ladder
        input: coordinates of P=(XP:ZP)
               scalar factor m, curve constants (A:C)
        output: KummerPoint [m]P=(X0:Z0)
        """
        if not n:
            return self.parent().zero()
        n = abs(n)
        if n == 1:
            return self

        XP, ZP = self.XZ()
        A = self.curve.A
        R0, R1, diff = self, xDBL(self, self.curve.A), self
        # Montgomery-ladder
        for i in [int(b) for b in bin(n)[3:]]:
            R0pR1 = xADD(R0, R1, diff)
            diff = xADD(R0, R1, R0pR1)
            if i == 0:
                R0, R1 = xDBL(R0, self.curve.A), R0pR1
            if i == 1:
                R0, R1 = R0pR1, xDBL(R1, self.curve.A)
        return R0

    def __rmul__(self, n):
        return self * n

def xDBL(P, A):
    X, Z = P.XZ()
    t0 = X - Z
    t1 = X + Z
    t0 = t0**2
    t1 = t1**2
    Z2 = t0
    Z2 = Z2 + Z2
    Z2 = Z2 + Z2
    X2 = Z2 * t1
    t1 = t1 - t0
    t0 = A + 2
    t0 = t0 * t1
    Z2 = Z2 + t0
    Z2 = Z2 * t1
    return Point(X2, Z2, P.curve)

def xADD(P, Q, diff):
    XP, ZP = P.XZ()
    XQ, ZQ = Q.XZ()
    xPQ, zPQ = diff.XZ()
    t0 = XP + ZP
    t1 = XP - ZP
    XP = XQ - ZQ
    ZP = XQ + ZQ
    t0 = XP * t0
    t1 = ZP * t1
    ZP = t0 - t1
    XP = t0 + t1
    ZP = ZP**2
    XQP = XP**2
    ZQP = xPQ * ZP
    XQP = XQP * zPQ
    return Point(XQP, ZQP, P.curve)
