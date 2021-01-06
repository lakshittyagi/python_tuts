import numpy as np

# Addition
myArr = np.arange(1,11)
print(myArr) #[1 2 3 4 5 6 7 8 9 10]
addition =  myArr + myArr
print(addition) # [2 4 6 8 10 12 14 16 18 20]

# Addition with a value
myArr1 = myArr + 100
print(myArr1) # [101 102 103 104 105 106 108 109 110]

# Subtraction
subtraction = myArr1 - myArr
print(subtraction) # [100 100 100 100 100 100 100 100 100 100]

# subtraction with a vlaue
print(subtraction - 50) # [ 50 50 50 50 50 50 50 50 50 50]

# Multiplications - we cannot multiply arrays

# Division
n1 = np.arange(1,6)
n2 = np.arange(6,11)
print(n1/n2)
n3 = n2/n1
print(n3)

# Divison by 0 will throw a warning. but program continues to run.

# Power

arr = np.arange(1,11)
print(arr) # [ 1 2 3 4 5 6 7 8 9 10]
print(arr ** 2) # [ 1 4 9 16 25 36 49 64 81 100 ]


