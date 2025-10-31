fruits = ["Banana", "Mango", "Watermelon", "Orange"]
print(fruits)
print(type(fruits))
print(len(fruits))
print(fruits[0])  # Accessing the first element
print(fruits[1])  # Accessing the second element
print(fruits[2])  # Accessing the third element
print(fruits[3])  # Accessing the fourth element
print(fruits[-1]) # Accessing the last element
fruits[0] = "Cherry"  # Modifying the first element
fruits.append("Pineapple")  # Adding a new element at the end
print(fruits)
for fruit in fruits:
    print("I like", fruit)

fav_comics = ["The broken ring", "Ominous Reader Viewpoint", "Pick me up"]
print(fav_comics)
for fav in fav_comics:
    print("My favorite comic is", fav)