#  1. Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.

triangle_leg1 = int(input("Please input the first length of right angled triangle: "))
triangle_leg2 = int(input("Please input the second length of right angled triangle: "))

right_triangle_area = (triangle_leg1 * triangle_leg2)/2
print(f'The area of right-angled triangle is equal to {right_triangle_area} sm. square')


#  2. Input a natural number n and output its last digit.

natural_number = int(input("Please input some natural number: "))

# Version 1: print out the last digit of natural number
last_digit = natural_number % 10
print("The last digit of your number is: ", last_digit)


# Version 2:  through converting int to string and taking the last index of string
number_to_string = str(natural_number)
last_index = number_to_string[-1]
print("The last index of your type casted number is: ", last_index)


#  3. Input a two-digit natural number and output the sum of its digits.

natural_number = int(input("Please input two digits natural number: "))
first_digit = natural_number // 10
second_digit = natural_number % 10
sum_of_digits = first_digit + second_digit
print("Sum of digits your inputted number is equal to: ", sum_of_digits)


#  4. Given the first and second number in an arithmetic progression and natural number n.
#      Find n-th element of arithmetic progression.

arith_num1 = int(input("Please input first number of arithmetic progression: "))
arith_num2 = int(input("Please input first number of arithmetic progression: "))
n = int(input("Input some natural number: "))

difference = arith_num2 - arith_num1
AP_nth_elem = arith_num1 + (n - 1) * difference
print("n-th element of arithmetic progression is equal to: ", AP_nth_elem)