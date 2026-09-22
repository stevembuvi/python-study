#Tuples
#Just like lists tuples store multiple items that can be of any data type
#items are ordered(have index)
#Items in a tuple are immutable(cannot be changed)
#All tuples belong to class tuple

fruits=('Mango','Oranges','Bananas','Lemons','Grapes')
print(fruits)
print(type(fruits))
#display bananas
print(fruits[2])
#slicing - display oranges,bananas and lemons
print(fruits[1:4])

#to modify an item in a tuple ---convert to list using list()
fruits=list(fruits)
print(fruits)
#modify
#change bananas to straw berries
fruits[2]="Strawberries"
print(fruits)
#add watermelon at end of the list
fruits.append('watermelon')
print(fruits)
#convert back to tuples using tuple()
fruits=tuple(fruits)
print(fruits)
print(type(fruits))

days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
#find Wednesday using index
print(days[2])
#Using a function find the length of the tuple
print(len(days))
#Replace Thursday with Thur
days=list(days)
print(days)
days[3]="Thur"
print(days)
#convert back to tuples
days=tuple(days)
print(days)