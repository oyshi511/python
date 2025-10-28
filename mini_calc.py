def calculator(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return  a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter operation 'add, ''subtract', 'multiply', 'divide:").lower()
# if operation == '+':
#     operation = 'add'
# elif operation == '-':
#     operation = 'subtract'
# elif operation == '*':
#     operation = 'multiply'
# elif operation == '/':
#     operation = 'divide'
result = calculator(num1, num2, operation)
print("The result is:", result)