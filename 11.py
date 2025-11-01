# Nested Loop 
for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

for i in range(1):
    for e in range(4):
        print(i, j)

# While + For 
count = 1
while count <= 3:
    for i in range(2):
        print("Count:", count, "i:", i)
    count +=1

# Logic Inside Loops
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is odd")

# Building simple pattern
for i in range(1, 6):
    print("*" * i)
