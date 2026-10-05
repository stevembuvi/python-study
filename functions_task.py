#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print("The area of the triangle is:", area)

#Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
   #Hint: how does an even / odd number react differently when divided by 2?
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")

#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
 #e.g if a user enters “0712345678”, the program should display “+254712345678”
 #e.g if a user enters “0112345678”, the program should display “+254112345678”
 #e.g if a user enters “712345678”, the program should display “+254712345678”

phone = input("Enter phone number: ")

if phone.startswith("07") or phone.startswith("01"):
    phone = "+254" + phone[1:]
elif phone.startswith("7") or phone.startswith("1"):
    phone = "+254" + phone
elif phone.startswith("254"):
    phone = "+" + phone
elif phone.startswith("+254"):
    phone = phone
else:
    print("Invalid number")
print(phone)

#Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
      #Hint: Check if it contains an “@” symbol and “.” symbol.
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
    #The goal of this exercise is to think about some internals that programs normally take care of for us. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
password = "admin@123"
attempts = 0

while attempts < 4:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access granted")
        break
    else:
        print("Wrong password")
        attempts += 1

if attempts == 4:
    print("Account blocked")

#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks = int(input("Enter student marks: "))

if marks > 79:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade E")

#Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
#Example If rows is 5, it should print the following:
#*
#**
#***
#****
#*****.....
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
prods = [
    ["omo", "30kshs", "300"],
    ["milk", "50kshs", "200"],
    ["bread", "45kshs", "359"],
    ["coffee", "5kshs", "79"]
]
total = 0

for product in prods:
    total += int(product[2])

print("Total stock:", total)

#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.datetime
from datetime import date

dob = input("Enter your date of birth (YYYY-MM-DD): ")

year, month, day = map(int, dob.split("-"))
birth_date = date(year, month, day)
today = date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12
print("Age:", years, "years,", months, "months,", days, "days")

#Write a program that prints the largest of 4 inputs taken as input from a user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
print("The largest number is:", largest)

#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
correct_email = "admin@mail.com"
correct_password = "Admin@123"

tries = 0

while tries < 3:
    email = input("Enter email: ")
    password = input("Enter password: ")
    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
        tries += 1
if tries == 3:
    print("You have been blocked")

#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Sum:", num1 + num2)
        break

    except ValueError:
        print("invalid character entered")
        print("Please enter numbers only.")

For example:

Enter first number: 10
Enter second number: 5.5
Sum: 15.5

If the user enters 10abc, it displays "invalid character entered" and asks for the inputs again.

#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK:  
basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

gross_salary = basic_salary + benefits

if gross_salary <= 5999:
    nhif = 150
elif gross_salary <= 7999:
    nhif = 300
elif gross_salary <= 11999:
    nhif = 400
elif gross_salary <= 14999:
    nhif = 500
elif gross_salary <= 19999:
    nhif = 600
elif gross_salary <= 24999:
    nhif = 750
elif gross_salary <= 29999:
    nhif = 850
elif gross_salary <= 34999:
    nhif = 900
elif gross_salary <= 39999:
    nhif = 950
elif gross_salary <= 44999:
    nhif = 1000
elif gross_salary <= 49999:
    nhif = 1100
elif gross_salary <= 59999:
    nhif = 1200
elif gross_salary <= 69999:
    nhif = 1300
elif gross_salary <= 79999:
    nhif = 1400
elif gross_salary <= 89999:
    nhif = 1500
elif gross_salary <= 99999:
    nhif = 1600
else:
    nhif = 1700

print("Gross salary:", gross_salary)
print("NHIF:", nhif)