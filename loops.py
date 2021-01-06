fruits = ['Banana','Apple','Orange','Grapes','Kiwi']    


# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# for loop
for fruit in fruits:
    print(fruit) 
# another way to for loop
for i in range(len(fruits)):
    print(fruits[i]) 
# for loop with step size    
for i in range(0,len(fruits),2): 
    print("\n",fruits[i])  

# for loop with else    
for i in range(10):
    print(i)
else: 
    print("This is inside for loop",i)  

# Break statement in for loop      

for i in range(10):
    print(i)
    if i == 5:
        break
# continue statement

for i in range(10):
    if(i == 5):
        continue
    print(i)
       