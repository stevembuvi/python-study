first_name="Steve"
last_name="Mbuvi"

full_name=first_name+" "+last_name
print(full_name)

num1="100"
num2="200"

total=num1+num2
print(total)
#when we add swtrings they contcat(join together) instead of summing up

#indexing and slicing
#indexing used to when accessing characters in a string
#Every character in string variable has a numeric representation
#starting on the left we startwith 0
#starting on the right we start with -1

text="I am a software developer"
print(text[3])
print(text[-5])

#display t and e from software
print(text[10])
print(text[-11])
#slicing
#=>slicing is extracting a part of a string using indexing
#[starting_index:end_index+1]
#display software
print(text[7:14+1])
#display developer
print(text[16:25])

text1="I am Student doing Software Development and we are learning Python Programming"
#display software developmnent
print(text1[19:39])
#display Pyton Programing
print(text1[60:78])
#display I am a Student
print(text1[0:12])

#len() used to count the number of all characters in a string
print(len(text1))