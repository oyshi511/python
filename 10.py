import math

num = input("Enter a number: ")
num = float(num)
print("Root", math.sqrt(num))
print("Power", math.pow(num,2))
print("Decimal more than or equal",math.ceil(num))    # Round up 
print("Decimal less than or equal", math.floor(num))   # Round down → 2
print("Pi value", math.pi)
print("e value", math.e)
print("Logarithm base e", math.log(float(num)))       # Natural logarithm

num2 = float(input("Enter circle radius: "))
area = math.pi * math.pow(num2, 2)
print("Area of the circle is: " , round(area, 3))