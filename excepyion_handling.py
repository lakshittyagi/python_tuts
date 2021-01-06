
   
import datetime

def add(num1,num2):
    try:
        a = int(num1) + int(num2)
        print(a)
        b = int(num1)/int(num2)
        print(b)
        method()
    # except Exception as e:
    #     print('something went wrong')
    #     with open('eroor.log','a') as f:
    #         f.write(f'{datetime.datetime.now()} - {str(e)}\n') 
    #     method()    
    except ValueError as e:
        print('Please enter numbers, Strings are not supported')
        with open('eroor.log','a') as f:
            f.write(f'{datetime.datetime.now()} - {str(e)}\n')
        method()    
            
    except ZeroDivisionError as e:
        print('Cannot devide by zero')
        with open('eroor.log','a') as f:
            f.write(f'{datetime.datetime.now()} - {str(e)}\n') 
        method()



def method():
    num1 = input('Enter first Number: ')
    num2 = input('Enter 2nd Number: ')
    add(num1,num2)

method()    
