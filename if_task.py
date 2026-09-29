#Take three inputs from a user, separately. Print the largest of the numbers.
    #Hint: Determine what type of data is taken in as input.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if num1>num2 and num1>num3:
    print("The largest number is:", num1)
elif num2 > num1 and num2 > num3:
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

#Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".
if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")

#Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".
if len(str1) > len(str2):
    print("str1 is longer")
elif len(str2) > len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")

#Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
    #Prints "Access Granted" if user_id is in valid_ids.
    #Prints "Access Denied" if user_id is not in valid_ids.
if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")

#Given a variable value that could be of any type, write a conditional statement that:
    #Prints "String Detected" if value is a string.
    #Prints "Integer Detected" if value is an integer.
    #Prints "Unknown Type" for any other type.
if type(value) == str:
    print("String Detected")
elif type(value) == int:
    print("Integer Detected")
else:
    print("Unknown Type")



