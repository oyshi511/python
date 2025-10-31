hobbies = []
for i in range(3):
    hobby = input("Enter a hobby:")
    hobbies.append(hobby)
print("Your hobbies are:", hobbies)

fav_food =[]

while True:
    food = input("What is you favorite foods? (type 'stop' to finish):")
    if food.lower() == 'stop':
        break
    fav_food.append(food)

# for i in range(3):
print("Your favorite foods are:", "," .join(fav_food))
# join() means show all items in a list without brackets.

movie = []

while True:
    mv = input("Enter your fav movies: (type 'done' to finish) (type 'remove' to delete the last movie):")
    if mv.lower() == 'done':
        break
    elif mv.lower() == 'remove':
        if movie:
            movie.pop()
            print("Last movie removed. Current list:", movie)
        else:
            print("No movies to removed.")
    else:
        movie.append(mv)

print("your fav movies are:", "," .join(movie))
