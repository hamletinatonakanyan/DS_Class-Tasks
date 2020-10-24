import pandas as pd
import numpy as np
import csv

#%%

with open('data.csv') as out:
    res = csv.reader(out, delimiter='|')
    data = pd.DataFrame(res)


#%%

def clean_from_symbols(column, list_of_cleaned_values):

    """
    Function for cleaning values of column from  symbols in dataframe
    :param column: column of pandas dataFrame
    :param list_of_cleaned_values: list type variable for ceeping cleand values
    :return: list_of_cleaned_values
    """

    symbols = [',', '-', '.', ' ', ';', ':', '!', "*"]

    for value in column:
        value = ''.join(i for i in value if i not in symbols)
        if value.isnumeric():
            list_of_cleaned_values.append(int(value))
        else:
            list_of_cleaned_values.append(value)

    return list_of_cleaned_values


#%%

# 1. Write a Pandas program to display all the records of REGIONS file

region_file = data[0:8]
region_file = region_file.drop([0, 1, 2, 3], axis=0)
region_file = region_file.dropna(how='all', axis=1)
region_file = region_file.drop([0, 3], axis=1)
region_file.columns = ['REGION_ID', 'REGION_NAME']
region_file.set_index(np.arange(4))

for col in region_file.columns:
    cleaned = []
    clean_from_symbols(region_file[col], cleaned)
    region_file[col] = cleaned

print(region_file)

#%%

# 2. Write a Pandas program to display all the location id from locations file.

l_id = pd.DataFrame({"LOCATION_ID": data.iloc[14:37, 1]})
location_id = l_id.set_index(np.arange(len(l_id)))
print(location_id)


#%%

# 3. Write a Pandas program to extract first 7 records from employees file.
employees_7 = data[43:50]
employees_7 = employees_7.drop([0, 12], axis=1).\
    set_index(np.arange(len(employees_7)))
employees_7.columns = ['EMPLOYEE_ID ', 'FIRST_NAME', 'LAST_NAME', 'EMAIL',
                       'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY',
                       'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']

print(employees_7)

#%%

# 4. Write a Pandas program to select distinct department id from employees file.

d_id = pd.DataFrame({"DEPARTMENT_ID": data.iloc[43:150, 11]})
department_id = d_id.set_index(np.arange(len(d_id)))

print(department_id)


#%%

# 5. Write a Pandas program to display the first, last name, salary and department number
#    for those employees whose first name starts with the letter 'S'

df = data.iloc[43:150, [2, 3, 8, 11]]
df = df.set_index(np.arange(len(df)))
df.columns = ['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']

pattern = 'S\w+'
df_names_start_with_S = df[df['FIRST_NAME'].str.contains(pattern)]

print(df_names_start_with_S)


