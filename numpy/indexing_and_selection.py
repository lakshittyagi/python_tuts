import numpy as np

myArr = np.arange(1,11)
print(myArr)
print(myArr[2]) # geting the value at index 2, wich will be 3.
myArr[2] = 5 # by this way we can reassign a value to the index 2.
print(myArr)
print(myArr[2])
myArr1 = myArr.reshape(2,5)
print(myArr1) # it will give an two dimensional matrix.
print(myArr)  # it remain the same 1 dimesional array.
print(myArr[0:4]) # it will get elements from 0 to 4. index 4 will be excluded. output [1,2,5,4]
print(myArr[4:]) # it will get all elemnts from index 4 to the end of the array. [5,6,7,8,9,10]

# make an instance of the Array. An instance of an array is not the another array.
myArr2 = myArr[0:5]
print(myArr2) # [1,2,5,4,5]

# but if i change myArr2 the changes will deflect in myArr too. lets see
myArr2[1] = 100
print(myArr2) # [1,100,5,4,5]
print(myArr) # [1,100,5,4,5,6,7,8,9,10]

# create a copy of an array

myArr3 = myArr.copy()
print(myArr3) # [1,100,5,4,5,6,7,8,9,10]


# geting elemnts of 2-d array
myarr4 = np.arange(0,25)
myarr4 = myarr4.reshape(5,5)
print(myarr4) 
print(myarr4[2][2]) # 12
# another way
print(myarr4[2,2]) # 12
myarr4[2,2] = 1000 # reassign value.
print(myarr4[2,2]) # 1000
# 2d Array slicing
print(myarr4[0:2,1:])