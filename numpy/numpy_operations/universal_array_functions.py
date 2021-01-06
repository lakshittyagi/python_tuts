import numpy as np

# Universal Array methods

# 1. np.sqrt - It used to find square root of the whole array. Lets see.
arr = np.arange(1,11)
print(arr)
print(np.sqrt(arr))

# 2. np.exp - It is used to calculate the expo values of whole array
print(np.exp(arr))

# 3. Trignometry functions
print(np.sin(arr)) # sin values
print(np.cos(arr)) # cos values

# 4. np.log - used to calculate logrithem
print(f'Log values of {arr} : {np.log(arr)}')

# sum of the array elements
print(sum(arr)) # we can use np.sum() and sum() 