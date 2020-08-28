class Money:

    # data members for showing amount of money and currency
    def __init__(self, currency_amount, currency_name):
        self.amount = currency_amount
        self.currency = currency_name

    # data method for printing amount of currency
    def print_obj(self):
        return str(self.amount) + ' ' + str(self.currency)

    # data method for summing two currencies
    def sum(self, other):
        money_amount = self.amount + other.amount
        return Money(money_amount, self.currency)

    # data method for subtracting two currencies
    def sub(self, other):
        money_amount = self.amount - other.amount
        return Money(money_amount, self.currency)


# function for making class objects, calling methods, printing results
def main():

    # making nwe instances for class Money()
    baht1 = Money(5000, 'THB')
    baht2 = Money(1000, 'THB')

    # printing new instances
    print(baht1.print_obj())
    print(baht2.print_obj())

    # summing two currencies of new created class objects and printing result
    print('After summing two currencies: ', baht1.sum(baht2).print_obj())

    # subtracting two currencies of new created objects and printing result
    print('After subtracting two currencies: ', baht1.sub(baht2).print_obj())


# calling function
main()
