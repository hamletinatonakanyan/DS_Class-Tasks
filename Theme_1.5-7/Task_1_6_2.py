class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def __repr__(self):
        return f'{self.numerator} {self.denominator}'

    @staticmethod
    def gcd(n, d):
        if d == 0:
            return n
        return Rational.gcd(d, n % d)

    def simplify(self):
        gc_div = Rational.gcd(self.numerator, self.denominator)
        self.numerator //= gc_div
        self.denominator //= gc_div
        return Rational(self.numerator, self.denominator)


rational = Rational(6, 8)
print(rational.simplify())
