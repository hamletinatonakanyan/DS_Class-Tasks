class Money:

    # data members for showing amount of money and currency
    def __init__(self, currency_amount, currency_name):
        self.amount = currency_amount
        self.currency = currency_name

    # data method for printing amount of currency
    def print_obj(self):
        print(f'Exists {self.amount} {self.currency}.')

    # data method for summing two currencies
    def sum(self, other):
        return f'After summing: {self.amount + other.amount} {self.currency}'

    # data method for subtracting two currencies
    def sub(self, other):
        return f'After subtracting: {self.amount - other.amount} {self.currency}'


# function for making class objects, calling methods, printing results
def main():

    # making nwe instances for class Money()
    baht1 = Money(5000, 'THB')
    baht2 = Money(1000, 'THB')

    # printing new instances
    baht1.print_obj()
    baht2.print_obj()

    # summing two currencies of new created class objects and printing result
    summing = baht1.sum(baht2)
    print(summing)

    # subtracting two currencies of new created class objects and printing result
    subtract = baht1.sub(baht2)
    print(subtract)


# calling function
main()
