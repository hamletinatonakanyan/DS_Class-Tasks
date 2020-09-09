class RationalEx:
    def __init__(self, num, denom):

        try:
            if type(num) is not int:
                raise TypeError
        except TypeError:
            print('RationalE constructor: numerator must be integer')
        else:
            self.numerator = num

        try:
            if type(denom) is not int:
                raise TypeError
            elif denom == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('RationalE constructor: denominator can\'t be zero')
        except TypeError:
            print('RationalE constructor: denominator must be integer')
        else:
            self.denominator = denom

            # simplifying the object's values through method great common divisor
            gc_div = RationalEx.gcd(self.numerator, self.denominator)
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
        return RationalEx.gcd(d, n % d)

    # static method for returning new object with value of least common multiple
    @staticmethod
    def lcm(d1, d2):
        return (d1 * d2) / RationalEx.gcd(d1, d2)

    # overloading some dunder methods
    def __add__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)
        num = self.numerator * (denom / self.denominator) + other.numerator * (denom / other.denominator)
        return RationalEx(num, denom)

    def __sub__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)
        num = self.numerator * (denom / self.denominator) - other.numerator * (denom / other.denominator)
        return RationalEx(num, denom)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator

        return RationalEx(num, denom)

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        denom = self.denominator * other.numerator

        return RationalEx(num, denom)

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    def __gt__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)

        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 > num2:
            return True
        return False

    def __ge__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)

        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 >= num2:
            return True
        return False

    def __lt__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)

        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 < num2:
            return True
        return False

    def __le__(self, other):
        denom = RationalEx.lcm(self.denominator, other.denominator)

        num1 = denom / self.denominator * self.numerator
        num2 = denom / other.denominator * other.numerator
        if num1 <= num2:
            return True
        return False

    def __pow__(self, power, modulo=None):
        num = self.numerator ** power
        denom = self.denominator ** power

        return RationalEx(num, denom)


rati1 = RationalEx(7, 6)
rati2 = RationalEx(5, 2)

try:
    print(rati1 + rati2)
except AttributeError:
    print('There is no such attribute')
