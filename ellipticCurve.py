class Curve(object):
    #Weierstras form: y**2 = x**3 + a*x + b
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.discriminant = -16*(4*a*a*a + 27*b*b)
        self.singular = (self.discriminant == 0)

    def testPoint(self, x, y):
        return y*y == x*x*x + self.a*x + self.b

    def __str__(self):
        return 'y^2 = x^3 + %sx + %s' % (self.a, self.b)


class Point(object):
    def __init__(self, x, y, curve):
        self.curve = curve
        self.x = x
        self.y = y
        if not curve.testPoint(x, y):
            raise Exception("This point %s not a valid point on the curve %s" % (self, self.curve))

    def __str__(self):
        return "(%r, %r)" % (self.x, self.y)

    def __neg__(self):
        return Point(self.x, -self.y, self.curve)

    def __add__(self, Q):
        if isinstance(Q, Identity):
            return self
        x_1, y_1, x_2, y_2 = self.x, self.y, Q.x, Q.y
        if (x_1, y_1) == (x_2, y_2):
            if y_1 == 0:
                return Identity(self.curve)
            m = (3 * x_1 * x_1 + self.curve.a) / (2 * y_1)
        else:
            if x_1 == x_2:
                return Identity(self.curve)  # vertical line
            m = (y_2 - y_1) / (x_2 - x_1)
        x_3 = m * m - x_2 - x_1
        y_3 = m * (x_3 - x_1) + y_1
        return Point(x_3, -y_3, self.curve)

    def __sub__(self, Q):
        return self + -Q

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Can't scale a point by something which isn't an int!")
        if n < 0:
            return -self * -n
        if n == 0:
            return Identity(self.curve)
        Q = self
        R = self if n & 1 == 1 else Identity(self.curve)
        i = 2
        while i <= n:
            Q += Q
            if n & i == i:
                R += Q
            i = i << 1
        return R

    def __rmul__(self, n):
        return self * n

    def __ne__(self, other):
        return not self == other


class Identity(Point):
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Identity"

    def __neg__(self):
        return self

    def __add__(self, Q):
        return Q


