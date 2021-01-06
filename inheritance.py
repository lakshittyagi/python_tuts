# Multi-Level Inheritance
class Person:
      def __init__(self,name,gender,yearOfBirth):
          self.name = name
          self.gender = gender
          self.yearOfBirth = yearOfBirth
      def calcAge(self):
          return 2021 - self.yearOfBirth      

class Employee(Person):
    def __init__(self):
        print('Hello, I am an Employee')
    def getSalary(self):
          print(f"Your salary is $50000")    


class Manager(Employee):
      def __init__(self):
          print('I am a Manager')

class Programmer(Employee):
    def __init__(self):
        print('Helo, I am a programmer')
class Peon(Employee):
    def __init__(slef):
        print('Hello, I am a Peon')
manager = Manager('lakshit','male',1998)
manager.getSalary() 


programmer = Programmer('Ankit','male',1888)
programmer.getSalary()


peon = Peon('sourabh','male',1970)
peon.getSalary()
