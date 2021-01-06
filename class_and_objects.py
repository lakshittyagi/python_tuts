class Employee:
    # class atribute
    company = "Google"
    # constructor
    def __init__(self,name,age,salary,job):
        print('I am a constructor')
        self.name = name
        self.age  = age
        self.salary = salary
        self.job = job
    # method    
    def userInfo(self):
        print(f'Name - {self.name}\n Age - {self.age}\n Salary - {self.salary}\n Job - {self.job}')
    # static method
    @staticmethod

    def goodMoring():
        print(f'Good Morning, {self.name}')    

employee1 = Employee('Lakshit',24,20000,'Engineer')
employee2 = Employee('Rajan',24,50000,'developer')
employee1.userInfo()
employee2.userInfo()
