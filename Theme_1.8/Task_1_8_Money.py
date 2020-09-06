class MoneyE:
    def __init__(self, currency_amount, currency_name):

        try:
            if type(currency_amount) is not int:
                raise TypeError
        except TypeError:
            print('Money constructor: amount must be int type')

        try:
            if type(currency_name) is not str:
                raise TypeError
        except TypeError:
            print('Money constructor: Currency must be str type')

        try:
            if currency_amount < 0:
                raise ValueError
        except ValueError:
            print('Money constructor: Amount must be positive value')

        self.amount = currency_amount
        self.currency = currency_name

    def __repr__(self):
        try:
            if self.amount < 0:
                raise ValueError
        except ValueError:
            print('MoneyE.__repr__: Amount must be positive value.')

        try:
            if type(self.currency) is not str:
                raise TypeError
        except TypeError:
            print('MoneyE.__repr__: Currency must be string value.')
        return f'{str(self.amount)} {self.currency}'

    def sum(self, other):
        money_amount = self.amount + other.amount

        try:
            if money_amount < 0:
                raise ValueError
        except ValueError:
            print('MoneyE.sum(): Amount is negative value')
        else:
            return MoneyE(money_amount, self.currency)

    def sub(self, other):
        money_amount = self.amount - other.amount

        try:
            if money_amount < 0:
                raise ValueError
        except ValueError:
            print('MoneyE.sub(): Amount is negative value')
        else:
            return MoneyE(money_amount, self.currency)


def main_e(cur1, cur2, amnt1, amnt2):
    try:
        if type(cur1) is not str:
            raise TypeError
    except TypeError:
        print('def main_e: Currency must be string type.')

    try:
        if type(cur2) is not str:
            raise TypeError
    except TypeError:
        print('def main_e: Currency must be string type.')

    try:
        if type(amnt2) is not int:
            raise ValueError
    except ValueError:
        print('def main_e: Amount must be int type.')

    try:
        if type(amnt2) is not int:
            raise ValueError
    except ValueError:
        print('def main_e: Amount must be int type.')
    else:
        baht1 = MoneyE(amnt1, cur1)
        baht2 = MoneyE(amnt2, cur2)

        print(baht1)
        print(baht2)

        print('After summing two currencies: ', baht1.sum(baht2))
        print('After subtracting two currencies: ', baht1.sub(baht2))


main_e('BHT', 2, -5000, 1000)
