students = ['Akshu','Lakshit','Aarav','Rajan','kamal']
# enumurate function
for index,student in enumerate(students):
    print(f'{index} - {student}')


# Global Keyword
# global keyword is used when we want to access a variable that is ddefined out the scope of the code block.

name = "Akshu" #global variable
def sayHello():
    # we cannot use global and local variable with the same name. if can only use either local or global.
    # to use global variable in a block we use global keyword
    global name
    print(f'Hello {name}')  # using global variable
    name = 'Lakshit'        # it will change the value of global variable.
    print(f'Hello {name}')      

sayHello()      