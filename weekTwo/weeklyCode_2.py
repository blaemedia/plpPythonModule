'''Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list.'''

myList=[]

while True:
  
    user=eval(input("Enter digit value: "))
    myList.append(user)
    print("value inserted into the List",myList,"\n")
    if user==0:
        break

print(myList)
result=sum(myList)
print("\n sum of the values in the List",result,"\n")
        


    

    