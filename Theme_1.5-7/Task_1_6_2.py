class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

        # simplifying the object's values through method great common divisor
        gc_div = Rational.gcd(self.numerator, self.denominator)
        self.numerator //= gc_div
        self.denominator //= gc_div

    # overriding dunder method for printing
    def __repr__(self):
        return f'{self.numerator} {self.denominator}'

    # static method for returning new object with value of great common divisor
    @staticmethod
    def gcd(n, d):
        if d == 0:
            return n
        return Rational.gcd(d, n % d)

    # static method for returning new object with value of least common multiple
    @staticmethod
    def lcm(n, d):
        return (n * d) / Rational.gcd(n, d)

    # overloading some dunder methods
    def __add__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num = self.numerator * (denom / self.denominator) + other.numerator * (denom / other.denominator)
        return Rational(num, denom)

    def __sub__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num = self.numerator * (denom / self.denominator) - other.numerator * (denom / other.denominator)
        return Rational(num, denom)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Rational(num, denom)

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        denom = self.denominator * other.numerator
        return Rational(num, denom)

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    def __gt__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 > num2:
            return True
        return False

    def __ge__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 >= num2:
            return True
        return False

    def __lt__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 < num2:
            return True
        return False

    def __le__(self, other):
        denom = Rational.lcm(self.denominator, other.denominator)
        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 <= num2:
            return True
        return False

    def __pow__(self, power, modulo=None):
        num = self.numerator ** power
        denom = self.denominator ** power
        return Rational(num, denom)


