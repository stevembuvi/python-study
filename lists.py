fruits=['mango','banana','orange','lemon','avocado']
print(fruits)
print(type(fruits))

#updating items using index
#replace orange with pixel
fruits[2]='pixel'
print(fruits)

#indexing and slicing
#indexing
print(fruits[2])

#list methods
#updating items
#append
fruits.append('strawberries')
fruits.append('watermelon')
print(fruits)

#insert 
fruits.insert(0,'apple')
print(fruits)

#slicing->extracting a part of a list - Display lemon
#[start_index:end_index+1]  
print(fruits[1:4])
print(fruits[2:5])

#remove items
fruits.remove('banana')
print(fruits)

#create a list of days of the week
week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
#display the day today
print(week[0])
#display the saturday
print(week[-2])
#display tuesday to friday
print(week[1:5])

#Updating lists
#update thursday to thur
week[3]='thur'
#add january to the end of the list

week.append('january')
week.insert(2,'december')
print(week)

#delete friday from the list 
week.remove('friday')
print(week)
#delete the last item on the list
week.remove('january')
print(week)
#delete the item at index 1
week.remove('tuesday')
print(week)
#delete all items from the list
week.clear()
print(week)
