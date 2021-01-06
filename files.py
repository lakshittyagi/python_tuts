
# read data from a file
f = open('sample.txt','r') # opening the file
data = f.read() # read function
print(data)
f.close()
# writing into a file
# writing into a file replace the file data with the data you provide
f = open('sample.txt','w')
f.write('hello, I am lakshit')
f.close()

# appending the data in a file

# person is a dictionary
person = {
    'name': 'Lakshit',
    'email': 'tyagi@gmail.com',
    'profession': 'Teacher'
}

f = open('sample.txt','a')
# f.write('\nWelcome\n\t to my youtube channel')
f.write(f'\n {person}')
f.close

# with statement to automatically close the files

with open('another.txt','w') as w:
     a = w.write('hello world')
