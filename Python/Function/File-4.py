# User Defined and parameterized function
def Addition(a,b):
    sum = a+b
    return sum

a = int(input("Enter your first value: "))
b = int(input("Enter your second value: "))

result = Addition(a,b)
print("Addition: ", result)
