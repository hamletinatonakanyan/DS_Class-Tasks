import numpy as np

#%%
# 1. Write a NumPy program to compute the multiplication of two given matrices

# generate first 3D matrix
np_arr1 = np.arange(1, 13).reshape(3, 2, 2)
print('First given 3D matrix:\n', np_arr1)

# generate second 3D matrix
np_arr2 = np.arange(13, 25).reshape(2, 2, 3)
print('\nSecond given 3D matrix:\n', np_arr2)

# multiple 2 given matrices
mult = np.dot(np_arr1, np_arr2)
print('\nMultiplication of 2 matrices:\n', mult)


#%%
# 2. Write a NumPy program to compute the determinant of an array

# generate 3D matrix
np_arr = np.random.randint(0, 27, (3, 3, 3), int)
print('\nGiven matrix:\n', np_arr)

# counting determinant of given array
det = np.linalg.det(np_arr)
print('\nDeterminant of given matrix:\n', det)


#%%
# 3. Write a NumPy program to compute the sum of the diagonal element of a given array

# generate 2D and 3D matrices and output the sum of those diagonal respectively
arr_2D = np.random.randint(1, 100, (3, 3))
print('\nGiven 2D matrix:\n', arr_2D)

arr_2D_diag_sum = np.trace(arr_2D)
print('\nSum of the diagonal of the given 2D matrix:\n', arr_2D_diag_sum)
print('\n', np.diagonal(arr_2D))


arr_3D = np.arange(1, 28).reshape(3, 3, 3)
print('\nGiven 3D matrix:\n', arr_3D)

diag_3D = np.diagonal(arr_3D)
arr_3D_diag_sum = np.trace(diag_3D)
print('\nSum of the diagonal of the given 3D matrix:\n', arr_3D_diag_sum)


#%%
# 4. Write a NumPy program to compute the inverse of a given matrix
from numpy.linalg import inv

# creating matrix
matrix_3D = np.random.randint(1, 100, (3, 3))
print('Given matrix:\n', matrix_3D)

# making the inverse matrix trough multiplication of the given 3d matrix to it's transposed matrix
pre_inv_matrix = matrix_3D.T.dot(matrix_3D)
inversed_matrix_3D = inv(pre_inv_matrix)
print('\nInversing the given matrix:\n', inversed_matrix_3D)

# checkin the inversed matrix through multiplication it to it's inversed
diag_eye_matrix = pre_inv_matrix.dot(inv(pre_inv_matrix))
print('\nMatrix with ones in diagonal:\n', diag_eye_matrix)


#%%
# 5. Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.

# write a few arrays to a file
np.savez('matrix inverse.npz', a=matrix_3D, b=inversed_matrix_3D)

print('\nRead data from created file:\n')

read_inv = np.load('matrix inverse.npz')
print('Created 3D matrix:\n', read_inv['a'])
print('\nInverse the 3D matrix:\n', read_inv['b'])
