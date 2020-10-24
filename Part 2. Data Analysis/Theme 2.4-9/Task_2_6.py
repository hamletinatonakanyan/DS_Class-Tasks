import numpy as np
import pandas as pd
import re

#%% md

           # Reading data and dividing file to 2 dataframes

#%%

data_ex1 = []
data_ex2 = []

with open('data copy.csv', 'r') as out:
    reader = out.readlines()
    for row in reader[2:8]:
        row = re.split('\s+', row)
        data_ex1.append(row)

    for row in reader[11:24]:
        row = re.split('\s+', row)
        data_ex2.append(row)


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


#%% md

                        # Fist DataFrame

#%%

# Cleaning data from empty columns, setting column names
df_ex1 = pd.DataFrame(data_ex1)
df_ex1 = df_ex1.drop(10, axis=1)
df_ex1.columns = ['school', 'school_index', 'class', 'name', 'surname',
                  'date_Of_Birth', 'age', 'height', 'weight', 'adress']

# Cleaning column's values from symbols
adress_values = []

clean_from_symbols(df_ex1['adress'], adress_values)
df_ex1['adress'] = adress_values

print(f'\nFirst data\n{df_ex1}')



#%% md

                        # Second DataFrame

#%%

# cleaning dataframe from empty columns and rows, setting indexes and column names
df_ex2 = pd.DataFrame(data_ex2)
df_ex2 = df_ex2.drop([0, 6], axis=1)
df_ex2 = df_ex2.drop(0, axis=0)
df_ex2.columns = ['ord_no', 'purch_amt', 'ord_date', 'customer_id', 'salesman_id']
df_ex2.set_index(np.arange(len(df_ex2)))


# Cleaning column's values from symbols
id_values = []

clean_from_symbols(df_ex2['salesman_id'], id_values)
df_ex2['salesman_id'] = id_values

print(f'\nSecond data\n{df_ex2}')


#%%

# 1. Write a Pandas program to split the following dataframe into groups based on school code

print('\n-->Split the following dataframe into groups based on school code')

grouped_school = df_ex1.groupby(['school_index'])
for val in df_ex1['school_index']:
    group = pd.DataFrame(grouped_school.get_group(val))
    print(f'\n{val}\n{group}')

# group by school code and describe values
grouped_school = df_ex1.groupby(['school_index', 'school'])
grouped_school.describe()


#%%

# 2. Write a Pandas program to split the following given dataframe by school code
#   and get mean, min, and max value of age for each school


# typecast for column 'age' with numeric values from string to int.
df_ex1.age = df_ex1.age.astype('int32')

# grouping schools and counting for each one min, max, mean values of age column
spec_data = df_ex1.groupby('school_index').agg({'age': ['min', 'max', 'mean']})

print(f'\n-->Mean, min, and max values by school code\n{spec_data}')


#%%

# 3. Write a Pandas program to split the following given dataframe into groups based on school code and class

school_by_code_and_class = df_ex1.groupby(['school_index', 'class'])
print(f'\n-->Dataframe into groups based on school code and class\n{school_by_code_and_class.first()}')


#%%

# 4. Write a Pandas program to split the following given dataframe into groups based on school code and cast grouping as a list

school_by_code_and_class = df_ex1.groupby(['school_index', 'name', 'surname'])
school_lst = list(school_by_code_and_class)
print(f'\n-->Dataframe based on school code and cast, grouping as a list\n{school_lst}')

#%%

# 5. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group.

# typecast for column 'height' with numeric values from string to int.
df_ex1.height = df_ex1.height.astype('int32')

# getting mean, min, and max values of 'class' by 'height'
height_by_class = df_ex1.groupby('class').agg({'height': ['min', 'mean', 'max']})
print(f'\n-->Mean, min, and max values by some group\n{height_by_class}')


#%%

# 6. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id)

# typecast for column 'purch_amt' with numeric values from string to int.
df_ex2.purch_amt = df_ex2.purch_amt.astype('float64').round(2)

# getting the mean, min, and max values of 'purch_amt' group by 'customer_id'
id_by_purch = df_ex2.groupby('customer_id').agg({'purch_amt': ['min', 'max', 'mean']})
print(f'\n-->Mean, min, and max values by purch_amt\n{id_by_purch}')
