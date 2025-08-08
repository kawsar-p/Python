list = ["Apple",1,"Banana",2,"Cherry",3,"Date",4,"Elderberry",5]
print(list)

list[6]="Grapes" # Replace element
print(list)

list[0:3] = ["Orange", "Pineapple", "Mango"] # Replace multiple elements from index 0 to 2
print(list)

new_list = list + ["Kiwi", "Lemon"] # Adding new elements to the list
print(new_list)

del list[1:5] # Delete elements from index 1 to 4
print(list)