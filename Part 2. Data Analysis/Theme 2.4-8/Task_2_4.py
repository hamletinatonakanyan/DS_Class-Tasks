import pandas as pd
import numpy as np

#%%

# 1. Write a Pandas program to add, subtract, multiple and divide two Pandas Series

# Creating first Pandas Series
py_list = list(range(1, 8))
list_of_indexes = ['b', 'c', 'f', 'd', 'a', 'g', 'e']
pd_series1 = pd.Series(py_list, index=list_of_indexes).sort_index()
print(f'\nFirst Pandas Series:\n{pd_series1}')

# Creating second Pandas Series
pd_series2 = pd.Series([-2, 4, -5, 3, 9, 1, -4])
print(f'\nSecond Pandas Series:\n{pd_series2}')

# Adding two Pandas Series
print('\nAdding created two Pandas Series.\n')
added_pd_series = pd.Series(pd_series1.values + pd_series2.values, index=pd_series1.index)
print(added_pd_series)

# Subtracting two Pandas Series
print('\nSubtracting created two Pandas Series.\n')
added_pd_series = pd.Series(pd_series1.values - pd_series2.values, index=pd_series1.index)
print(added_pd_series)

# Multiplying two Pandas Series
print('\nMultiplying created two Pandas Series.\n')
added_pd_series = pd.Series(pd_series1.values * pd_series2.values, index=pd_series1.index)
print(added_pd_series)

# Dividing two Pandas Series
print('\nDividing created two Pandas Series.\n')
added_pd_series = pd.Series(pd_series1.values // pd_series2.values, index=pd_series1.index)
print(added_pd_series)


#%%

# 2. Write a Pandas program to convert a dictionary to a Pandas series.

py_dict = {'a': 6, 'c': 9, 'd': 13, 'b': 7}
print(f'\nPython dictionary: {py_dict}')

dict_to_pdSeries = pd.Series(py_dict).sort_index()
print(f'\nPandas Series converted from a dictionary\n{dict_to_pdSeries}')


#%%

# 3. Write a Pandas program to convert a NumPy array to a Pandas series

npArray_to_pdSeries = pd.Series(np.arange(1, 9), index=['c', 'o', 'u', 'n', 't', 'i', 'n', 'g'])
print(f'\nPandas Series converted from a Numpy array\n{npArray_to_pdSeries}')


#%%

# 4. Write a Pandas program to convert the first column of a DataFrame as a Series

pd_data = pd.DataFrame(np.arange(1, 17).reshape(4, 4), index=['f', 's', 't', 'fo'], columns=['first', 'second', 'third', 'fourth'])
print('\nPandas data\n', pd_data)

print(f"\nFirst column of a Pandas DataDrame converted to a Pnadas Series.\n{pd_data['first']}")
print(f"\nFirst column of a Pandas DataDrame converted to a Pnadas Series through iloc function.\n{pd_data.iloc[:, 0]}")


#%%

# 5. Write a Pandas program to sort a given Series

pdSeries = pd.Series(np.arange(1, 9), index=['c', 'o', 'u', 'n', 't', 'i', 'n', 'g'])
print(f'\nPandas Series\n{npArray_to_pdSeries}')
print(f'\nSorted Pandas Series by index\n{pdSeries.sort_index()}')
print(f'\nSorted Pandas Series by values in descending order\n{pdSeries.sort_values(ascending=False)}')


#%%

# 6. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

# Pandas DataFrame- information about students' examination
student_exam_data = pd.DataFrame(
    {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
     'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
     'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
     index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(f"\nPandas DataFrame: information about students' exam results\n\n{student_exam_data}")

# Selecting the rows where 15 > score <= 20
selected_rows = student_exam_data[(student_exam_data.score > 15) & (student_exam_data.score <= 20)]
print(f"\nSelected rows, where 15 < score <= 20:\n{selected_rows}")


#%%

# 7. Write a Pandas program to calculate the sum of the examination attempts by the students.

# Pandas DataFrame - information about students' examination
student_data = pd.DataFrame(
    {'name': ['John', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
     'score': [11.3, 9.6, 18.7, np.nan, 13.9, 20, 14.5, np.nan, 8, 19],
     'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
     'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
     index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(f"\nPandas DataFrame: information about students' examination\n\n{student_data}")

# Calculate the sum of the examination attempts by the students
attempts_sum = pd.Series(student_data['attempts']).sum()
print(f'\nSum of the examination attempts by the students: {attempts_sum}')
