import pandas as pd
import numpy as np

lst = [10,20,30]
lst1 = ['a','b','c']
arr = np.array(lst)
dict1 = {'name': 'lakshit','age':24,'role': 'devloper'}
# creating a series

mySeries = pd.Series(data= lst, index= lst1)

print(mySeries['a']) # Now we can access elements using our defined index just like a dictionary in python.

# create series from a numpy array
print(pd.Series(data=arr,index=lst1))

# create a series from a dictionary
print(pd.Series(data=dict1))

# Adding two series
ser1 = pd.Series([1,2,3],['a','b','c'])
ser2 = pd.Series([4,4,6],['a','b','d'])
print(ser1+ser2) # a => 5.0 , b => 6.0 , c => NaN , d = Nan