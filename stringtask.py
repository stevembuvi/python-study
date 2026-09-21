#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class :name = “  JOHn  .“ to “john”

name="   JOHn   "
name=name.strip()
print(name)
name=name.capitalize()
print(name)

#Slice to display "Breed is German"
sentence_one="The Dog Breed is German Shephered"
sentence_one=sentence_one.replace('The Dog Breed is German Shephered','Breed is German')
print(sentence_one)

#Slice to display "Clinton forces"
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
sentence_two=sentence_two.replace('Defeats for the Clinton forces, this was her moment of triumph','Clinton forces')
print(sentence_two)

#Split the below sentence using a semicolon i.e ; And display length of the result. 
text="The lazy dog;ran so fast; it hit the wall."
text=text.split(';')
print(text)
print(len(text))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
fisrt_name="Joh.n"
last_name="Do,e" 
fisrt_name=fisrt_name.replace('Joh.n','John')
last_name=last_name.replace('Do,e','Doe')
full_name=fisrt_name+' '+last_name
print(full_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r='["E","W","C"]' 
r=r.replace('["E","W","C"]','EWC')
print(r)