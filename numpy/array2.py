# other numpy array methods.
import numpy as np


# Linspace - is ued to create a equaly displaced number with an starting and end point.
lint = np.linspace(1, 2, 5)  # it will create [1.   1.25 1.5  1.75 2.  ]
print(lint)

# create a arrray of zeros

# one dimensional array with 4 zero elements.
zeros = np.zeros(4)
print(zeros)  # [0. 0. 0. 0.]
# two dimensional array with 1 rqw and 4 colums elements.
zeros2 = np.zeros((2, 4))
print(zeros2)  # [[0. 0. 0. 0.]
#                [0. 0. 0. 0.]]


# array of 1's
one1 = np.ones(5)
print(one1)

# A matrix with 3 rows and three colums with each element = 1
one2 = np.ones((3, 3))
print(one2)

# identity matrix using numpy
identMatrix = np.eye(4)  # A 4x4 identity matrix.
print(identMatrix)

# random int using numpy

randNumber = np.random.randint(50,60) 
# between 50 to 60, 60 is exclusive
print(f"\n The random integer is : {randNumber}")

# geting an array of random numbers using numpy randint

arrayOfRandomInt = np.random.randint(1,50,10) # array of 10 elemnts range between 1 to 50
print(arrayOfRandomInt) # ([10,30,45,12,32,18,44,29,31,27])
# max value in an array and index of it.
print(f" Index - {arrayOfRandomInt.argmax()} Value - {arrayOfRandomInt.max()}")
# min value in an array and index of it.
print(f" Index - {arrayOfRandomInt.argmin()} Value - {arrayOfRandomInt.min()}")

# datatype

nums = np.arange(0,10)
print(nums.dtype) # int32