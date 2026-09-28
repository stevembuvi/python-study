#Take three inputs from a user, separately. Print the largest of the numbers.
    #Hint: Determine what type of data is taken in as input.
num1 = int(input("28: "))
num2 = int(input("18: "))
num3 = int(input("40: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=34

if temp>30:
    print('The temperature is too high')
elif temp>15:
    print('Normal temperature')
else:
    print('Cold temperature')

#Write a Python program that checks if a variable x is between 10 and 20 (inclusive) ,and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x=11
y=30
if 10<=x<=20 and y>100:
    print('Conditions Met')
else:
    print('Conditions not met')

#Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password="secret123"
if password =="secret123":
    print('Access granted')
else:
    print('Access denied')
