feel = input("Are you sad?").lower()
# feel2 = input("Why are you sad?")
if feel == "yes":
    print("I hope you feel better soon!")
elif feel == "no":
 print("Good to hear that you are happy!")
else:
   print("It's okay to have mixed feelings sometimes.")

age = int(input("How old are you?"))
if age <= 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade A+")
elif marks >=80:
    print("Grade A")
elif marks >=70:
    print("Grade A-")
elif marks >=60:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else:
    print("Fail")


first_num = int(input("Enter first number:"))
second_num = int(input("Enter second number:"))
operation = input("What operation do you want to perform? '+', '-', '*', '/', '%'")
if operation == "+":
    print("The sum is:", first_num + second_num)
elif operation == "-":
    print("The difference between the numbers is:", first_num - second_num)
elif operation == "*":
    print("The product is:", first_num * second_num)
elif operation == "/":
    print("The division gives:", first_num/second_num)
elif operation == "%":
    print("The percentage is:", first_num % second_num)