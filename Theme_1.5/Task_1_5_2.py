class Money:

    # defining 2 class variables
    amount = 0
    currency = ''

    # as arguments constructor takes amount of currency and it's name
    def __init__(self, currency_amount, currency_name):
        self.amount = currency_amount
        self.currency = currency_name

    # class method for printing amount of currency
    def print_obj(self):
        print(f'Exists {self.amount} {self.currency}.')

    # class method for summing two currencies
    def sum(self, other):
        return self.amount + other.amount

    # class method for subtracting two currencies
    def sub(self, other):
        return self.amount - other.amount


# function for defining class objects, calling class methods, printing results
def main():

    baht1 = Money(5000, 'THB')
    baht2 = Money(1000, 'THB')

    baht1.print_obj()
    baht2.print_obj()

    summing = baht1.sum(baht2)
    print(f'{baht1.currency} after increasing: {summing}')

    subtract = baht1.sub(baht2)
    print(f'{baht1.currency} after decreasing: {subtract}')


# calling function
main()
