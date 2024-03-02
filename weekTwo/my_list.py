# Declaring an empty list
my_list=[]

# Appending 4 values from the user
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Printing out the accepted values
print("4 values appended\n",my_list,"\n")

# Inserting the value 15 at the second position in the list.
my_list.insert(1,15)
print("15 inserted in the second position in the list \n",my_list,"\n")

# Extend my_list with another list: [50, 60, 70].
another_list=[50, 60, 70]
print(another_list)
my_list.extend(another_list)
print("Another list to be extended\n",my_list,"\n")

# Sort my_list in ascending order.
my_list.sort()
print("Sorted values of my_list\n",my_list,"\n")

# Find and print the index of the value 30 in my_list.
for i in my_list:
    if i == 30:
        print("Index of the value 30 in my_list\n",my_list.index(i),"\n")
