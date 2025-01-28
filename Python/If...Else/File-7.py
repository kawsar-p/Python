# Passing grade chacker program

A = int(input("Enter your marks: "))

if A >= 80 and A <=100:
    print("Your grade is A+")
elif A >= 70 and A < 80:
    print("Your grade is A")
elif A >= 60 and A < 70:
    print("Your grade is B")
elif A >= 50 and A < 60:
    print("Your grade is C")
elif A >= 40 and A < 50:
    print("Your garade is D")
else:
    print("You are fail")