#Custom functions
#They dont add logic
#Arrange code into reusable blocks
#A function is a block code that performs a certain task.

#Creating Custom Functions
#Define the function using the def key word
#Followed by name

       #Syntax
    #def function_name():
       #block of code

def triangle_area():
    base=20
    height=30
    area=0.5*base*height
    print(area)

triangle_area()

def hello(name):
    print(f'Hello{name}')
hello('Steve')
hello('Alex')
def circle_area():
    pi=3.14
    radius=20
    area=pi*radius**2
    print(area)

circle_area()

#calclulate area of a square
def square_area():
    length=30
    area=length*length
    print(area)

square_area()

#parameters->variables used inside the function
#arguments->exact values passed when calling the function.

#create a function that calculates the area of a rectangle
def rectangle_area():
    length=15
    width=20
    area=length*width
    print(area)

rectangle_area()

#Class slide 66