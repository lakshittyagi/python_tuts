import numpy as np

# boolean array

myArr = np.arange(1,11)
print(myArr)
test = myArr < 5
print(test) # return true where the array element is smaller then 5 and return false where array element is bigger then 5.

# we can slice an array by comparision operator
myArr1 = myArr[myArr<5]
print(myArr1) # [1 2 3 4]