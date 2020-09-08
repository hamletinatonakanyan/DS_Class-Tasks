# STRINGS
# 1.Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
inputted_str = str(input("Input some word(s): "))
new_str = inputted_str[:2] + inputted_str[-2:]
print("New string made by your inputted word's first and last 2 letters, is: ", new_str)


# 2.Write a Python program to remove the nth index character from a nonempty string.
inputted_str = str(input("Input some word(s): "))

n_th = int(input("Input number of letter which you want to remove  from your word(counted from left): "))
new_str = inputted_str[:(n_th-1)] + inputted_str[n_th:]
print("Your new word is: ", new_str)


# 3.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
inputted_str = str(input("Input some word(s): "))

tmp = inputted_str[0]
inputted_str = inputted_str.replace(inputted_str[0], inputted_str[-1])
inputted_str = inputted_str[:-1] + tmp
print(inputted_str)


# 4.Write a Python function to get a string made of 4 copies of the last two characters of a specified string
specified_str = str(input("Please input some word: "))


def char_copy(spec_str):
    last_2_char_copy = spec_str[-2:] * 4
    return last_2_char_copy


print(char_copy(specified_str))



# LISTS
# 1.Write a Python program that make a list from given string

any_str = 'Python'
print("Our word is: ", any_str)
str_to_list1 = list(any_str)
print("List made by letters is: ", str_to_list1)

# or
str_to_list2 = [ch for ch in any_str]
print("List made by letters is: ", str_to_list2)

# or
str_to_list3 = []
str_to_list3.extend(any_str)
print("List made by letters is: ", str_to_list3)



# 2.Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.

given_list = [2, 'hi', ['data', 'science'], '!', 33, "by", ':)']
print("Given list is: ", given_list)
new_list = (given_list[1:4] + given_list[6:])
print("New list after deleting elements is: ", new_list)

# or
del given_list[4:6]
del given_list[0]
print("New list after deleting elements is: ", given_list)



# 3.Write a Python program which add an element to the given list

some_list = [2, 3, 4, ['hello', 1], 'universe']
print("Inputted list is: ", some_list)
elem = 'hi there'
some_list.append(elem)
print("Extended list is: ", some_list)



# 4.Write a Python program which concat 2 lists.
first_list = [1, 2, 3]
print("First list is: ", first_list)

second_list = ["lampochka", "gori"]
print("Second list is: ", second_list)

final_list = first_list + second_list
print("List after concatenating first two is: ", final_list)

# or
first_list.extend(second_list)
print("List after concatenating first two is: ", first_list)