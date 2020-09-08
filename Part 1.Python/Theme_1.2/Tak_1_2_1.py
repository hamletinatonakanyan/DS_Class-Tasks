# 1.Write a Python program to get the largest number from a list.

lst = [12, 34, 3, 11, 89, 121]
desc_sorted = sorted(lst, reverse=True)
largest_elem = desc_sorted[0]
print(largest_elem)


# 2.Write a Python program to get the frequency of the given element in a list to.

li_st = [11, 34, 3, 11, 89, 121, 34, 11, 3]
frequency = li_st.count(11)
print(frequency)


# 3.Write a Python program to remove the second element from a given list,
#   if we know that the first elements index with that value is n.

lis_t = [34, 11, 3, 11, 89, 121, 34, 11, 3]
after_1_index = lis_t.index(11) + 1
deleting_index = lis_t.index(11, after_1_index)
lis_t.pop(deleting_index)
print(lis_t)