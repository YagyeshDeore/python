myset = {"apple", "banana", "cherry"}
# apple
# banana
# cherry
#Check if "banana" is present in the set
print("banana" in myset)
# Output:
# True
#Add an item to a set
myset.add("orange")
print(myset)
# Output:
# {'banana', 'orange', 'cherry', 'apple'}
#Remove an item from a set
myset.remove("banana")
print(myset)
# Output:
# {'orange', 'cherry', 'apple'}
# apple
# orange
# cherry
#Loop through the set, and print the values
for x in myset:
    print(x)
# Output:
# apple
# orange
# cherry
#Get the length of the set
print(len(myset))
# Output:
# 3
#Remove the last item by using the pop() method
x = myset.pop()
print(x)
print(myset)
# Output:
# apple
# {'orange', 'cherry'}
#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round
print(thisset)
# Output:
# {'banana', 'cherry', 'apple'} 
# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Python - Join Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Output:
# {1, 2, 3, 'a', 'b', 'c'}
set1.update(set2)
print(set1)