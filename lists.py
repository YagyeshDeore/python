mylist = ["apple", "banana", "cherry"]
print(mylist)
mylist.append("orange")
print(mylist)
mylist.remove("banana")
print(mylist)
mylist.insert(1, "blueberry")
print(mylist)
mylist.sort()
print(mylist)
length = len(mylist)
print("Length of the list is:", length)

# Additional list operations
mylist.pop()  # removes the last item
print(mylist)
mylist.reverse()
print(mylist)
mylist2 = ["kiwi", "mango"]
combined_list = mylist + mylist2
print(combined_list)
mylist.clear()
print(mylist)

print("data type of mylist is:", type(mylist))
#List inside List
nested_list = [1, 2, [3, 4], 5]
print(nested_list)
print(nested_list[2])  # Accessing the nested list
print(nested_list[2][1])  # Accessing an element in the nested list

#The list() constructor
fruits = list(("apple", "banana", "cherry")) # note the double round
print(fruits)

#python collections (Array
#list, tuple, set, dictionary


#extend list
fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["orange", "mango", "grapes"]
fruits1.extend(fruits2)
print(fruits1)

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  #loop through the index numbers
for i in range(len(thislist)):
    print(thislist[i])
#using while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
#list comprehension
[print(x) for x in thislist]
#Join two list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#list methods
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #Add an item to the end of the list
thislist.insert(1, "lemon") #Add an item at the specified index
thislist.remove("banana")   #Remove the item with the specified value
thislist.pop()              #Remove the last item in the list
thislist.clear()           #Remove all items from the list
print(thislist)

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#Python - Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()            #Sort the list alphabetically
print(thislist)
thislist.sort(reverse = True) #Sort the list descending
print(thislist)
#Customize Sort Function
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) 
#Python - Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)
#Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)
#Python - List Methods
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #Add an item to the end of the list
thislist.insert(1, "lemon") #Add an item at the specified index
thislist.remove("banana")   #Remove the item with the specified value
thislist.pop()              #Remove the last item in the list
thislist.clear()           #Remove all items from the list
print(thislist)     