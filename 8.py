# Return value from function
# First without return
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8

# Now with return
def add(a, b):
    return a - b

result = add(5, 3)
print(result)
print(result * 2)

# Using multiple returns
def check(num):
    if num/2 == 0:
        return "Even"
    else:
        return "Odd"
print(check(5))