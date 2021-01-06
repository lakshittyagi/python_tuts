import numpy as np
import pandas as pd

# dataframe
arr = np.random.randn(5,4)
print(arr)
df = pd.DataFrame(arr,['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# geting single coloumn of dataframe as a series
print(df['W'])
# OR
ser1 = df['W']
print(ser1['A']) # by using key
for index,item in enumerate(ser1): # By using for loop
    print(f"{index} : {item}")
# OR
print(df.W)

# Adding Coloum's of DataFrame
df['sum'] = df['W'] + df['X'] + df['Y'] # can be continue till end of the coloumns.
print(df) # it will have a new coloum called sum with the data it gets from addition.

# Removing a Coloumn from Data Frame.
df.drop('sum', axis=1,inplace=True) # inplace = true delete the column permanently.
print(df)

# get row of the dataframe

print(df.loc['A'])

# Selecting a single element from the table
print(df.loc['A','Z'])

# selecting a subset
# df.loc[[rows],[coloums]]
print(df.loc[['A','B'],['X','Y']])