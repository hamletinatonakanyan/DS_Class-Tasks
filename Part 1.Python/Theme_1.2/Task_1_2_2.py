# 1.Write a Python program to multiply all the items in a list.
list1 = [1, 1, 2, 3, 5, 8, 11]
multi = 1
i = 0

while i < len(list1):
    multi *= list1[i]
    i += 1
print(multi)


# 2.Write a Python program to get the largest number from a list.
list2 = [1, 13, 2, 3, 5, 8, 11]
largest_num = list2[0]
i = 1

while i < len(list2):
    if list2[i] > largest_num:
        largest_num = list2[i]
    i += 1
print(largest_num)


# 3.Write a Python program to generate and print a list except for the first 5 elements,
#   where the values are square of numbers between 1 and 30 (both included)
gen_list = []
i = 0
j = 1

while i < 30:
    if i > 4:
        gen_list.append(j**2)
    else:
        gen_list.append(j)
    print(i, " - ", gen_list[i])
    i += 1
    j += 1


# 4.Write a Python program to remove duplicates from a list
dup_list = [4, 5, 3, 4, 11, 3, 54, 11, 62, 78, 5]

for elem in dup_list:
    if dup_list.count(elem) > 1:
        dup_list.remove(elem)
print(dup_list)


# 5. Write a Python program to find the most appeared element in a list.
lst = [4, 5, 11, 4, 11, 3, 54, 11, 62, 78, 5]
most_appeared = lst[0]

for elem in lst:
    if lst.count(elem) > lst.count(most_appeared):
        most_appeared = elem
print(most_appeared)