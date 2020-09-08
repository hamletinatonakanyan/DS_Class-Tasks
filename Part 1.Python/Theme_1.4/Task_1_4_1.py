# 1.Write a python program which returns a given list without duplicates.

def unique_elem(lst):
    return set(lst)


# 2. Write a python program which returns common elements of 2 lists.

def common_elem(list1, list2):
    return set(list1) & set(list2)


# 3.Write a python program which return elements which are in first list but not in second

def deference(list1, list2):
    return set(list1) - set(list2)


# 4.Write a python program which return elements are or in first list, either in second, but not in both

def symmetric_def(list1, list2):
    return set(list1) ^ set(list2)


# 5. Write a python program which return elements which are or in first, either in second, or in both
def union(list1, list2):
    return set(list1) | set(list2)


# 6. Write  python function which get set and element value, and remove from set element with given value if exist

def remove_from_set(set1, elem):
    if elem in set1:
        set1.remove(elem)
    return set1


# 7. Write a python python program, which return list from given set,
#    where each element of list, is equal to cub of set element


def cube(se_t):
    lst_cube = []
    for i in se_t:
        lst_cube.append(i ** 3)
    return lst_cube
