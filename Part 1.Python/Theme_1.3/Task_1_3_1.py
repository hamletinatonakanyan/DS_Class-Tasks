""" 1. Write a Python function, which gets 2 numbers,
       and return True if the second number is first
       number divider, otherwise False."""


def divider(x, y):
    if x % y == 0:
        return True
    return False


"""  2. Write a Python function, which gets a number, and return True 
       if that number is palindrome, otherwise False. """


def palindrome(num):   # version 1
    s_num = str(num)
    
    if s_num[:] == s_num[::-1]:
        return True
    return False


def palindrome(num):    # version 2
    s_num = str(num)
    
    for i in s_num:
        if int(i) == num % 10:
            num //= 10
        else:
            return False
    return True


""" 3. Write a Python function, which gets a number, and 
       return True if that number is prime, otherwise False. """


def prime(num):

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


""" 4. Write a Python function, which checks if a number is perfect 
      - that is equal to the sum of its proper positive divisors. """


def perfect_number(num):
    sum = 0

    # catching all divisors of number and summing together 
    for i in range(1, num):
        if num % i == 0:
            sum += i

    # if sum of divisors is equal to number => it's a perfect one
    if sum == num:
        return True
    else:
        return False


""" 5. Write a function, which gets 2 numbers, and return their Great common divisor """


def great_com_div(num1, num2):
    if num2 == 0:
        return num1
    return great_com_div(num2, num1 % num2)


print(great_com_div(96, 36))

