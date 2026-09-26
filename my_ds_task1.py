# PYTHON DATA STRUCTURES CHALLENGE
# Create a file called my_ds_task1.py and attempt the questions below

my_ds = [45,"Kevin",(720,),["Lesson","Python",{"currency": "KES","student": {"name": "James",
    "age": 23},"subjects": ["Python", "SQL", "HTML", "CSS"]}],834,(91, "Mary", ["HTML", "CSS", "JavaScript"])
]
# 1. Print KES.
print(type(my_ds))
print(my_ds[3][2]["currency"])
# 2. Print 720 from the tuple.
print(my_ds[2][0])
# 3. Print Python from the nested list.
    #my_ds[3] gives the nested list
    #[1] gives the item at index 1 in the nested list
print(my_ds[3][1])
# 4. Print the student's name "James". 
    #my_ds[3] gets the nested list
    #my_ds[3][2] gets the dictionary
    #["student"] gets the student dictionary
    #["name"] gets "James"
print(my_ds[3][2]["student"]["name"])
# 5. Print SQL from the subjects list inside the dictionary.
     #[subjects] gets to subject list and [1] gets "SQL"
print(my_ds[3][2]["subjects"][1])
# 6. Print HTML from the subjects list inside the dictionary.
print(my_ds[3][2]["subjects"][2])
# 7. Add a new key called "amount" to the dictionary with a value of 1500.
     #my_ds[3] gets the nested list
     #[2] gets the dictionary
     #["amount"] creates the new key
     #= 1500 assigns the value 1500
my_ds[3][2]["amount"]= 1500
print(my_ds[3][2])
# 8. Change the student's name from "James" to "Brian".
   #my_ds[3] gets the nested list
   #[2] gets the dictionary
   #["student"] gets the student dictionary
   #["name"] selects the name
   #= "Brian" changes the name
my_ds[3][2]["name"]="Brian"
print(my_ds[3][2])
# 9. Add "Django" to the end of the subjects list.
my_ds[3][2]["subjects"].append("Django")
print(my_ds[3][2]["subjects"])
# 10. Change "CSS" in the subjects list to "Bootstrap".
my_ds[3][2]["subjects"][3]=("Bootstrap")
print(my_ds[3][2]["subjects"])
# 11. Print 834 reversed as 438.
#     Do not use an inbuilt reverse method.
#     Do not manually assign 438.
#     Hint: Convert the number to a string and use [::].
         #my_ds[4] gets 834
         #str(my_ds[4]) converts 834 to "834"
         #[::-1] reads the string backwards
print(type(my_ds[4]))
my_ds[4]=str(my_ds[4])
print(str(my_ds[4])[::-1])
# 12. Print "Mary" from the last tuple.
print(my_ds[5][1])
# 13. Print "JavaScript" from the list inside the last tuple.
print(my_ds[5][2][2])
# 14. Change "JavaScript" to "React".
my_ds[5][2][2]="React"
print(my_ds)
# 15. Print the entire updated my_ds.
print(my_ds)
# BONUS CHALLENGE
# Print the following individually:
# Currency: KES
print("Currency", my_ds[3][2]["currency"])
# Amount: 1500
    #my_ds[3] gets the nested list
    #[2] # gets the dictionary
    #["amount"] # gets the value 1500
print("Amount" , my_ds[3][2]["amount"])
# Student: Brian
print("Name" , my_ds[3][2]["name"])
# Subject: Django
print("Subject:" , my_ds[3][2]["subjects"][4])
# Technology: React
print("Technology:", my_ds[5][2][2])
#
# You can research or discuss with your classmates to find the solutions.