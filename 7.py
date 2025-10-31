# Learning about Functions in Python 
def greet():
    print("Learning about Functions")
greet()
# def means define a function
# great is the name of the function
# () indicates that this function does not take any parameters=input. Everything indented (inside the function) runs when you call it. If i write anything that will work as variable inside the brackets it will be treated as parameter.
# To call the function, you just write its name followed by parentheses: great()

# Function with parameters=input
def greet_person(name):
    print("Hi", name,"!")
greet_person("Rose")


# Function that returns a value
def add(a,b):
    return a + b
result = add(3,5)
print("The sum is:", result)


# Practice Exercise:
# Task 1
def introduce():
    print("My name is Rose.")
    print("I am learning Python.")
    print("Functions make coding easy!")

introduce()

# Self discovery
def hey():
    print("Hey there you maggot!")
hey()

def new(namay):
    print("Hello", namay)
new("Rose")
new("Mishma")

# Task 2
def num(x,y):
    return (x * y)*100
output = num(5, 5)
print("The result is:", output)

def food(items):
    print("I like this ", items)
food("Pizza")
food("Burger")