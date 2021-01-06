num1  = int(input("Enter first numnber: "))
num2  = int(input("Enter second numnber: "))
num3  = int(input("Enter third numnber: "))
num4  = int(input("Enter fourth numnber: "))


if num1 > num2:
    greater1 = num1
else:
    greater1 = num2

if num3>num4:
    greater2 = num3
else:
    greater2 = num4
if greater1>greater2:
    print(greater1, 'is the greatest number!')
else:
    print(greater2, 'is the greatest number!')

