import numpy as np

# 1.Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

#%%
num_list = [i for i in range(1, 100, 5)]
print(f'Python list:\n{num_list}')

numpy_array = np.array(num_list)
print(f'Numpy array from python list:\n{numpy_array}')


#%%
# 2.Write a NumPy program to create a NumPy array with values ranging from 2 to 10

arranged_array = np.arange(2, 10).reshape(2, 2, 2)
print('Making numpy array through arange function and reshaping it to 3D (2, 2, 2) array:\n', arranged_array)


#%%
# 3.Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.

null_vector = np.zeros(10)
print('Null vector is:\n', null_vector)
null_vector[5:8] = 11
print('Updated vector is:\n', null_vector)


#%%
# 4.Write a NumPy program to test whether each element of a 1-D array is also present in a second array

np_arr1 = np.random.randint(1, 10, 5, int)
print('first numpy array:\n', np_arr1)
np_arr2 = np.random.randint(3, 9, 4, int)
print('second numpy array:\n', np_arr2)

bool_common = np.in1d(np_arr1, np_arr2)
print('Values of first array which are also presented in second one, resulting in boolean values:\n', bool_common)


#%%
# 5. Check if two arrays have common values and return the indices

arr_ind = np.intersect1d(np_arr1, np_arr2)
if len(arr_ind) == 0:
    print('There isn\'t common values')
else:
    print('Indices of common values of 2 arrays:\n', arr_ind)