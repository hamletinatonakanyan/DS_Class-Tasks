class MoneyE:
    def __init__(self, currency_amount, currency_name):

        try:
            if type(currency_amount) is not int:
                raise TypeError
            elif currency_amount < 0:
                raise ValueError
        except TypeError:
            print('Money constructor: amount must be int type')
        except ValueError:
            print('Money constructor: Amount must be positive value')
        else:
            self.amount = currency_amount

        try:
            if type(currency_name) is not str:
                raise TypeError
        except TypeError:
            print('Money constructor: Currency must be str type')
        else:
            self.currency = currency_name

    def __repr__(self):
        return f'{str(self.amount)} {self.currency}'

    def sum(self, other):
        amount_sum = self.amount + other.amount
        return MoneyE(amount_sum, self.currency)

    def sub(self, other):
        amount_sub = self.amount - other.amount
        return MoneyE(amount_sub, self.currency)


def main_e(cur1, cur2, amnt1, amnt2):

    baht1 = MoneyE(amnt1, cur1)
    baht2 = MoneyE(amnt2, cur2)

    try:
        print(baht1)
        print(baht2)
        print('After summing two currencies: ', baht1.sum(baht2))
        print('After subtracting two currencies: ', baht1.sub(baht2))
    except AttributeError:
        print(f'main(): there is no such attribute')


main_e('BHT', 'BHT', 5000, 1000)
