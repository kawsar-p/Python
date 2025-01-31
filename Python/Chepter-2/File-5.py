# List range print

num = list(range(10))
print (num)

# Length print

iteam = ["C++", "100", "Apple","Mango"]
print(len(iteam))
# Adding and removing extra itam using append mood

iteam.append("CSE")
print(iteam)

iteam.pop()
print(iteam)

# Use of Insert function
iteam.insert(2,"Monkey") # index number and iteams name
print(iteam)

# Use of Remove function
iteam.remove("Monkey")
print(iteam)

# Use of sort and reverse function

iteam1 = [1,8,9,6,5,4,3,2,4.5] # Can't use string or integer/float same time   
iteam1.sort()
print(iteam1)
iteam1.reverse()
print(iteam1)

# copy list
iteam2 = iteam.copy()
print(iteam2)

# use of position seartching
position = iteam1.index(1)
print(position)

# use of count keyword
counts = iteam1.count(4)
print(counts)

# use of clear key
iteam.clear()
print(iteam)
