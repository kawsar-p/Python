print("---> Menu <---\n")
print("1. Addition \n2. Subtradtion \n3. Multipication \n4. Division \n5. Modlus" )

A = int(input("\nEnter your choice: "))
print("\n")

if A == 1:
    print("Addition of two numbers")
    X = int(input("Enter the first value: "))
    Y = int(input("Enter the second value: "))
    print("\nThe sum of two numbers is : ", X + Y)

elif A == 2:
    print("Subtrction of two numbers")
    X = int(input("Enter the first value: "))
    Y  = int(input("Enter the Second value: "))
    X = int(input("Enter the first value: "))
    print("\nThe sub of two numbers is : ", X - Y)

elif A == 3:
    print("Multipication of two numbers")
    X = int(input("Enter the first value: "))
    Y  = int(input("Enter the second value: "))
    print("\nThe mul of two numbers is : ", X * Y)

elif A == 4:
    print("Divsion of two numbers")
    X = int(input("Enter the first value: "))
    Y  = int(input("Enter the fisecondrst value: "))
    
    print("\nThe div of two numbers is : ", X / Y)

elif A == 5:
    print("Modlus of two numbers")
    X = int(input("Enter the first value: "))
    Y  = int(input("Enter the second value: "))
    print("\nThe mod of two numbers is : ", X % Y)

else:
    print("Invalid input")