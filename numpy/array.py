import numpy as np
arr = np.arange(0,25) # arange method is ued to create an array with an starting and ending elements. we can also provide step size like this. arr = np.arange(0,10,2) and it will generate [0,2,4,8]
print(arr)
list1 = [1,2,3,4,5]
arr1 = np.array(list1) # array method can convert a python list into an array
print(arr1)
matrix = arr.reshape(5,5) # reshape method is used to convert an array into a two dimensional array or a matrix.
print(matrix)
print(matrix[4,4]) # By using this syntax we can access a particular element of the martix. here 4,4 is the position of element in the matrix.

def generator():
    '''       
       Generator method is defind for generating an array of numbers. it ask for array length when you use it.

       It is basically a multiline comment. but it used to describe the use of the method. whenever you hover on this method it will provide you this
    '''
    num = int(input('Enter number of elements you want in your array: '))
    arr = np.arange(0,num)
    return arr
myArray = generator()
myArray = myArray.reshape(5,5)
print(myArray)
