maths = int(input('Enter Maths Marks: '))
physics = int(input('Enter physics Marks: '))
chemestry = int(input('Enter chemestry Marks: '))
english = int(input('Enter English Marks: '))
hindi = int(input('Enter Hindi Marks: '))

total = maths + physics + chemestry + english + hindi
avg   = total/5
if(avg > 90 and avg < 100):
    print('Your got A+ grade')
elif(avg > 80 and avg < 90):
    print('You got A grade')
elif(avg>60 and avg < 80):
    print('You got B+ grade')
elif(avg>50 and avg < 60):
    print('You got B grade')
elif(avg>35 and avg < 50):
    print('You got C grade')
else:
    print('You are failed')                    