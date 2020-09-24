import numpy as np

#%%
# 1. Write program which will find the maximum and minimum values of multidimensional numpy array

multi_dim_array = np.random.randint(1, 40, (2, 5, 4))
print(f'Multidimensional array:\n {multi_dim_array}')

min_MD_array = np.min(multi_dim_array)
print(f'Minimum value of the given multi dimensional array: {min_MD_array}')

max_MD_array = np.max(multi_dim_array)
print(f'Maximum value of the given multi dimensional array: {max_MD_array}')


#%%
# 2. Write program which will find the maximum and minimum values of 2nd column in the multidimensional numpy array

MD_array = np.random.randint(1, 19, (2, 3, 3))
print(f'Multidimensional array:\n {MD_array}')

min_by_2nd_column = np.min(MD_array[:, :, 1], axis=1)
print(f'\nMinimum values by 2nd column of the given multidimensional array: {min_by_2nd_column}')

max_by_2nd_column = np.max(MD_array[:, :, 1], axis=1)
print(f'\nMaximum values by 2nd column of the given multidimensional array: {max_by_2nd_column}')


#%%
# 3. Write program which will find the median value in the multidimensional numpy array

dim4_array = np.arange(1, 49).reshape(2, 2, 4, 3)
print(f'Multidimensional array:\n {dim4_array}')

median_4d_array = np.median(dim4_array)
print(f'\nMedian of the given 4 dimensional array: {median_4d_array}')


#%%
# 4. Create 1D and 2D numpy arrays and multiple together

dim1_array = np.arange(1, 7)
print(f'One dimensional array:\n {dim1_array}')

dim3_array = np.arange(1, 37).reshape(2, 3, 6)
print(f'\n3 dimensional array:\n {dim3_array}')

d1_dot_3d = np.dot(dim3_array, dim1_array)
print(f"\nMultiplication of 1D array to 3D array through 'np.dot':\n {d1_dot_3d}")

mul_dim1_to_dim3 = dim1_array * dim3_array
print(f"\nMultiplication of 1D array to 3D array through '*' : \n {mul_dim1_to_dim3}")
