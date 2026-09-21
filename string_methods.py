my_name="stephen MBUVI"
my_name.capitalize()
#capitalize  ->make the first character have upper case and the rest lower case 
print(my_name.capitalize())

# lower and upper
# .lower(converts string characters to lower case) , .upper(converts string characters to upper case)
text1= "MY name is STEVE"
print(text1)
text2=text1.lower()
print(text2)
text3=text1.upper()
print(text3)

#strip ->used to remove leading and trailing spaces

text4="  I am a student    "
print(text4)
print(len(text4))
text5=text4.strip()
print(len(text5))

#clean sentence to "Python programming"
sentence1="    PYThon ProgrammING"
sentence1=sentence1.strip()
print(sentence1)
sentence1=sentence1.capitalize()
print(sentence1)

#clean sentence2 to "SOFTWARE DEVELOPMENT"
sentence2="Software DEVELOPMENT    "
sentence2=sentence2.strip()
sentence2=sentence2.upper()
print(sentence2)

#clean sentence3 to "computer science"
sentence3="     COMPUter ScieNCE    "
sentence3=sentence3.strip()
sentence3=sentence3.lower()
print(sentence3)

#replace -.used to replace a character in a string

sentence4="i am a python Developer"

sentence4=sentence4.replace('python','Java')
print(sentence4)
#clean to "i am a Developer"
sentence4=sentence4.replace('python','')

#count->used to count the appearance of a character in a string

sentence4="i am a python Developer"
print(sentence4.count('e'))

#verify an email address is correct
email="stevembuvi@gmail@.com"
print(email.count('@'))

#split ->used to split a string using a character
sentence4="i am a python Developer"
sentence5=sentence4.split('p')
print(sentence5)

#change sentence6 to Stephen Mutiso
sentence6="Stephen Mbuvi"
sentence6=sentence6.replace('Mbuvi','Mutiso')
print(sentence6)

#count the number of times o has appeared
sentence7="Python programming"
print(sentence7.count('o'))

#split sentence8 using the colon
sentence8="Stephen:Mbuvi:blessing:mutanu"
sentence8=sentence8.split(':')
print(sentence8)