#Write a program that displays a numbers 1 to 50 inside a list.
lst = list(range(1, 51))
display = []

for i in lst:
    display.append(i)

print(display)

#From 1 above display the ones divisible by 7 or 5 inside a list.
lst = list(range(1, 51))
divisible = []

for i in lst:
    if i%5==0 or i ==0:
        divisible.append(i)

print(divisible)

#Find sum and average of values in the range between 10 to 40
lst1 = list(range(10, 41))
sum=0
for i in lst1:
    sum=sum+i
print(sum)

average=sum/len(lst1)
print(average)
#Put in a list the first 10 odd numbers between 10 to 50.
lst2 = list(range(10, 51))
odd = []

for i in lst2:
    if i % 2 != 0:
        odd.append(i)
    if len(odd) ==10:
            break
print(odd)

#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop
lst3 =input(range(1,10))

user_input=input('Enter numbers')
user_input=int(user_input)
for i in lst3:
    mult=user_input*i
    print(f"{user_input}*{i}={mult}")

#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop


#ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#Display the total quantity of the 3 above.
ls1 = [ ("Jay", "20"), ("Mo", "30"), ("Mya", "32") ]
total_quantity=0
for i in ls1:
    quantity=int(i[1])
    total_quantity=total_quantity+quantity
print(total_quantity)
                        

#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
correct_password = "admin@123"

for attempt in range(4):
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password try again.")

else:
    print("Account is blocked.")

