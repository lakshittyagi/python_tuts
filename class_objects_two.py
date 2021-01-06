# Get Employee's Salary

class Employee:
    # Class Atribute
    company = "Pinaka Consulting Service"
    def __init__(self,name):
        self.name = name
        self.name = self.name.casefold()  # casefold() is used to convert string into lowercase.
        users = ['lakshit','rajan','kamal','divyanshu','sourabh'] # A list of employees
        if self.name in users:
            self.getSalary(self.name) # calling getSalary function with argument name.
        else:
            print('user not found!')
            self.employee()   # calling function to get the name of employee
    def getSalary(self,name):
        self.name = name
        # salary Table (dictionary)
        users = {
            'lakshit': '50000',
            'rajan': '40000',
            'kamal': '20000',
            'divyanshu': '30000',
            'sourabh': '45000'
        }
        # checking if given name is in the records
        if self.name in users:
            print(f'Name : {self.name}\nCompany:{self.company}\nsalary : {users[self.name]}')
            self.employee()
    # employee function        
    def employee(self):
        name = input('Enter Name of Employee: ')        
        employee = Employee(name)        

# creating employee object from Employee class for the first time.
name = input('Enter Name of Employee: ')        
employee = Employee(name) 
