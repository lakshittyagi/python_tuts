name  = "hello, I am lakshit. And lakshit is a software developer."

length = len(name) # length of string
print(length)
find1  = name.find('lakshit')
print(find1) # find method
replaceValue = name.replace('lakshit','Abhishek') # replace method
trimName = name.strip() #trim the string 
print(trimName)
lowerCase = name.casefold() #lowercase 
print(lowerCase)
countingChar = name.count('lakshit') #counting characters
print(countingChar)
encodeName = name.encode()
print(encodeName)

number = "12345" #
isNumeric = number.isnumeric() # checking if string contains all numeric values
print(isNumeric)

# The split() method splits a string into a list.

friends = "lakshit kamal rajan divyanshu sourabh"

friendsList = friends.split();
print(type(friendsList), " - ", friendsList) 


