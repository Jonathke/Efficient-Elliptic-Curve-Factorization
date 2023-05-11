class IntegersModN(object):
    def __init__(self, N):
        self.N = N
    def mod(self):
        return self.N
    def __call__(self, n):
        return ModNElem(n, self)

class ModNElem(object):
    def __init__(self, n, R):
        self.R = R
        self.n = n % R.N

    def __add__(self, other):
        if type(other) == int:
            return self.R(self.n + other)
        return self.R(self.n + other.n)
    def __sub__(self, other):
        return self.R(self.n - other.n)
    def __mul__(self, other):
        return self.R(self.n * other.n)
    def __neg__(self):
        return self.R(-self.n)
    def __pow__(self, e):
        return self.R(pow(self.n, e, self.R.mod()))
    def __eq__(self, other):
        return self.R == other.R and self.n == other.n
    def inv(self):
        return self.R(pow(self.n, -1, self.R.mod()))
    def __str__(self):
        return str(self.n)
    def __repr__(self):
        return f'{self.n} (mod {self.R.mod()})'
    def __int__(self):
        return self.n

if __name__ == "__main__":
    ZN = IntegersModN(13*17)
    a = ZN(4)
    b = ZN(15)
    print(a*b)
    print(a*b*b)
    print(a.inv())
    print(a.inv()*a)
    print(int(b.inv()))
