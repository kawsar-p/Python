print("Hello world")
print("\n")

# Variable Type
a = 200
b = 20.5
c= "Apple"

# Oparation
sum = a+b
sub = a-b
multi = a*b
div = a/b
apple = True

print("Output of Addition: ",sum)
print("Output of subtraction: ",sub)
print("Output of Multipication: ",multi)
print("Output of Division: ",div)
print("Bool", apple)
print("String: ", c)
print("\n")

# Type of
print(type(a))
print(type(b))
print(type(c))
print(type(apple))
print("\n")


# string
print("Apple and " + "Mango")
string1 = "IUBAT"
string2 = "- International University of Business Agriculture and Technology"
print(string1 + string2)

# User input
name = input("Enter Your name: ")
print(name)

num1= int(input("Enter Your integer value: "))
print(num1)
num1= float(input("Enter Your float value: "))
print(num1)
string= str(input("Enter Your string value: "))
print(string)

# Eval
evaluation = eval(input("Enter Your Evaluat value: "))
print(evaluation) 

# Temp Store vale
a5 = 2
b5 = 6

temp = a5
a5 = b5
b5 = temp

print(a5)
print(b5)

# Swap without temp
x=10
y=20
x,y=y,x
print(x)
print(y)

# Power and Mod
p1 = 2
print(a ** 2)

# OR
print(pow(a,2))


# Logical Operation AND, OR, NOT
print(2<3 and 3==3)
print(not((2!=2 or 2==4) and not(2!=8)))
 
# IS and IS not
print(1 is 1)
print(1 is not 5)

# Bitwise opearator 
# AND = &; OR = |; XOR = ^;   
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

print("\n")
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

print(bin(10))
print(oct(10))
print(hex(10))

ax = hex(10)
by = hex(50)

print(ax + by)

# Power
print(2**8)
print(pow(2,8))

# Membership Operator (In, Not In)

iubat= "International University of Business Agriculture and Technology"
print("Agriculture" in iubat)
print("Apple"not in iubat)

# Conditional Statement
a = 10
b =200
c = 5
if(a>b):
  print("True: A > B")

if(a==b):
  print("Eqal: A = B")
else:
  print("False: A!=B")

if(a>b and a>c):
  print("A is large")
elif(a<b and b>c):
  print("B is large")
elif(c>a and c>b):
  print("B is large")
else:
  print("All is Equal")

age = 20

if age >= 18:
    if age >= 21:
        print("You can drive and vote")
    else:
        print("You can vote but cannot drive")
else:
    print("You are under 18")

a=200
b=20
c=100
if a<b:
   if b==c:
      print("Apple")
   if b>c:
      print("Mango")
   else:
      print("Fuska")
else:
   print("Bananana")