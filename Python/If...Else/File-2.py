A = int(input("Enter the first value: "))
B = int(input("Enter second value: "))
C = int(input("Enter thired value: "))

if A > B and A > C:
    print("Larget value: " , A )

elif B > A and B > C:
    print("Largest value: " , B)

else:
    print("\nLargest Value: ", C)