# Program to check the category of a number
number = int(input("Enter a number: "))

if number > 0:  # First condition
    if number % 2 == 0:  # Nested condition
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    if number < 0:  # Nested condition in else block
        print("The number is negative.")
    else:
        print("The number is zero.")
