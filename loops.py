                     # Python Loops
#Python loops are used to perform a repetitive task multiple times until a certein condition is met.
#Python has two loop commands
   #for loop
   #while loop

#for loop
#->used ti iterate over a sequence(strings,lists,tuples)
#syntax

#for iterator in sequence:
    #block of code
#iterator->represents each item in the sequence
#block of code ->the repeated task


fruits=['mango','organges','apple','lemon','grapes']

for fruits in fruits:
    print(fruits)

numbers=[10,20,30,40,50]
for i in numbers:
    print('number')

my_list=[1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print("Steve")

#print Techcamp 100 times
#range(start,stop+1) creates a sequence of numbers

numbers=list(range(1,101))

for i in numbers:
    print('TechCamp')

#Display even numbers betwen 10 and 59

lst=list(range(10,51))

for num in lst:
    if num%2==0:
        print(num)
   
#dicplay numbers between 100 and 150 that are divisible by 5.
lst1=list(range(100,151))
divisble=[]
for i in lst1:
    if i%5==0:
        divisble.append(i)
print(divisble)

# display odd numbers btw 30 and 100

lst2=list(range(30,101))
odd=[]
for m in lst2:
    if m%2!=0:
        odd.append(m)
print(odd)

# Btwn 1 to 100 display numbers divisible by 3 and 5 in a list

lst3=list(range(1,101))
lst4=[]
for d in lst3:
    if d%3==0 and d%5==0:
        lst4.append(d)

print(lst4)


# display hello 3 times
lst5=list(range(1,4))
print(lst5)
attempts =3
for i in lst5:
    pin=input("Enter your pin:")
    correct_pin='1234'
    if pin==correct_pin:
        print("Access granted")
        break
    else:
        rem_att=attempts-i
        if rem_att==0:
            print('Account blocked')
        else:
            print(f'Wrong pin try again you have {rem_att} attempts remaining')
# break =>used to stop the loop