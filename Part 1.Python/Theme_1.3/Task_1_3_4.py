""" 1.Write a Python function, which Implements the Euler function.
# Euler function returns a count of numbers not great than N, which are mutually simple with N. """


# Version 1
def euler_func(num):
    e_nums = []

    # checking  which numbers  are dividers for num and adding them to the list
    num_divs = [i for i in range(1, num) if num % i == 0]

    # checking dividers of each number between [1, num)
    for k in range(1, num):
        each_divs = []
        for m in range(1, k+1):
            if k % m == 0:
                each_divs.append(m)

        # compare amount of  num's dividers and each number's dividers, if \
        # their have only one common divider, count this number as Euler's number
        intersection = list(set(num_divs).intersection(set(each_divs)))
        if len(intersection) == 1:
            e_nums.append(k)

    return len(e_nums)


# Version 2: Implementing Euler's totient function
def euler_totient(num):
    eulers_num = []

    # counting great common divisor of 2 numbers
    def gcd(n1, n2):
        if n2 == 0:
            return n1
        return gcd(n2, n1 % n2)

    # checking if gcd of given number and each number before that is equal 1 or not
    for i in range(1, num):
        if gcd(num, i) == 1:
            eulers_num.append(i)

    return len(eulers_num)


""" 2.Ticket numbers usually consist of an even number of digits. A ticket number is considered 
        lucky if the sum of the first half of the digits is equal to the sum of the second half.
      Given a ticket number n, determine if it's lucky or not. """


def lucky_number(number):
    number_to_string = str(number)
    sum_start = 0
    sum_end = 0

    for i in range(len(number_to_string)):
        if i < len(number_to_string)/2:
            sum_start += int(number_to_string[i])
        else:
            sum_end += int(number_to_string[i])

    if sum_start == sum_end:
        return True
    else:
        return False


""" 3. The robot is standing on a rectangular grid and is currently located at the point (X0, Y0). 
       The coordinates are integers. It receives N remote commands(list with n elements each of them is a command). 
       Each command is one of : up, down, left, right. Upon receiving a correct command, the robot moves one unit 
       in the given direction. If the robot receives an incorrect command, it simply ignores it. 
       Where will the robot be located after following all the commands? """


def move_robot(n_list):
    coordinates = {'X': 0, "Y": 0}

    for i in n_list:
        if i == 'right':
            coordinates['X'] += 1
        elif i == 'left':
            coordinates['X'] -= 1
        elif i == 'up':
            coordinates['Y'] += 1
        elif i == 'down':
            coordinates['Y'] -= 1

    return tuple(coordinates.values())


""" 4. Write a python function, which returns the sum of digits of given number N. """


def digits_sum(num):
    s_num = str(num)
    dig_sum = 0

    for i in s_num:
        dig_sum += int(i)

    return dig_sum


""" 5. Write a python program to find the next smallest palindrome of a specified number. 
       For example, for 119 next palindrome is 121. """


def next_palindrome(num):
    # count how many is needed for next tenner, add it to the number
    tmp = 10 - (num % 10)
    new_num = num + tmp

    # cut the last digit(last zero)
    new_num = new_num // 10

    # to the current number add the same number (until last digit) in reverse version
    final_num = str(new_num) + str(new_num)[:-1][::-1]

    return int(final_num)

