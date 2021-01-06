def Employee(name,age,profession,salary):
    person = {
        'name': name,
         'age': age,
         'profession': profession,
         'salary': salary
    }
    return person

name = input("Enter Name: ")
age  = int(input("Enter Age: "))
profession = input("Enter profession: ")
salary = int(input("Enter salary: "))

# Employee1 = Employee(name,age,profession,salary)
Employee2 = Employee(name,age,profession,salary)

# print(Employee1)
print(Employee2)

