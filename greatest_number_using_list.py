num1  = int(input("Enter first numnber: "))
num2  = int(input("Enter second numnber: "))
num3  = int(input("Enter third numnber: "))
num4  = int(input("Enter fourth numnber: "))

# Example of list
list1 = [num1,num2,num3,num4]
list1.sort()

# Example of set
set1 = {num1,num2,num3,num4}
print('List of your enterd values:\n ', list1)
print("this is a set of your values:\n", set1)
print("the greatest number among",list1," is: ",list1[-1])



