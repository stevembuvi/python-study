
numbers=(10, 20, 30, 40, 50)
#add 60 to the end and replace 30 with 35
print(numbers)
numbers=list(numbers)
print(numbers)
numbers.append(60)
print(numbers)
numbers[2]=35
print(numbers)
numbers=tuple(numbers)
print(numbers)

values = (15, 5, 30, 25, 10) 
#arrange the elements in ascending order.
values=list(values)
print(values)
values=sorted(values)
print(values)
values=tuple(values)
print(values)

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana". 
fruits=list(fruits)
print(fruits)
print(fruits.count('banana'))
fruits.pop(1)
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop(3)
print(fruits)

names = ("Alice", "Bob", "Charlie", "David")
#Reverse the order of elements using sort method.
names=list(names)
print(names)
names.sort(reverse=True)
print(names)
names=tuple(names)
print(names)

colors = ("red", "blue", "green")
#add "yellow" at index 1
colors=list(colors)
print(colors)
colors.insert(1,"Yellow")
print(colors)
colors.append('Purple')
colors.append('Orange')
print(colors)
