"fruits"= {"Mangoes","Oranges","Bananas","Lemons","Grapes"}

print("fruits")
print(type("fruits"))

# add
"fruits".add('strawberries')
print("fruits")

# remove or discard
"fruits".remove('Bananas')
print('fruits')

# sets.py - Python Sets Practice

# --- QUESTIONS ---

# Q1. Create a set
my_set = {10, 20, 30, 40, 50}
print("Q1 Original set:", my_set)

# Q2. Add element 60 to the set
my_set.add(60)
print("Q2 After adding 60:", my_set)

# Q3. Remove element 20 from the set
my_set.discard(20) # discard doesn't throw error if not found
print("Q3 After removing 20:", my_set)

# Q4. Given two sets, find union, intersection, difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("\nQ4 A:", A, "B:", B)
print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference A-B:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

# Q5. Check if an element exists
fruits = {"apple", "banana", "cherry"}
print("\nQ5 Is banana in fruits?", "banana" in fruits)

# Q6. Remove duplicates from a list using set
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_numbers = list(set(numbers))
print("\nQ6 List with duplicates:", numbers)
print("After removing duplicates:", unique_numbers)

# Q7. Count unique words
sentence = "python is easy and python is powerful"
unique_words = set(sentence.split())
print("\nQ7 Unique words:", unique_words)
print("Count:", len(unique_words))