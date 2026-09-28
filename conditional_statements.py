#Conditional Statements =>Used to make decisions based on a result of a certein condition
#Conditions are crested using comarison operators(<,>,==,<=,>=,!=)
#Conditions returns Booleans
#Python uses three primary key words on conditional statements(if,else,elif)

              #if statements
#Executes a block of code only when the condition is true
              #Sytntax
     #if condition:
              #block of code
if 20>10:
    print('twenty is greater')

age=30
if age>18:
    print('Adult')
#authorize users from 18 to 60 years to access website
age>=18
age<=60
if age>=18 and age<=60:
    print('Allow access')

#check if the temperature is above 30 print too hot
temp=34
if temp>30:
    print('Too Hot')
#if else statement
#->Else statement executes ehen the statement is false
  #else cannot exist without if
           #Syntax
        #if condition:
            #if block
        #else:
            #else block

#print pass if student marks is above 50 otherwise fail
marks=58

if marks>50:
    print('Pass')
else:
    print('Fail')

#if-elif-else ->to check multiple conditions with different outcomes
#print pass if student marks is above 70 ,  print Average if mark is 50 to 70 otherwise fail

if marks>70:
    print('Pass')
elif marks>=50 and marks<=70:
    print('Average')
else:
    print('Fail')

#Print Senior Adult if age is above 50, print adult if age is above 20, print teenager if the age is above 12, otherwise print child.
age=10

if age>50:
    print('Senior Adult')
elif age>20:
    print('Adult')
elif age>12:
    print('Teenager')
else:
    print('Child')

#Print A if marks is above 80
#Print B if marks is above 70
#Print C if marks is above 60
#Print D if marks is above 50
#otherwise print E

marks=52

if marks>80:
    print('A')
elif marks>70:
    print('B')
elif marks>60:
    print('C')
elif marks>50:
    print('D')
else:
    print('E')

#Class Task: Slide 56. 1 – 4
                 # Slide 58. All
                 # Slide 59. 3 – 4

