# 1. Write a python program, which adds a new value with the given key in dict.

my_dict = {'list': [1, 1, 2, 3, 5]}

# adding new value in the key which already exists
my_dict['list'].append(8)

# adding new value through new key
my_dict['tuple'] = (13, 21, 34, 55)
print(my_dict)


# 2. Write a python program which concat 2 dicts.

dict1 = {'set': {1, 2, 3, 5}}
dict2 = {'string': 'hey you'}
dict1.update(dict2)
print(dict1)


# 3. Write a python program, which create a dictionary for given number N,
#    where keys are numbers from 1 to N, and values are cubs of that numbers

def dictionary(num):
    dict_cube = {}
    for i in range(1, num+1):
        dict_cube.update({i: i**3})

    return dict_cube


# 4. Write a python program which create dict from 2 lists with the same length

# through implementing function
def list_to_dict(list1, list2):
    brightest = {}
    keys = list1[::-1]
    values = list2[::-1]

    for i in range(len(keys)):
        brightest[keys.pop()] = values.pop()
    return brightest


# through zipping
value = ['Antares', 'Betelgeuse', 'Aldebaran', 'Rigel']
key = [1, 2, 3, 4]

brightest_stars = dict(zip(key, value))
print(brightest_stars)


# 5. Write a python program which gets the maximum and minimum values of a dictionary

def dict_mm_values(my_dict):
    values = sorted(list(my_dict.values()))
    max_v = values[-1]
    min_v = values[0]
    return max_v, min_v


# 6. Write a python program which combines 2 dictionaries into one, if there is an element with the same key,
#    appropriate element of combined dict will be an element with that key, and sum of values as value.

def dicts_combine(dict1, dict2):
    for i in dict2.keys():
        if i in dict1:
            dict1[i] += dict2[i]
        else:
            dict1.update({i: dict2[i]})
    return dict1


# 7. Write a python program which create dict from string, where keys are letters of  string,
#    values are counts of letters in string

def str_to_dict(given_str):
    output_dict = {}

    for i in given_str:
        output_dict.update({i: given_str.count(i)})
    return output_dict
