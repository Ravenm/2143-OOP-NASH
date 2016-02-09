class Fraction(object):
    def __init__(self, n=None, d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        x = self.numerator / self.denominator
        if x != 0:
            return "%s and %s / %s" % (x, self.numerator % self.denominator, self.denominator)
        else:
            return "%s / %s" % (self.numerator, self.denominator)

    def numerator(self, n):
        self.numerator = n

    def denominator(self, d):
        self.denominator = d

    def __mul__(self, rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return Fraction(x, y)

    def __add__(self, rhs):
        return Fraction(((self.numerator * rhs.denominator)+(rhs.numerator * self.denominator)),
                        (self.denominator * rhs.denominator))

if __name__ == '__main__':
    a = Fraction(1, 2)
    b = Fraction(4, 5)
    e = Fraction(15, 16)
    c = a * b
    print(c)
    d = a + b
    print(d)
    g = b * e
    print(g)
    f = b + e
    print(f)
