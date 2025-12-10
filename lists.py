#List 
# Lists are used to store multiple items in a single variable.


mylist = ["apple","banana","cherry","apple"]            #ordered, changeable, Allow Duplicates
print(mylist)
print(len(mylist))

#List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list4 = ["abc", 34, True, 40, "male"]
print(list4)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#The list() Constructor

thislist2 = list(("apple","banana","cherry"))
print(thislist2)


thislist1 = ["maruti", "mercedes","Thar","Rolls Royce","G-Wagon"]
print(thislist1[1])     #access items
print(thislist1[-1])    #Negative Indexing
print(thislist1[2:5])   #Range

thislist = ["apple", "banana", "cherry"] #Change item value
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]    #Change a Range of Item Values
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry"] # insert Items
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"] #To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"] #Extend List """To append elements from another list to the current list, use the extend() method."""
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)